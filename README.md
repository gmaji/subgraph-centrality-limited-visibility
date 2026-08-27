# Subgraph-centrality-with-limited-visibility
Python implentation for the paper "Evaluating Classical Node Centralities on Networks with Limited Topological Visibility"
# Required Python Libraries
Numpy
Pandas
Networkx
Matplotlib
Scipy
NDlib

# Network Dataset Used
All networks used for the study are available in Dataset directory. They are edge lists in csv files with format as <Source node>, <Destination Node>

# How to Run:

Run the python notebook "SubGraphCen_with_Limited_Visibility_R1.ipynb" available inside src directory. 
It has all required function definitions and Separate Main execution block for computing one results/plots at a time. Each function definition is well documented and grouped based on functional similarity.
Numerical results will be saved/exported in Results directory and All plots generated will be saved into Figures directory.

# Illustrative part of Execution Pipeline
import os
Network_Name="Physician"
csv_file = os.path.join("datasets", f"{Network_Name}_dataset.csv")
G = load_graph(csv_file)
G.remove_edges_from(nx.selfloop_edges(G))
G = get_largest_connected_component(G)
# Compute dynamic beta threshold
BETA_THRESHOLD = compute_beta_threshold(G, MU)
BETA = 2 * BETA_THRESHOLD  # Scaled beta

print(f"Computed Beta Threshold: {BETA_THRESHOLD:.6f}")
print(f"Using Beta Value: {BETA:.6f}")

# Simulate SIR model and Plot S,I,R vs time plots

centrality = compute_centrality_measures(G)

for measure in [
        "Betweenness",
        "Closeness",
        "K-Shell",
        "PageRank",
        "Eigenvector",
        "Katz",
        "VoteRank"]:

    seed = get_top_seed(centrality[measure])

    print(f"{measure} Seed = {seed}")

    avgS, avgI, avgR = simulate_Single_Seed_SIR_curve(
                            G,
                            seed,
                            BETA,
                            MU,
                            mc_runs=1000)

    plot_Single_seed_SIR_curve(
            Network_Name+"_"+measure,
            avgS,
            avgI,
            avgR,
            title=rf"{measure} Centrality ($\beta$ = {BETA:.4f}, $\mu$ = {MU}, Seed = {seed})"
    )
