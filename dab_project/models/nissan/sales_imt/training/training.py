import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load sample data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)

# Train a model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Set the tracking URI to Databricks if not set
mlflow.set_tracking_uri('databricks')
mlflow.set_registry_uri('databricks-uc')
# Define the name for the registered model in Unity Catalog
model_name = "citibike_dev.models.testmodel2"

exp_path = "/Workspace/Users/torranceross@ymail.com/test_exp2"

# Create or set the experiment
mlflow.set_experiment(exp_path)

# Log the model with Unity Catalog registration
with mlflow.start_run():
    mlflow.sklearn.log_model(
        sk_model=clf,
        # name= 'sklearn-model2',
        artifact_path="sklearn-model",
        registered_model_name=model_name,
        input_example=X_test[:5]
    )

    # Alternatively, log metrics and other artifacts if needed
    mlflow.log_metric("accuracy", clf.score(X_test, y_test))