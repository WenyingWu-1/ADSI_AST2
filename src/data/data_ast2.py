# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os.path
import json

def show_cat_col_info(df,cat_cols):
    for i in cat_cols:
        print(f'Column - {i}: {len(df[i].unique())} unique values')
        print(df[i].unique())
        print()


def create_cats_dict(df,cat_cols):
    cats_dict = dict()
    for i in cat_cols:
        cats_dict[i] = list(df[i].unique())
    return cats_dict


def generate_cat_mapping_dict(df,col):
    col = df[col].astype('category')
    col_dict = dict(enumerate(col.cat.categories))
    col_dict = dict((v,k) for k,v in col_dict.items())
    return col_dict

def save_dicts(brewery_name_dict=None, beer_style_dict=None, path='../data/processed/'):
    if brewery_name_dict is not None:
        file = open(f"{path}brewery_name_dict.json", "w")
        json.dump(brewery_name_dict, file)
        file.close()
    
    if beer_style_dict is not None:
        file = open(f"{path}beer_style_dict.json", "w")
        json.dump(beer_style_dict, file)
        file.close()
    
def read_dicts(path='../data/processed/'):
    
    if os.path.isfile(f'{path}brewery_name_dict.json'):
        file = open(f"{path}brewery_name_dict.json", "r")
        brewery_name_dict = json.load(file)
        file.close()
    
    if os.path.isfile(f'{path}beer_style_dict.json'):
        file = open(f"{path}beer_style_dict.json", "r")
        beer_style_dict = json.load(file)
        file.close()
    
    return brewery_name_dict, beer_style_dict


def get_class_distribution(obj, beer_style_dict):
    dict_length = len(beer_style_dict)
    helper_list = list(range(104))
    count_dict = dict()
    for i in helper_list:
        count_dict[f"type_{str(i)}"] = 0
    
    for i in obj:
        if i in helper_list:
            count_dict[f"type_{i}"] +=1              
            
    return count_dict