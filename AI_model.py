# from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer
# model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
# tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M", src_lang="en", tgt_lang="ko")

# encoded_en = tokenizer(src_text[0], return_tensors="pt")
# generated_tokens = model.generate(**encoded_en, forced_bos_token_id=tokenizer.get_lang_id("ko"))
# answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# ''' fine-tuning 시 loss 값 뽑는 코드(forward pass)

# model_inputs = tokenizer(src_text, text_target=tgt_text, return_tensors="pt")
# loss = model(**model_inputs).loss  # forward pass
# '''

# print(answer)

title = ["Protesters storm BlackRock’s Paris office holding red flares and firing smoke bombs Every year, tens of thousands of migrants fleeing war, persecution and poverty risk the treacherous route in search of better economic prospects. They travel in dinghies that are unfit for the journey and can be left stranded, sparking major diplomatic rows between European countries in the region."]

text = ["Protesters storm BlackRock’s Paris office holding red flares and firing smoke bombs Every year, tens of thousands of migrants fleeing war, persecution and poverty risk the treacherous route in search of better economic prospects. They travel in dinghies that are unfit for the journey and can be left stranded, sparking major diplomatic rows between European countries in the region."]

import pprint as pp
import json
import torch
from transformers import AutoTokenizer, LongT5ForConditionalGeneration
device =  'cpu'

model_name = "pszemraj/long-t5-tglobal-base-16384-book-summary"
model = LongT5ForConditionalGeneration.from_pretrained(model_name)
sum_tokenizer = AutoTokenizer.from_pretrained('t5-base')

def generate_summary(text):
    input_ids = sum_tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True).to(device)
    summary_ids = model.generate(input_ids.to(device), max_length=150, num_beams=2, early_stopping=True)
    summary = sum_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

model.to('cpu')

summary = generate_summary(text[0])
print(summary)


