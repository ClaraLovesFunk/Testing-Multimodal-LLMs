#!/usr/bin/env python3

import os
import itertools
import time
import json
CACHE_DIR = '/home/users/cwicharz/project/Testing-Multimodal-LLMs/data/huggingface_cache'
os.environ["TRANSFORMERS_CACHE"] = CACHE_DIR 
import argparse
import subprocess


with open('config.json', 'r') as f:
        config = json.load(f)

ds_name_all = config['dataset_names']
model_name_all = config['model_names']  


def run_inference(model_name, dataset_name):
    
    base_model_dir = "/home/users/cwicharz/project/Testing-Multimodal-LLMs/inference"
    base_dataset_dir = "/home/users/cwicharz/project/Testing-Multimodal-LLMs/datasets"
    venv_base_dir = "/home/users/cwicharz/project/Testing-Multimodal-LLMs/venvs" 

    model_path = os.path.join(base_model_dir, model_name)
    venv_path = os.path.join(venv_base_dir, model_name, "bin", "python") # Using the Python interpreter directly

    if not os.path.exists(model_path):
        print(f"Model path {model_path} does not exist!")
        return

    if not os.path.exists(venv_path):
        print(f"Virtual environment for {model_name} does not exist!")
        return

    cmd = [venv_path, os.path.join(model_path, "inference.py"), "--dataset", dataset_name]
    env = os.environ.copy()  
    env["TRANSFORMERS_CACHE"] = CACHE_DIR
    subprocess.run(cmd, env=env)


def run_all_inferences(model_names, dataset_names):
    for model, dataset in itertools.product(model_names, dataset_names):
        try:
            run_inference(model, dataset)
            
        except Exception as e:
            print(f"Error running inference for model {model} on dataset {dataset}. Error: {e}")


if __name__ == "__main__":

    start_time = time.time()

    parser = argparse.ArgumentParser(description="Run inference on a model with a given dataset.")
    parser.add_argument("-models", type=str, nargs='*', required=True, help="List of model names separated by spaces or commas. Use 'all' for all models.")
    parser.add_argument("-datasets", type=str, nargs='*', required=True, help="List of dataset names separated by spaces or commas. Use 'all' for all datasets.")
    
    args = parser.parse_args()

    args.models = ''.join(args.models).split(',')
    args.datasets = ''.join(args.datasets).split(',')

    if 'all' in args.models:
        args.models = model_name_all
    if 'all' in args.datasets:
        args.datasets = ds_name_all

    run_all_inferences(args.models, args.datasets)

    end_time = time.time()
    run_time = int((end_time - start_time)/60)
    print(f'runtime (min): {run_time}')