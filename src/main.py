from data_loader import load_data
from analysis import (
    display_data,
    detect_outliers_manual,
    add_new_columns,
    bitwise_species,
    unique_measurements,
    manual_statistics,
    functional_programming
)

from visualization import plot_all_graphs
from report_generator import generate_report
from utils import get_random_unique

def main():
    df = load_data()
    if df is None:
        return
    display_data(df)
    outliers = detect_outliers_manual(
        df,
        "sepal_length"
    )
    print("\nOutliers:", outliers)
    df = add_new_columns(df)
    bitwise_species(df)
    unique_set = unique_measurements(df)
    print("\n10 Random Unique Tuples:")
    print(get_random_unique(unique_set))
    manual_statistics(
        df,
        "sepal_length"
    )
    functional_programming(df)
    plot_all_graphs(df)
    generate_report(df, outliers)

    print("\nProject Completed Successfully!")

if __name__ == "__main__":
    main()