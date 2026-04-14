from functools import reduce
from utils import recursive_sum, recursive_count
# Display rows and info
def display_data(df):
    print(df.head(10))
    print(df.tail(5))
    print(df.info())
    print("\nRows where sepal_length > 5:\n")
    for index, row in df.iterrows():
        if row["sepal_length"] > 5:
            print(row)

# Manual outlier detection
def detect_outliers_manual(df, column):
    values = list(df[column])
    values = sorted(values)
    n = len(values)
    q1 = values[n // 4]
    q3 = values[(3 * n) // 4]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = []
    for value in values:
        if value < lower:
            outliers.append(value)
        elif value > upper:
            outliers.append(value)
    return outliers

# Add new columns
def add_new_columns(df):
    df["petal_area"] = df["petal_length"] * df["petal_width"]
    df["petal_to_sepal_ratio"] = (
        df["petal_length"] / df["sepal_length"]
    )
    df["combined_score"] = (
        df["sepal_length"]
        + df["petal_length"]
        - df["sepal_width"]
    )

    # Validation using loops
    for i in range(len(df)):
        if df["petal_area"][i] < 0:
            print("Invalid petal area found.")
    return df

# Encode species and do bitwise AND
def bitwise_species(df):

    mapping = {
        "setosa": 1,
        "versicolor": 2,
        "virginica": 3
    }
    encoded = []
    for species in df["species"]:
        encoded.append(mapping[species])
    print("\nBitwise AND Comparison:\n")
    for i in range(0, len(encoded)-1):
        result = encoded[i] & encoded[i+1]
        print(
            encoded[i],
            "&",
            encoded[i+1],
            "=",
            result
        )

# Unique tuple set
def unique_measurements(df):
    unique_set = set()
    for index, row in df.iterrows():
        tup = (
            row["sepal_length"],
            row["sepal_width"],
            row["petal_length"],
            row["petal_width"]
        )
        unique_set.add(tup)
    print("\nUnique Measurement Count:")
    print(len(unique_set))
    return unique_set

# Manual statistics
def manual_statistics(df, column):
    values = list(df[column])


    # Replace NaN/0 with mean
    clean_values = []
    for v in values:
        if v == 0:
            continue
        else:
            clean_values.append(v)
    total = recursive_sum(clean_values)
    count = recursive_count(clean_values)
    mean = total / count
    sorted_vals = sorted(clean_values)
    median = sorted_vals[len(sorted_vals)//2]
    mode = max(
        set(sorted_vals),
        key=sorted_vals.count
    )
    print(f"\nManual Stats for {column}")
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Min:", min(sorted_vals))
    print("Max:", max(sorted_vals))



# Functional Programming
def functional_programming(df):
    mean_value = df["petal_length"].mean()
    filtered = list(
        filter(
            lambda x: x > mean_value,
            df["petal_length"]
        )
    )
    mapped = list(
        map(
            lambda x: x * 2,
            df["petal_length"]
        )
    )
    reduced = reduce(
        lambda x, y: x * y,
        df["petal_length"][:5]
    )
    print("\nFiltered:", filtered[:5])
    print("Mapped:", mapped[:5])
    print("Reduced:", reduced)