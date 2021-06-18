## Simple Baseline

Our task involved the binary classification of controversial text. With this in mind, we utilized the majority class baseline to determine the majority class of the training data and apply this class to all input in the testing data set. 

In order to utilize this script, two command-line arguments  must be supplied, the first being the path to the training CSV and the second being the path to the test CSV. This script will then output two files, the first titled *predicted_majority_test.csv*, the predicted labels for the test data given the majority class and the second file being *actual_test.csv*, the actual labels to the test set. Both files are formatted properly to be directly inputted as command-line args into our evaluation script, *f1_score*.

With these file names, we can directly call our evaluation metric with:
*python f1_score.py actual_test.csv predicted_majority_test.csv*
This returns an F1 score for the data of  __0.94689__, given that the majority of labels are uncontroversial given that the majority of online commentary is uncontroversial.