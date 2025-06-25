import requests

# Set your local FastAPI endpoint
url = "http://127.0.0.1:8000/predict"

# Load the same features used in training
import joblib
features = joblib.load("features.pkl")

# Fill in example values for all features
example_input = {
    feature: 0.0 for feature in features  # Default values (you can set real ones)
}
example_input[features[0]] = 123456.0  # Example modification
example_input[features[1]] = 1.0
# ... fill more if needed

# Send POST request
response = requests.post(url, data=example_input)

# Print the response HTML content
print(response.text)
