# Function to generate detailed analysis report
def generate_report(df, outliers):

    try:
        with open(
            "outputs/iris_analysis_report.txt",
            "w"
        ) as file:

            # Title
            file.write("=====================================\n")
            file.write("     IRIS FLOWER ANALYSIS REPORT\n")
            file.write("=====================================\n\n")


            # Dataset Shape
            file.write("1. DATASET OVERVIEW\n")
            file.write("----------------------\n")
            file.write(f"Total Rows    : {df.shape[0]}\n")
            file.write(f"Total Columns : {df.shape[1]}\n\n")


            # Column Names
            file.write("2. COLUMN NAMES\n")
            file.write("----------------------\n")
            for column in df.columns:
                file.write(f"- {column}\n")
            file.write("\n")


            # Statistical Summary
            file.write("3. BASIC STATISTICS\n")
            file.write("----------------------\n")
            file.write(str(df.describe()))
            file.write("\n\n")


            # Outliers
            file.write("4. OUTLIER ANALYSIS\n")
            file.write("----------------------\n")
            file.write(f"Outliers Found : {len(outliers)}\n")
            file.write(f"Outlier Values : {outliers}\n\n")


            # Unique Species Count
            file.write("5. SPECIES DISTRIBUTION\n")
            file.write("----------------------\n")

            species_count = df["species"].value_counts()
            for species, count in species_count.items():
                file.write(f"{species} : {count}\n")
            file.write("\n")


            # New Columns Created
            file.write("6. GENERATED FEATURES\n")
            file.write("----------------------\n")
            file.write("- petal_area\n")
            file.write("- petal_to_sepal_ratio\n")
            file.write("- combined_score\n\n")


            # Final Summary
            file.write("7. FINAL OBSERVATION\n")
            file.write("----------------------\n")
            file.write(
                "Dataset processed successfully with "
                "statistical analysis, visualization, "
                "feature engineering, and report generation.\n"
            )


            file.write("\n=====================================\n")
            file.write("      REPORT GENERATED SUCCESSFULLY\n")
            file.write("=====================================\n")


    except Exception as e: #Eceptional: Catch any exceptions that occur during file writing
        print("Error writing report:", e)