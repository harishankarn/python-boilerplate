import json
import sys
import os
import logging
from pathlib import Path

class Utilities:
	logger = logging.getLogger(__name__)

	def __init__(self):  
		print("Logger", self.logger) 
		source_path = str(Path("./").resolve())
		sys.path.append(source_path) 
	def push_var(self,key,val,file_path):

		vars = json.loads(open(file_path))

		if key not in vars:
			vars[key] = val
			with open(file_path, 'w') as f:
				json.dump(data, f)
		else:
			raise Exception(f"{key} already exists in {path} !")

	def get_value(self,key,file_path):
		with open(file_path) as config_file:
			keys = json.load(config_file)
			return keys[key]

	def get_data(self,file_path,repo):
		import dvc.api
		with dvc.api.open(file_path,repo=repo) as fd:
			return fd
