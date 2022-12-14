#!/bin/bash
docker login -u hendryboyz -p WoxN0524*

for COMPONENT in $(ls components/);
do
  if [ $COMPONENT = "show_results" ]; then
    continue
  fi
  docker rmi -f hendryboyz/kubeflowpoc:$COMPONENT
  docker build -t hendryboyz/kubeflowpoc:$COMPONENT --build-arg COMPONENT=$COMPONENT .
  docker push hendryboyz/kubeflowpoc:$COMPONENT
done