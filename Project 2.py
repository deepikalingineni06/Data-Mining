#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
 
MAX_ITERATIONS = 20
K_RANGE = range(2, 11)
OUTPUT = "For k = {} After {} iterations: SSE error = {:.4f}"

SSE = lambda X, L, C: sum(np.linalg.norm(X[i] - C[L[i]]) ** 2 for i in range(len(X)))

def plot_chart(errors):
    # Plot Sum of Squared errors [versus] K-clusters chart
    plt.plot(K_RANGE, errors, marker='x')
    plt.xlabel("'K' clusters"); plt.ylabel("Sum of Squares Error (SSE)")
    plt.title("SSE (vs) K chart")
    plt.show()

def cluster(dataset_filepath):
    # Load dataset into a numpy array
    with open(file=dataset_filepath, mode='r') as fhand:
        data = fhand.readlines()
    for i, row in enumerate(data):
        data[i] = list(map(float, row.split()))
    features = np.array(data)[:, :-1]
    # KMeans clustering of data
    errors = []
    for k in K_RANGE:
        error = 0
        for _ in range(MAX_ITERATIONS):
            kmeans = KMeans(n_clusters=k, init='random', n_init=1)
            kmeans.fit(features)
            error += SSE(features, kmeans.predict(features), kmeans.cluster_centers_)
        error_average = error / MAX_ITERATIONS
        errors.append(error_average)
        print(OUTPUT.format(k, MAX_ITERATIONS, error_average))
    return errors
     

if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) == 2:
        dataset_filepath = argv[1]
        errors = cluster(dataset_filepath)
        plot_chart(errors)
    else:
        print("[USAGE]", "$ python3 <script>.py <dataset/filepath>", sep="\n\n")
        exit(1)
