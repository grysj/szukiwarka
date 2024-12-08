import numpy as np
from scipy.sparse import load_npz
import pickle
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import time
from eng_help.funcs import *
import json

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

class Engine():
	with open('eng_help/word_list.pkl', 'rb') as file:
		word_list = pickle.load(file)
		m = len(word_list)
	stop_words = set(stopwords.words('english'))

	stemmer = SnowballStemmer("english")

	
	def __init__(self) -> None:
		self.US = []
		self.V = []
		ks = [500, 1000, 2000, 4000]
		for k in ks:
			self.US.append(np.load(f'matrices/{k}/US_{k}.npy'))
			self.V.append(np.load(f'matrices/{k}/V_{k}.npy'))
        
		self.M = load_npz("matrices/norm_matrix.npz")

    
	def get_search_v(self, query, param):
		q_mapped = create_map(query, self.stemmer, self.stop_words)

		vec_q = create_q(q_mapped,self.word_list,self.m)

		vec_res = vec_q @ self.M if param >3 else vec_q @ self.US[param] @ self.V[param]

		return vec_res

	def search(self, query, param=4, k=5):
		print(query)
		start = time.time()
		q_mapped = create_map(query, self.stemmer, self.stop_words)

		vec_q = create_q(q_mapped,self.word_list,self.m)

		vec_res = vec_q @ self.M if param >3 else vec_q @ self.US[param] @ self.V[param]

		vec_res = np.array(vec_res)
		


		k_biggest = get_k_biggest(vec_res, k)
		results = get_results(k_biggest)
		stop = time.time()
		data = dict()
		data["time"] = str(round(stop - start, 2))+ ' s'
		data["results"] = results
		data["query"] = query
		data = json.dumps(data, sort_keys=True)
		return data




        
          
        
