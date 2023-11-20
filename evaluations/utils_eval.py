import re
import string
import json
from sklearn import metrics


def extract_answer(model, dataset, output_raw):

    if model == 'idefics':
        output_clean = output_raw.split("\nAssistant: ")[-1].strip().lower() #Extracting the answer after "Assistant: "
            
    elif model == 'openflamingo':
        # Using a regular expression to capture the portion after "\nAnswer:" followed by any number of dots
        if dataset in ['hateful_memes', 'mami', 'esnlive', 'scienceqa', 'aokvqa', 'clevr', 'gqa']:
            match = re.search(r'\nAnswer:\.+(.*)', output_raw)
        if dataset in ['mvsa']:
            match = re.search(r'\nSentiment: \.+(.*)', output_raw)
        if dataset in ['mami']:
            match = re.search(r'\nSexism Label: \.+(.*)', output_raw)
        if dataset in ['hateful_memes']:
            match = re.search(r'\nHate Label: \.+(.*)', output_raw)
        if match:
            output_clean = match.group(1).strip().lower()
        else:
            output_clean = output_raw

    elif model == 'adept':
        # Corrected regular expression pattern to match the text following \u0004
        pattern = r'\u0004\s(.+)'
        match = re.search(pattern, output_raw)
        if match:
            output_clean = match.group(1).strip().lower()
        else:
            output_clean = output_raw

                
        

    else:
        output_clean = output_raw.lower()

    # Remove any punctuation from the output
    output_clean = ''.join(ch for ch in output_clean if ch not in string.punctuation)

    return output_clean


def compute_standard_metrics(y_true, y_pred, pos_label, average='binary', zero_division=0, flag_only_acc = False):

    if y_pred == []: # if no valid predictions were made, model cannot be evaluated
        invalid_ans = float('nan')
        scores = {
            'accuracy': invalid_ans, 
            'precision': invalid_ans, 
            'recall': invalid_ans, 
            'f1': invalid_ans}

    else:
        if flag_only_acc == True:
            scores = {
                        'accuracy': metrics.accuracy_score(y_true, y_pred),
                        }
        
        if flag_only_acc == False:
            if average=='binary':
                scores = {
                    'accuracy': metrics.accuracy_score(y_true, y_pred),
                    'precision': metrics.precision_score(y_true, y_pred, average = average, pos_label=pos_label, zero_division=zero_division),
                    'recall': metrics.recall_score(y_true, y_pred, average = average, pos_label=pos_label, zero_division=zero_division),
                    'f1': metrics.f1_score(y_true, y_pred, average = average, pos_label=pos_label, zero_division=zero_division),                  
                }

            else:
                scores = {
                    'accuracy': metrics.accuracy_score(y_true, y_pred),
                    'precision': metrics.precision_score(y_true, y_pred, average = average, zero_division=zero_division),
                    'recall': metrics.recall_score(y_true, y_pred, average = average, zero_division=zero_division),
                    'f1': metrics.f1_score(y_true, y_pred, average = average, zero_division=zero_division),                  
                }
    return scores


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)
    

def get_id_2_label_dict(data_text, label_name, dataset_name):

    if dataset_name =="blub":
        print('blup')
    # if dataset_name == 'aokvqa':
    #     if t

    else:
        data_text = data_text["data"]
            
        labels = {
            item["text_input_id"]: item[label_name]
            for item in data_text
            if "text_input_id" in item and label_name in item
        }

    return labels


def get_clean_valid_preds_trues(output, output_name, VALID_ANS_VALUES, labels, model, dataset_name, data_text, mode, task = None):
    
    
    y_true, y_pred = [], []
    valid_count = 0

    # if dataset_name not in ['aokvqa'] and mode != 'hard':
    #     data_text = data_text["data"]
    data_text = data_text["data"]

    for item in output:      
        
        output_raw = str(item[output_name]) 
        pred_value = extract_answer(model, dataset_name, output_raw)
        
        
        if VALID_ANS_VALUES == "sample-dependent":
            
            if dataset_name in ["scienceqa"]:    
                sample = next((d for d in data_text if d['text_input_id'] == item["text_input_id"]), None)
                if sample is not None:
                    no_choices = len(sample['answer_choices'])
                    VALID_ANS_VALUES_sample_dependent = [str(i) for i in range(no_choices)]
                    if pred_value in VALID_ANS_VALUES_sample_dependent and item["text_input_id"] in labels:   
                        valid_count += 1
                        y_pred.append(pred_value)
                        y_true.append(str(labels[item["text_input_id"]]).lower())
            
            elif dataset_name in ["aokvqa"]:
                if mode == 'soft':
                    sample = next((d for d in data_text if d['text_input_id'] == item["text_input_id"]), None)
                    if sample is not None:
                        VALID_ANS_VALUES_sample_dependent = sample['answer_choices']
                        pred_value = pred_value.lower()
                        if item["text_input_id"] in labels and pred_value in VALID_ANS_VALUES_sample_dependent: #mode == 'hard' and pred_value in VALID_ANS_VALUES 
                            valid_count += 1
                            y_pred.append(pred_value)
                            y_true.append(labels[item["text_input_id"]])
                            
                            
                        

                # print(data_text)
                # print('TEEEESSSST1')
                # sample = next((d for d in data_text if d['text_input_id'] == item["text_input_id"]), None)
                # print('TEEEESSSST2')
                
                # if task == 'hard':
                #     if task == "multiple choice (aokvqa)":
                #         if sample is not None:
                #             VALID_ANS_VALUES_sample_dependent = sample['answer_choices']
                #             if pred_value in VALID_ANS_VALUES_sample_dependent and item["text_input_id"] in labels:   
                #                 valid_count += 1
                #                 y_pred.append(pred_value)
                #                 y_true.append(str(labels[item["text_input_id"]]).lower())
                
                # elif task == 'soft':
                #     print('TEEEESSSST3')
                #     if task == "direct answer (aokvqa)":
                #         if sample is not None:
                #             if item["text_input_id"] in labels:   
                #                 valid_count += 1
                #                 y_pred.append(pred_value)
                #                 y_true.append(str(labels[item["text_input_id"]]).lower())
                #     elif task == "multiple choice (aokvqa)":
                #         if sample is not None:
                #             VALID_ANS_VALUES_sample_dependent = sample['answer_choices']
                #             if pred_value in VALID_ANS_VALUES_sample_dependent and item["text_input_id"] in labels:   
                #                 valid_count += 1
                #                 y_pred.append(pred_value)
                #                 y_true.append(str(labels[item["text_input_id"]]).lower())
            
        # direct answer tasks for which we do not determine what a valid answer is and what not
        elif VALID_ANS_VALUES == "no-ans-validity":
            if mode == 'hard':
                if item["text_input_id"] in labels:
                    y_pred.append(pred_value)
                    y_true.append(str(labels[item["text_input_id"]]).lower())
                valid_ans_ratio = None
            if mode == 'soft':
                if item["text_input_id"] in labels:
                    label_str = str(labels[item["text_input_id"]]).lower()
                    if label_str in pred_value:
                        y_pred.append(label_str)
                    else:
                        y_pred.append(pred_value)
                    y_true.append(label_str)
                valid_ans_ratio = None

        # for classification or multiple choice task, where valid answers are the same for all instances
        else:
            if mode == 'hard' and pred_value in VALID_ANS_VALUES and item["text_input_id"] in labels:
                valid_count += 1
                y_pred.append(pred_value)
                y_true.append(str(labels[item["text_input_id"]]).lower())

            elif mode == 'soft':
                matched_values = [val for val in VALID_ANS_VALUES if val in pred_value]
                if len(matched_values) == 1 and item["text_input_id"] in labels:
                    valid_count += 1
                    y_pred.append(matched_values[0])
                    y_true.append(str(labels[item["text_input_id"]]).lower())

    valid_ans_ratio = valid_count / len(output) if output else 0

    return valid_ans_ratio, y_pred, y_true


def get_examples(ds, output, output_name, labels):
    
    if ds == 'okvqa':
        examples = {
            item["text_input_id"]: 1 if any(str(label).lower() == str(item.get(output_name)).lower() for label in labels[item["text_input_id"]]) else 0
            for item in output
            if "text_input_id" in item and item["text_input_id"] in labels
        }

    else:
        examples = {
            item["text_input_id"]: 1 if str(labels[item["text_input_id"]]) == item.get(output_name) else 0
            for item in output if "text_input_id" in item and item["text_input_id"] in labels
        }

    return examples