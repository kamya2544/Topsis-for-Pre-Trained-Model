# TOPSIS Implementation for Pre-Trained Model Selection
## Overview:-
This repository contains a Python implementation of the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). It helps in selecting the best alternative (e.g., pre-trained models) based on multiple criteria, such as BLEU score, latency, and perplexity.

## Working:-
Step 1: Normalization: The decision matrix is normalized to scale the criteria to comparable units. <br>
Step 2: Weighted Matrix: The normalized matrix is multiplied by weights (importance) to account for the relative importance of each criteria. <br>
Step 3: Ideal and Negative-Ideal Solutions: The best (ideal) and worst (negative-ideal) values for each criterion are determined based on whether they are gain (+) or loss (-). <br>
Step 4: Distance Calculation: The Euclidean distance of each alternative is calculated from the ideal and negative-ideal solutions. <br>
Step 5: TOPSIS Score and Ranking: The relative closeness of each alternative to the ideal solution is computed, and alternatives are ranked accordingly.

## Input Data Description:-
| Criteria      | Description                      | Type (Gain/Loss)| Weight |
| ------------- | -------------                    | ------          | ----   |
| BLEU Score    | Measures model performance       | Gain(+)         | 0.3    |
| Latency(ms)   | Measures processing speed        | Loss(-)         | 0.2    |
| Perplexity    | Measures prediction uncertainty  | Loss(-)         | 0.4    |

## Example Input:-
| Model      | BLEU Score | Latency(ms)| Perplexity |
| -----------| -----------| ------     | ----       |
| Model 1    | 0.85       | 70         | 4          |
| Model 2    | 0.67       | 30         | 6          |
| Model 3    | 0.70       | 45         | 3          |

## Output:-
The analysis demonstrated clear rankings of the models based on their closeness scores, with Model 1 being the most preferred due to its higher BLEU score and lower latency and perplexity. The visualizations further highlighted how the models compare across criteria and their overall performance.

Rankings: [1 2 3] <br>
Closeness/Topsis Score: [0.56021227 0.49703687 0.45328415]

## Graphical Visualization:-
![image](https://github.com/user-attachments/assets/31ebab29-ca92-41cf-9722-58e6cbd4e6cb)


## Conclusion:-
In this implementation, we applied TOPSIS to evaluate and rank pre-trained models for text generation based on criteria such as BLEU score (performance), latency (speed), and perplexity (prediction uncertainty). TOPSIS is a versatile and effective decision-making tool, especially for evaluating machine learning models or other systems with multiple performance criteria. This approach not only simplifies complex decisions but also ensures transparency and objectivity in ranking alternatives.
