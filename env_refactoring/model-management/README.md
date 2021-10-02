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
python examples/example.py
```
Open `localhost:5000` to see tracked `test_experiment` experiment in MLFlow tracking ui.

