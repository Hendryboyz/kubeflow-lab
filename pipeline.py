from kfp import dsl, components, compiler
from components.show_results.func import show_results

@dsl.pipeline(name='First Pipeline', description='Applies Decision Tree and Logistic Regression for classification problem.')
def pipeline(demo: str=''):
  download = components.load_component_from_file('components/download_data/component.yaml')
  decision_tree = components.load_component_from_file('components/decision_tree/component.yaml')
  logistic_regression = components.load_component_from_file('components/logistic_regression/component.yaml')
  
  download_task = download()
  
  decision_tree_task = decision_tree(download_task.output)
  logistic_regression_task = logistic_regression(download_task.output)
  
  show_results(decision_tree_task.output, logistic_regression_task.output)
  

if __name__ == '__main__':
  compiler.Compiler().compile(pipeline)