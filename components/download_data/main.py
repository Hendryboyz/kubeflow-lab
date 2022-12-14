import argparse
import json
from pathlib import Path
from sklearn import datasets, model_selection

def __create_arg_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser()
  parser.add_argument('--data', type=str)
  return parser

def __download_data(args: argparse.Namespace):
  x, y = datasets.load_breast_cancer(return_X_y=True)
  x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
  
  data = {
    'x_train': x_train,
    'x_test': x_test,
    'y_train': y_train,
    'y_test': y_test 
  }
  
  data_json = json.dumps(data)
  with open(args.data, 'w') as out_file:
    json.dump(data_json, out_file)

if __name__ == '__main__':
  args = __create_arg_parser().parse_args()
  
  Path(args.data).parent.mkdir(parents=True, exist_ok=True)
  
  __download_data(args)
  
  
  
  
  