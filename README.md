# Cyberattack Detector AI: Real-Time Threat Detection

![GitHub release](https://img.shields.io/github/release/Tejas290/cyberattack-detector-AI.svg) [![Download Releases](https://img.shields.io/badge/Download%20Releases-Here-blue)](https://github.com/Tejas290/cyberattack-detector-AI/releases)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Model Training](#model-training)
- [Hyperparameter Optimization](#hyperparameter-optimization)
- [Web UI](#web-ui)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **Cyberattack Detector AI** is a FastAPI-based web application designed for real-time detection of cyberattacks. This application leverages machine learning to classify network traffic as either benign or an attack. With a trained model and dynamic feature input via a web user interface, it serves as a valuable tool for cybersecurity research and intelligent intrusion detection.

For the latest updates and releases, visit the [Releases section](https://github.com/Tejas290/cyberattack-detector-AI/releases).

## Features

- **Real-Time Detection**: Monitor network traffic and detect potential cyber threats in real-time.
- **User-Friendly Interface**: Easy-to-navigate web UI for inputting features and viewing results.
- **Dynamic Input**: Adjust input features dynamically to test various scenarios.
- **Machine Learning Model**: Utilizes a trained model for accurate predictions.
- **Scalability**: Designed to handle varying amounts of traffic data efficiently.
- **Research Ready**: Ideal for cybersecurity researchers and practitioners.

## Installation

To set up the Cyberattack Detector AI on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tejas290/cyberattack-detector-AI.git
   cd cyberattack-detector-AI
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

The application should now be running at `http://127.0.0.1:8000`.

## Usage

Once the application is running, navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI. Here, you can input your network traffic data to see whether it is classified as benign or an attack.

1. **Input Data**: Enter the necessary features into the provided fields.
2. **Submit**: Click on the "Execute" button to get predictions.
3. **View Results**: The results will display whether the traffic is benign or an attack.

## Architecture

The application is built using FastAPI, which allows for high performance and easy scalability. The architecture consists of the following components:

- **Frontend**: A web interface for user interaction.
- **Backend**: The FastAPI server that handles requests and predictions.
- **Model**: A trained machine learning model that classifies the input data.

### Diagram

![Architecture Diagram](https://example.com/architecture-diagram.png)

## Model Training

The model used in this application is a Multi-Layer Perceptron (MLP) classifier. The training process involves the following steps:

1. **Data Collection**: Gather a dataset of network traffic labeled as benign or attack.
2. **Preprocessing**: Clean and preprocess the data to make it suitable for training.
3. **Training**: Train the MLP classifier using the training dataset.
4. **Evaluation**: Evaluate the model's performance using a validation dataset.
5. **Tuning**: Optimize hyperparameters to improve accuracy.

### Example Code for Training

```python
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load your dataset
data = load_data()

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(data.features, data.labels, test_size=0.2)

# Initialize the model
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy}")
```

## Hyperparameter Optimization

Hyperparameter tuning is crucial for improving model performance. This application includes a hyperparameter optimization step that adjusts parameters like learning rate, number of layers, and neurons per layer.

### Techniques Used

- **Grid Search**: Systematically testing combinations of parameters.
- **Random Search**: Randomly sampling from the parameter space.
- **Bayesian Optimization**: Using probabilistic models to find the best parameters.

### Example Code for Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'hidden_layer_sizes': [(50,), (100,), (150,)],
    'activation': ['relu', 'tanh'],
    'solver': ['adam', 'sgd'],
}

grid_search = GridSearchCV(MLPClassifier(), param_grid, cv=3)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
```

## Web UI

The web user interface is built using HTML, CSS, and JavaScript. It provides an intuitive way for users to interact with the model.

### Features of the Web UI

- **Input Forms**: Easy-to-use forms for entering network traffic data.
- **Real-Time Feedback**: Instant results displayed after submission.
- **Responsive Design**: Works well on various devices, including mobile.

### Example Code for Web UI

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyberattack Detector</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Cyberattack Detector</h1>
    <form id="input-form">
        <label for="feature1">Feature 1:</label>
        <input type="text" id="feature1" name="feature1" required>
        <button type="submit">Submit</button>
    </form>
    <div id="result"></div>
    <script src="script.js"></script>
</body>
</html>
```

## Contributing

Contributions are welcome! If you want to contribute to the Cyberattack Detector AI, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the page.
2. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Make Changes**: Implement your changes and test them.
4. **Commit Your Changes**: Commit your changes with a clear message.
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Fork**: Push your changes to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
6. **Create a Pull Request**: Go to the original repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

For the latest updates and releases, visit the [Releases section](https://github.com/Tejas290/cyberattack-detector-AI/releases).