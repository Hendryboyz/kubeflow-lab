import argparse
import json
from pathlib import Path
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

def __create_arg_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser()
  parser.add_argument('--data', type=str)
  parser.add_argument('--accuracy', type=str)
  return parser


def __load_input_data(args: argparse.Namespace) -> dict:
  with open(args.data, 'r') as data_file:
    data = json.load(data_file)
    return json.load(data)

def __logistic_regression(args: argparse.Namespace):
  data = __load_input_data()
  
  x_train = data['x_train']
  x_test = data['x_test']
  y_train = data['y_train']
  y_test = data['y_test']
  model = LogisticRegression()
  model.fit(x_train, y_train)
  
  y_pred = model.predict(x_test)
  
  accuracy = accuracy_score(y_test, y_pred)
  
  with open(args.accuracy, 'w') as out_file:
    out_file.write(str(accuracy))

if __name__ == '__main__':
  parser = __create_arg_parser()
  args = parser.parse_args()
  
  Path(args.accuracy).parent.mkdir(parents=True, exist_ok=True)
  
  __logistic_regression(args)