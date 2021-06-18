## Evaluation Script

f1_score.py

We are utilizing F1 score in our binary classification task. Being that controversial comments can include extremely hateful messages but we also do not want to censor speech, F1 score serves as a metric that will help us minimize false negatives while taking into account possible imbalance in classes. 

F1 score is the harmonic mean of the recall and precision of the model. The recall is defined as the true positives over the sum of true positives and false negatives. The precision is defined as the true positives over the sum of true positives and false positives. In our specific case, 0 is defined as the positive case in which it is not controversial and 1 is defined as the negative case where it is controversial. 

## Required format

Our script takes in two command-line arguments, each as the file path to a CSV file. The first command-line argument is the CSV file of the actual labels. This file should be formatted as 1 column with a header where each label is a separate row. The second command-line argument should be the predicted labels formatted as 1 column with a header where each label is a separate row. 
## Example:

Actual: [0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
Predicted: [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]

Suppose these labels are formatted as valid CSV's, called *actual.csv* and *predicted.csv* with valid headers. To compute the F1 score utilizing the script, the following is typed in terminal:

*$ python f1_score.py actual.csv predicted.csv*

The F1 score for the given example should then be printed in the format below:

*F1 Score is: 0.6666666666666665*