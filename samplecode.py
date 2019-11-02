# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import re
import numpy as np
import json
import flask
from flask import Flask,request

app=Flask(__name__)

@app.route('/home')
def test_api():
    return  "Yay/// My API is working.."

@app.route('/topwords',methods=['POST'])
def find_top_words():
    data = json.loads(request.data.decode())
    text,num_words = data['text'],data['num']
    word_tokens =re.split(' |;|,|:',text)
    word_len = [len(word) for word in word_tokens]
    sorted_len = np.argsort(word_len)
    top_words=[]
    for idx in sorted_len[-num_words:]:
        top_words.append(word_tokens[idx])
    return str(top_words)

@app.route('/lastwords',methods=['POST'])
def find_last_words():
    data = json.loads(request.data.decode())
    text,num_words = data['text'],data['num']
    word_tokens =re.split(' |;|,|:',text)
    word_len = [len(word) for word in word_tokens]
    sorted_len = np.argsort(word_len)
    last_words=[]
    for idx in sorted_len[:num_words]:
        last_words.append(word_tokens[idx])
    return str(last_words)        


if __name__=='__main__':
    app.run(host='localhost',port=5000,debug=True)
