from transformers import pipeline, AutoTokenizer

def transformss():
    
    classifier = pipeline('text-generation',pad_token_id = 50256)
    return classifier

