from asyncio.base_futures import _FINISHED
from cgi import test
import os
import csv
import xml.etree.ElementTree as ET
import spacy
import json
import pandas as pd
from collections import defaultdict
import numpy as np
import math
import re
import matplotlib.colors as mcl

root_file = os.getcwd()
nlp = spacy.load("en_core_web_sm")


def seg_sentence(sentence):
    doc = nlp(sentence)
    tokens = []
    id = 0
    for token in doc:
        id = id + 1
        tokens.append(token.text)
    return tokens





# Processing the query
def process(query,data_embeddings,category,categories,data):
    query_embed = nlp(query).vector
    scores = {}
    for word, embed in data_embeddings.items():
        category = categories[word]
        dist = query_embed.dot(embed)
        dist /= len(data[category])
        scores[category] = scores.get(category, 0) + dist
    return scores

def maxscore(wordscore):

    maxkeyvalue = max(zip(wordscore.values(), wordscore.keys()))[1]
    maxkey = max(zip(wordscore.values(), wordscore.keys()))[0]

    return maxkeyvalue, maxkey


def pre_process(tokens):
    rule_dict_list = []
    data = {
        'Actions': ['pick','grab','move','get','take','bring','put','carry','grasp','release','place','leave'],
        'Colors': ['yellow', 'red','green','orange','brown','turquoise']
        }
      # Words -> category
    categories = {word: key for key, words in data.items() for word in words}
    # Words -> category
    data_embeddings = {}
    for category, elements in data.items():
        for element in elements:
            data_embeddings[element] = nlp(element).vector

    for idx, token in enumerate(tokens):
        rule_dict = {}
        wordscore = process(token,data_embeddings,category,categories,data)
        entity = maxscore(wordscore)[0]
        entityvalue = maxscore(wordscore)[1]
        if entity == "Colors" and token in mcl.CSS4_COLORS:
            rule_dict["start"] = idx
            rule_dict["end"] = idx + 1
            rule_dict["type"] = "Color"
            rule_dict_list.append(rule_dict)
    return rule_dict_list




from tabulate import tabulate
def annotation_details(sentence,mydict):
    tokens = seg_sentence(sentence)
    table = [range(0,len(tokens)),tokens]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    entities = []
    finished_entity_input = False
    finished_relation_input = False
    rule_dict_list = pre_process(tokens)
    entities = entities + rule_dict_list
    print("entities: ",entities)
    while not finished_entity_input:
        e = input("Adding one entitiy, yes (y) or no (n)?")
        et = {}
        if e == 'y':
            et["start"] = int(input("Start: "))
            et["end"] = int(input("End: "))
            it = input("Type: Action (a) | Color (c) | Trajector (t) | SpatialIndicator (i) | GoalIndicator(g) ?")
            if it == "a":
                et["type"] = "Action"
            elif it == "t":
                et["type"] = "Trajector"
            elif it == "i":
                et["type"] = "SpatialIndicator"
            elif it == "g":
                et["type"] = "GoalIndicator"
            entities.append(et)
        elif e == 'n':
            finished_entity_input = True
            mydict["entities"] = entities
    relations = []
    for l in np.arange(0,len(mydict["entities"])):
        print("[",l,"]",mydict["entities"][l],end=" ")
        print("\n")
    while not finished_relation_input:
        e = input("Adding one relation, yes (y) or no (n)?")
        et = {}
        if e == 'y':
            et["head"] = int(input("Head: "))
            et["tail"] = int(input("Tail: "))
            it = input("Type: Spatial (s) | Transition (t) ?")
            if it =="s":
                et["type"] = "Spatial"
            elif it=="t":
                et["type"] = "Transition"
            relations.append(et)
        elif e == 'n':
            finished_relation_input = True
            mydict["relations"] = relations     
    return mydict

def annotation_semeval(index):
    path = "semeval-2014-task6/train_data/commands.txt"
    file = open(path)
    lines = file.readlines()
    count = 0
    mydict = {}
    # Strips the newline character
    for i in range(index,len(lines)):
        line = lines[i]
        line = line.strip()
        pattern = r'[0-9]'
        new_text = re.sub(pattern,'',line)
        new_text = new_text.strip()
        mydict["tokens"] = seg_sentence(new_text)
        mydict = annotation_details(new_text, mydict)
        filename = "dataset/semeval/s" + str(i) + ".json"
        with open(filename, 'w') as f:
            json.dump(mydict, f)



if __name__=='__main__':
    annotation_semeval(508)