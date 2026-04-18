import matplotlib.pyplot as plt
import os

# Create graphs folder if not exists
os.makedirs("outputs/graphs", exist_ok=True)


def plot_all_graphs(df):

    # Colors for species
    colors = {
        "setosa": "red",
        "versicolor": "blue",
        "virginica": "green"
    }

    # ---------------- HISTOGRAM (IMPROVED) ----------------
    plt.figure(figsize=(8,5))

    for species in df["species"].unique():

        subset = df[df["species"] == species]

        plt.hist(
            subset["petal_length"],
            bins=12,
            alpha=0.4,
            color=colors[species],
            edgecolor="black",
            label=species
        )

    plt.title(
        "Petal Length Distribution by Species",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Petal Length")
    plt.ylabel("Frequency")

    plt.legend(title="Species")
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("outputs/graphs/histogram.png")
    plt.close()


    # ---------------- SCATTER (SPECIES-WISE) ----------------
    plt.figure(figsize=(7,5))

    for species in df["species"].unique():

        subset = df[df["species"] == species]

        plt.scatter(
            subset["petal_length"],
            subset["petal_width"],
            color=colors[species],
            s=70,
            alpha=0.7,
            label=species
        )

    plt.title(
        "Petal Length vs Petal Width (Species-wise)",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("outputs/graphs/scatter_plot.png")
    plt.close()


    # ---------------- BOXPLOT (SPECIES-WISE) ----------------
    plt.figure(figsize=(7,5))

    data = []
    labels = []

    for species in df["species"].unique():

        subset = df[df["species"] == species]

        data.append(subset["sepal_length"])
        labels.append(species)

    box = plt.boxplot(data, patch_artist=True)

    # Apply colors to boxes
    for patch, species in zip(box['boxes'], labels):
        patch.set_facecolor(colors[species])

    plt.title(
        "Sepal Length Distribution by Species",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Species")
    plt.ylabel("Sepal Length")

    plt.xticks(range(1, len(labels)+1), labels)

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig("outputs/graphs/box_plot.png")
    plt.close()


    # ---------------- BAR CHART ----------------
    plt.figure(figsize=(7,5))

    counts = df["species"].value_counts()

    counts.plot(
        kind="bar",
        color=[colors[s] for s in counts.index]
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