import numpy as np

def topsis(data, weights, impacts):
    """
    Parameters:
    - data: 2D array, where each row is an alternative/model and each column is a criteria.
    - weights: List of weights for each criteria.
    - impacts: List of '+' or '-' for each criteria, indicating whether it is gain (+) or loss (-).

    Returns:
    - rankings: higher rank = better alternative
    """

    data = np.array(data)
    weights = np.array(weights)

    # Normalizing the decision matrix
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    # Applying weights/importance to the normalized matrix
    weighted_data = norm_data * weights

    # Determining the ideal and negative-ideal solutions
    ideal_solution = np.max(weighted_data * (impacts == 1), axis=0) + np.min(weighted_data * (impacts == -1), axis=0)
    negative_ideal_solution = np.min(weighted_data * (impacts == 1), axis=0) + np.max(weighted_data * (impacts == -1), axis=0)

    # Calculating the distance of each alternative from the ideal and negative-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_data - ideal_solution) ** 2).sum(axis=1))
    distance_to_negative_ideal = np.sqrt(((weighted_data - negative_ideal_solution) ** 2).sum(axis=1))

    # Calculating the relative closeness to the ideal solution i.e. Topsis Score as per formula given in class slide
    closeness = distance_to_negative_ideal / (distance_to_ideal + distance_to_negative_ideal)

    # Ranking the alternatives based on closeness (higher = better)
    rankings = closeness.argsort()[::-1] + 1  # Rank starts from 1
    return rankings, closeness


# Example
if __name__ == "__main__":
    # Example data: Rows = models, Columns = criteria
    data = [
        [0.85, 70, 2],  # Model 1: BLEU score, latency (ms), perplexity
        [0.56, 40, 9],  # Model 2
        [0.35, 35, 5],  # Model 3
    ]
    weights = [0.3, 0.2, 0.4]  # Importance of each criterion
    impacts = ['+', '-', '-']  # Gain (+) or Loss (-) criteria

    rankings, closeness_scores = topsis(data, weights, np.array(impacts) == '+')
    print("Rankings:", rankings)
    print("Closeness/Topsis Score:", closeness_scores)

""" We can modify the example data, weights, and impacts based on our specific models and evaluation criteria. """