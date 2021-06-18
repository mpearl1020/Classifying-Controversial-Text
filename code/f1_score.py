import csv
import sys

if __name__ == '__main__':
  actual_csv = sys.argv[1]
  predicted_csv  = sys.argv[2]

  with open(actual_csv, newline='') as f:
    read = csv.reader(f)
    # [1:] to skip header, remove if no header
    actual_data = list(read)[1:]
  actual_data = [int(data[0]) for data in actual_data]

  with open(predicted_csv, newline='') as f:
    read = csv.reader(f)
    # [1:] to skip header, remove if no header
    predicted_data = list(read)[1:]
  predicted_data = [int(data[0]) for data in predicted_data]

  if (len(predicted_data) != len(actual_data)):
    print('Error: Lengths of two csvs are not the same')
    exit()

  tp = 0
  fp = 0
  fn = 0
  for val1, val2 in zip(actual_data, predicted_data):
    if (val1 == 1 and val2 == 1):
      tp += 1
    if (val1 == 0 and val2 == 1):
      fp += 1
    if (val1 == 1 and val2 == 0):
      fn += 1
  recall = tp / (tp + fp)
  precision = tp / (tp + fn)
  f1 = 2 * ((precision * recall) / (precision + recall))
  print("F1 Score is: " + str(f1))