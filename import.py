import kagglehub

# Download latest version
path = kagglehub.dataset_download("willianoliveiragibin/grocery-inventory")

print("Path to dataset files:", path)