import mlflow
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score

# 1. Connect to Local MLflow Tracking Server
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("mnist-mlp-classifier")

# 2. Load MNIST Dataset
print("Loading MNIST dataset...")
X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False, parser="auto")
X = X / 255.0  # Normalize pixel values to [0, 1]

# 10k subset for fast, clean convergence
X_train, X_test, y_train, y_test = train_test_split(
    X[:10000], y[:10000], test_size=0.2, random_state=42, stratify=y[:10000]
)

# 3. Define 6 Configurations (Architecture x Learning Rate)
experiments = [
    {"hidden_layer_sizes": (50,), "learning_rate_init": 0.001, "batch_size": 64},
    {"hidden_layer_sizes": (50,), "learning_rate_init": 0.01,  "batch_size": 64},
    {"hidden_layer_sizes": (100,), "learning_rate_init": 0.001, "batch_size": 64},
    {"hidden_layer_sizes": (100,), "learning_rate_init": 0.01,  "batch_size": 64},
    {"hidden_layer_sizes": (100, 50), "learning_rate_init": 0.001, "batch_size": 64},
    {"hidden_layer_sizes": (100, 50), "learning_rate_init": 0.01,  "batch_size": 64},
]

# 4. Run Experiment Loop
for i, config in enumerate(experiments, 1):
    arch_str = "-".join(map(str, config["hidden_layer_sizes"]))
    lr = config["learning_rate_init"]
    run_name = f"mlp-arch_{arch_str}-lr_{lr}"
    
    with mlflow.start_run(run_name=run_name):
        # Log Hyperparameters
        mlflow.log_param("architecture", str(config["hidden_layer_sizes"]))
        mlflow.log_param("learning_rate_init", config["learning_rate_init"])
        mlflow.log_param("batch_size", config["batch_size"])
        mlflow.log_param("max_iter", 30)

        # Train Model
        mlp = MLPClassifier(
            hidden_layer_sizes=config["hidden_layer_sizes"],
            learning_rate_init=config["learning_rate_init"],
            batch_size=config["batch_size"],
            max_iter=30,
            random_state=42,
            early_stopping=False
        )
        mlp.fit(X_train, y_train)

        # Evaluate Metrics
        preds = mlp.predict(X_test)
        val_acc = accuracy_score(y_test, preds)
        val_f1 = f1_score(y_test, preds, average="macro")
        final_train_loss = float(mlp.loss_curve_[-1])

        # Log Metrics
        mlflow.log_metric("train_loss", final_train_loss)
        mlflow.log_metric("val_accuracy", val_acc)
        mlflow.log_metric("val_f1_macro", val_f1)

        print(f"[{i}/6] {run_name} | train_loss: {final_train_loss:.4f} | val_acc: {val_acc:.4f}")

print("\nAll 6 experiments completed successfully!")
