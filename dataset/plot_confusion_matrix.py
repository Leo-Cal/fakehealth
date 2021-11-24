import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics._plot.confusion_matrix import ConfusionMatrixDisplay
from sklearn.model_selection import KFold, StratifiedKFold


#def main(predicted_y, expected_y, labels, largesize=False,title='Confusion matrix', filename='confusion_matrix.png'):
def main():
    

    labels = ['No','Yes']
    emotions = ["admiration","amusement","anger","annoyance","approval","caring","confusion","curiosity","desire","disappointment","disapproval","disgust","embarrassment","excitement","fear","gratitude","grief","joy","love","nervousness","optimism","pride","realization","relief","remorse","sadness","surprise","neutral"]
    with open(r'D:\FakeHealth-master\dataset\arrays for cms.csv') as f:
        reader = csv.reader(f)
        data = list(reader)
    first_row = data[0]
    data = data[1:]
    for emotion in emotions:
        print(emotion)
        expected_index = first_row.index("Expected {}".format(emotion))
        predicted_index = first_row.index("Predicted {}".format(emotion))
        filename = "{}_confusion_matrix.png".format(emotion)
        title = "Confusion matrix for {} (GoEmotion dataset)".format(emotion)
        
        expected_data = [x[expected_index] for x in data]
        predicted_data = [x[predicted_index] for x in data] 
    
        cm = confusion_matrix(expected_data, predicted_data)
        disp = ConfusionMatrixDisplay(cm, display_labels=labels)
        disp.plot(cmap=plt.cm.Blues, values_format='')
        plt.xlabel('Predicted result')
        plt.ylabel('Expected result')
        plt.title(title)
        plt.savefig(os.path.join("output", filename), dpi=200)
        plt.close()



main()