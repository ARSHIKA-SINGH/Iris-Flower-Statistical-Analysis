import matplotlib.pyplot as plt
import os


# Create graphs folder if not exists
os.makedirs("outputs/graphs", exist_ok=True)
def plot_all_graphs(df):

    # ---------------- HISTOGRAM ----------------
    plt.figure(figsize=(7,5))
    plt.hist(
        df["petal_length"],
        bins=12,
        color="skyblue",
        edgecolor="black"
    )

    plt.title(
        "Petal Length Distribution",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Petal Length")
    plt.ylabel("Frequency")

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("outputs/graphs/histogram.png")
    plt.close()


    # ---------------- SCATTER ----------------
    plt.figure(figsize=(7,5))

    plt.scatter(
        df["petal_length"],
        df["petal_width"],
        color="purple",
        s=70,
        alpha=0.7
    )

    plt.title(
        "Petal Length vs Petal Width",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("outputs/graphs/scatter_plot.png")
    plt.close()


    # ---------------- BOXPLOT ----------------
    plt.figure(figsize=(7,5))

    plt.boxplot(
        df["sepal_length"],
        patch_artist=True,
        boxprops=dict(facecolor="lightgreen")
    )

    plt.title(
        "Sepal Length Box Plot",
        fontsize=14,
        fontweight="bold"
    )

    plt.ylabel("Sepal Length")

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("outputs/graphs/box_plot.png")
    plt.close()


    # ---------------- BAR CHART ----------------
    plt.figure(figsize=(7,5))

    df["species"].value_counts().plot(
        kind="bar",
        color=["red", "blue", "orange"]
    )

    plt.title(
        "Species Count Comparison",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Species")
    plt.ylabel("Count")

    plt.xticks(rotation=0)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("outputs/graphs/bar_chart.png")
    plt.close()