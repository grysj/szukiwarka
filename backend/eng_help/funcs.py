import numpy as np
from scipy.sparse import csr_matrix
from collections import Counter

from nltk.tokenize import word_tokenize
import time
import sqlite3


def create_map(query, stemmer, stop_words):
    words = word_tokenize(query.lower())
    

    filtered_words = [stemmer.stem(word) for word in words if word.isalpha() and word not in stop_words]
    
    return Counter(filtered_words)


def create_q(word_map, union_list, n):
    q_i= np.zeros(n)

    i = 0
    for word in union_list:
        q_i[i,] = word_map.get(word, 0)
        i += 1
    
    return q_i/np.linalg.norm(q_i)


def get_k_biggest(arr, k):
    arr = list(enumerate(arr, start=1))
    arr.sort(key = lambda x: -x[1])
    return arr[:k]

def get_results(to_find):
    conn = sqlite3.connect('database/sites.db')
    results = []
    cursor = conn.cursor()
    
    sqlquery = 'SELECT link, title FROM links WHERE idx=?'

    for idx, prob in to_find:
        result = dict()
        cursor.execute(sqlquery, (idx,))
        href, name = cursor.fetchone()
        result["prob"] = str(round(prob * 100, 2)) + "%"
        result["name"] = name
        result["href"] = href
        results.append(result)
    return results

