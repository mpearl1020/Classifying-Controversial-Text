import csv
import sys
import pandas as pd

if __name__ == '__main__':
  train_csv = sys.argv[1]
  test_csv  = sys.argv[2]

  train_df = pd.read_csv(train_csv).drop(columns=['Unnamed: 0'])
  test_df = pd.read_csv(test_csv).drop(columns=['Unnamed: 0'])
  
  not_contro = len(train_df[train_df['contro'] == 0])
  contro = len(train_df[train_df['contro'] == 1])

  majority = 1 if contro > not_contro else 0
  predictions = []
  for i in range(len(test_df)):
    predictions.append(majority)
  
  header = ['predicted_labels']
  with open('predicted_majority_test.csv', 'w', newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    for val in predictions:
      writer.writerow(str(val))

  actual_labels = test_df['contro'].to_list()
  header = ['actual_labels']
  with open('actual_test.csv', 'w', newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    for val in actual_labels:
      writer.writerow(str(val))
  
