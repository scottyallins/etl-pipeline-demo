import json

def load_data(rows, path="data/output.jason"):
	with open(path, "w") as f:
		json.dump(rows, f, indent=2)
