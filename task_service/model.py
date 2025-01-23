import os,json,time

class TaskDB:
	data_model = {
		"name":str,
		"id":str,
	}

	storage_file = "/tmp/tasks.db"

	def __init__(self):
		self.tasks = []
		self.last_loaded = 0

		if not os.path.exists(TaskDB.storage_file):
			self.save_db()

	def load_db(self):
		current_time = time.time()
		if current_time - self.last_loaded < 30:
			print("Using cached data.")
			return self.tasks

		with open(TaskDB.storage_file) as f:
			self.tasks = json.load(f)
			self.last_loaded = current_time
		return self.tasks

	def save_db(self):
	    with open(TaskDB.storage_file, 'w') as f:
	    	json.dump(self.tasks,f)

	def add_task(self,task_data):
		if self.validate(task_data):
			self.tasks.append(task_data)
			self.save_db()
			return True
		return False

	def validate(self, data):
		for k,v in TaskDB.data_model.items():
			if k not in data or not isinstance(data[k], v):
				return False

		# for i in self.tasks:
		# 	if i["id"] == data["id"]:
		# 		return False

		return True