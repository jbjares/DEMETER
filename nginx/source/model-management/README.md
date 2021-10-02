# Model Management and Experiment Tracking using MLFlow

## build 
```
docker build . -t mlflow-tracking
```

## run
```
docker run -p 5000:5000 -v ${PWD}/mlruns:/mlruns -v ${PWD}/mlartifacts:/mlartifacts mlflow-tracking 
```

## usage (example)
```
pip install mlflow scikit-learn
python fertilizers_test.py
```
Open `localhost:5000` to see tracked `fertilizers` experiment in MLFlow tracking ui.

## dockerhub
https://hub.docker.com/r/crmne/mlflow-tracking
