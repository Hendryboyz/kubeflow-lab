from kfp import components

@components.func_to_container_op
def show_results(
  decision_tree: float,
  logistic_regression: float
) -> None:
  print(f'Decision tree (accuracy): {decision_tree}')
  print(f'Logistic regression (accuracy): {logistic_regression}')