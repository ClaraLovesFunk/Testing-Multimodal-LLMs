from utils.info import DatasetInfo
from utils.evaluation_metrics import compute_standard_metrics
from utils.evaluation_metrics import pipeline_preprocess

VALID_ANS_VALUES = ['positive', 'negative', 'neutral']
TASK_NAME = "sentiment analysis"
POS_LABEL = ""
label_name = "classification_label"
output_name = "output_sentiment analysis"
dataset_name = "mvsa"


def evaluate_mvsa(CONFIG_PATH, dataset_name, model_name, mode, run):

    # preprocess output & get valid answer ratio 
    y_pred_dict, y_true_dict, _, valid_ans_ratio_dict = pipeline_preprocess(
         CONFIG_PATH, VALID_ANS_VALUES, dataset_name, model_name, run, mode)
    
    # do the evaluation, but with output data transformed according to evaluation modus
    scores_dict = {}
    examples_dict = {}
    
    DatasetInfo_instance = DatasetInfo(dataset_name)
    tasks = DatasetInfo_instance.get_tasks()
    for task in tasks:
        y_pred = y_pred_dict[task]
        y_true = y_true_dict[task]

        scores = compute_standard_metrics(
            y_true, 
            y_pred, 
            pos_label=POS_LABEL, 
            average='weighted', 
            zero_division=0, 
            flag_only_acc=False)
        scores_dict[task] = scores

    return scores_dict, examples_dict, valid_ans_ratio_dict