from typing import Union
from fastapi import FastAPI, UploadFile, File
import requests
import json
from itertools import islice
import bisect

app = FastAPI()

requestHandled_Count = 0
sumRequestHandleTimeMs = 0

@app.get("/dictionary")
def collect_statistics(prefix: str):
    global requestHandled_Count
    global sumRequestHandleTimeMs
    find_match_url = 'http://127.0.0.1:8000/show_dictionary?prefix=' + prefix
    response = requests.get(find_match_url)
    # The time it took the service to handle the requests.
    sumRequestHandleTimeMs += response.elapsed.total_seconds()
    requestHandled_Count += 1
    return json.loads(response.text)

@app.get("/show_dictionary")
# get the list starts with the prefix
def find_match(prefix: str):
    with open("dictionary.txt", "r") as dictionary_file:
        match = [word.strip() for word in islice(dictionary_file, None) if word.startswith(prefix)] 
    return match

@app.get("/statistics")
def get_statistics():
     # The average time it took the service to handle the requests.
    averageRequestHandleTimeMs = sumRequestHandleTimeMs /requestHandled_Count
  
    # How many requests did the service handled.
    requestHandledCount =requestHandled_Count
    
    # How many words are in the dictionary.
    with open("dictionary.txt", "r") as dictionary_file:
        for count, line in enumerate(dictionary_file):
            pass
    wordCount = count + 1

    statistics = {
        "averageRequestHandleTimeMs ": averageRequestHandleTimeMs,
        "requestHandledCount ": requestHandledCount,
        "wordCount ": wordCount
    }
    return statistics

@app.post("/update_dictionary")
def insert_words_to_dictionary(words_file_name: UploadFile = File(...)):
    dictionary_file_name = "dictionary.txt"
    with open(dictionary_file_name, "r") as f:
        contents = f.readlines()
        
    with open(words_file_name.filename, "r") as words_file:
        for word in words_file:
          bisect.insort(contents, word)
              
    with open(dictionary_file_name, "w") as f:
      contents = "".join(contents)
      f.write(contents)

    return {"Update successfully"}
