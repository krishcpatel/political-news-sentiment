from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def match_label_and_value_with_highest_value(values, labels):
    # Get the index of the highest value
    highest_value_index = values.index(max(values))
    # Return the corresponding label and value
    return labels[highest_value_index], values[highest_value_index]

def predict_politics(text):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

    inputs = tokenizer(text, return_tensors="pt")
    labels = torch.tensor([0])
    outputs = model(**inputs, labels=labels)
    loss, logits = outputs[:2]

    values = logits.softmax(dim=-1)[0].tolist()

    labels = ['Left', 'Center', 'Right']
    highest_value_label, highest_value = match_label_and_value_with_highest_value(values, labels)
    return highest_value_label, highest_value, values