import numpy as np
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle


def train_svm_model():
	data = pd.read_excel('titanic.xls')
	
	labels = data['survived']
	
	features = data.drop(["survived", "name", "ticket", "cabin", "embarked", "boat", "body", "home.dest"], axis=1)
	
	mapping = {"male": 0, "female": 1}
	
	features.replace({"sex": mapping}, inplace=True)
	
	labels.fillna(0, inplace=True)
	features.fillna(20, inplace=True)
	
	classifier = SVC()
	
	print(features.columns.values)
	
	X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.10, shuffle=True)
	
	classifier.fit(X_train, y_train)
	
	print(X_train)
	
	accuracy = classifier.score(X_test, y_test) * 100
	
	if accuracy > 70:
		with open("classifier.pickle", "wb") as f:
			pickle.dump(classifier, f)
		print("Accuracy is %3d%% so we saved it" % accuracy)
		
	else:
		print("Accuracy is %3d%% but we didn't save" % accuracy)
	
	

def guess_if_survived(pclass, sex, age, siblings, parents, fare_price):
	
	with open("classifier.pickle", "rb") as f:
		classifier = pickle.load(f)
		
	input = {}
	input['pclass'] = [pclass]
	input['sex'] = [sex]
	input['age'] = [age]
	input['siblings'] = [siblings]
	input['parents'] = [parents]
	input['fare_price'] = [fare_price]
	
	features = pd.DataFrame(input)
		
	prediction = classifier.predict(features)
	
	if prediction[0]:
		print("You survived")
		
		return True
	else:
		print("You died")
		
		return False


if __name__ == "__main__":
	guess_if_survived(1, 0, 18, 1, 2, 100)
	guess_if_survived(2, 0, 60, 3, 2, 10)