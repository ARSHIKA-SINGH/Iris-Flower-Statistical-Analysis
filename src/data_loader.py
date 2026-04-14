import pandas as pd
# Function to load dataset safely using try-except
def load_data():
    try:
        df = pd.read_csv("data/iris.csv")
        # Rename columns for easier access
        df.columns = [
            "id",
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "species"
        ]
        # Remove "Iris-" prefix from species names
        df["species"] = df["species"].str.replace("Iris-", "")
        return df


    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None

    except Exception as e:
        print("Error:", e)
        return None