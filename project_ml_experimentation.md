#### SER594: Experimentation
#### Title: “Analysis of Professional Tennis Match Statistics for Outcome Prediction”
#### Author: “Aksh Rajesh Chauhan””
#### Date: 11/25/2024


## Explainable Records
### Record 1
**Raw Data:** 

Example match data:

* Tournament: Australian Open
* Date: 2000-01-17
* Player 1: Puerta M.
* Player 2: Agassi A.
* Winner: Agassi A.
* Rank 1: 112
* Rank 2: 1
* Score: 2-6 2-6 3-6

**Prediction Explanation:** Since, the rank assigned to Player 1 is 112 and Player 2 is assigned as 1, the proposed model predicts that Player 2 will win. This actually mirrors previous performance, in that higher ranked players do better and are able to win more often.

### Record 2
**Raw Data:** 

Example match data:

* Tournament: Australian Open
* Date: 2000-01-17
* Player 1: Alami K.
* Player 2: Manta L.
* Winner: Alami K.
* Rank 1: 35
* Rank 2: 107
* Score: 6-4 7-6 7-5

**Prediction Explanation:** Player 1 (Rank 35) defeats Player 2 (Rank 107), and according to the model the result comes out to be correct with the help of lower rank of the second player. This is a match score data which suggest that though Player1 was victorious the game was quite stiff.

## Interesting Features
### Feature A
**Feature:** Player Rank

**Justification:** Player rank is inarguably one of the most important features because it can be important for determining the victory or the defeat of the match. That is why players occupying higher ranks on the game servers usually win more often – thanks to experience, high skills, and stable probability calculations. The rank is expected to have a clear relationship with the result of the match or the game.

### Feature B
**Feature:** Match Score

**Justification:** The match score feature is useful since it indicates just how close the match was. While a straight score of 3 – 0 could mean that the player that emerged as the winner was very much superior over the rival player, a score of 3 – 2, assigns the impression of a narrow victory. It can provide insights into the strength and performance of each player.

## Experiments 
### Varying A (Player Rank)
**Prediction Trend Seen:** When varying Player Rank (Feature A), the model should predict a higher likelihood of a win for the player with a better rank. The trend should show that as the difference in rank increases in favor of one player, the likelihood of that player winning also increases.

### Varying B (Match Score)
**Prediction Trend Seen:** When varying the match score (Feature B), the model may predict a stronger result for the player who wins in straight sets (e.g., 2-0 or 3-0) compared to a player who wins with a more competitive score (e.g., 3-2). A lower score in terms of set count would indicate a more decisive win, which might impact the prediction.

### Varying A and B together
**Prediction Trend Seen:** When varying both Player Rank and Match Score together, the model might reveal an even more accurate prediction. For example, if a higher-ranked player wins decisively (e.g., 3-0), the model will likely predict their victory with higher confidence. Conversely, a lower-ranked player winning a close match (e.g., 3-2) may still yield a prediction for the underdog due to the competitive score.


### Varying A and B inversely
**Prediction Trend Seen:** If Player Rank (Feature A) and Match Score (Feature B) are varied inversely (e.g., higher-ranked player losing a close match), the prediction might be less confident, as the model struggles to balance the conflicting signals from rank and match score. The prediction could shift towards an upset in cases where the higher-ranked player loses despite a strong match score.

