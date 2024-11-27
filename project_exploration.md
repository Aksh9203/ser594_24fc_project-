#### SERX94: Exploratory Data Munging and Visualization
#### Title: “Analysis of Professional Tennis Match Statistics for Outcome Prediction”
#### Author: “Aksh Rajesh Chauhan””
#### Date: 10/22/2024

## Basic Questions
**Dataset Author(s):** Unknown, sourced from professional tennis match records and betting market data

**Dataset Construction Date:** The dataset contains records from professional tennis matches across multiple years, with match dates ranging from January 2000 onward.

**Dataset Record Count:** The dataset contains approximately 50,000 match records, spanning different tournament series and player profiles.

**Dataset Field Meanings:** 
* Tournament Details: Series, Date, Court Type (Indoor/Outdoor), Surface Type (Clay, Grass, etc.), Round
* Player Information: Player Names, Rankings, Points
* Match Specifics: Best of Format, Winner, Final Score
* Betting Market Data: Match Odds for both players

**Dataset File Hash(es):** TODO

## Interpretable Records
### Record 1
**Raw Data:** 

* Tournament: Australian Open
* Date: 2000-01-17
* Player 1: Puerta M.
* Player 2: Agassi A.
* Winner: Agassi A.
* Rank 1: 112
* Rank 2: 1
* Score: 2-6, 2-6, 3-6

**Interpretation:** This match demonstrates the relationship between player rank and match outcome. Player 2 (Agassi A.), ranked 1, won decisively against Player 1 (Puerta M.), ranked 112. The scoreline (2-6, 2-6, 3-6) reflects a straightforward victory, consistent with the expected trend that higher-ranked players tend to win against lower-ranked opponents.

### Record 2
**Raw Data:** 

* Tournament: Australian Open
* Date: 2000-01-17
* Player 1: Alami K.
* Player 2: Manta L.
* Winner: Alami K.
* Rank 1: 35
* Rank 2: 107
* Score: 6-4, 7-6, 7-5

**Interpretation:** This match showcases a closer contest. Despite Player 1 (Alami K.) being higher-ranked (35) than Player 2 (Manta L., ranked 107), the match was competitive, as evidenced by the score (6-4, 7-6, 7-5). The result aligns with the model’s prediction that the higher-ranked player would win, but it also suggests that rank disparity does not always guarantee a dominant performance.

## Background Domain Knowledge
Tennis is also one of the most popular sports depending on the worldwide audience and numerous competitions organize every year. ATP is the association that oversees Male professional tennis circuits, these include; ATP tour, ATP Challenger tour, and ATP Champions tour. The ATP Tour features the world's top male tennis players competing in various tournaments throughout the year, culminating in prestigious events like the Grand Slams and the ATP Finals.

* Understanding the dynamics of ATP tournaments requires knowledge of several key elements:
* Tournament Structure: The ATP tournaments series are classified according to the point system and the amount of prestige accorded to them as follows: the grand slams, the ATP world tour masters 1000, ATP world tour 500 and ATP world tour 250. Every tournament is different from another in terms of playing surface – clay, grass or hard; in terms of draw size, and the actual money at stake.

* Player Rankings: Ranking points are awarded to the players depending the performance they register in tournaments. These aspects define their global standing and thus tournament ratings as well as qualifications for entry into a tournament tier. The rank in place ensures that the players maintain high results in a number of events.

* Match Dynamics: Matches are accepted to differ in duration and contact ratio within a court by means of tennis arena, climate, and landslide strategies. For example, extended rallies would be observed – in comparison with grass courts – because clay courts are slower.

* Statistical Analysis: Using match data can enable evaluation of how players, their team or opponent, are doing, detailed statistics of how the two have fared against each other and probable result of the match to be forecasted. A need to analyze serve speed, break points won and lost together with unforced errors help in analyzing the match behavior.

Tennis analytics has become increasingly sophisticated with advancements in technology.Critical information is now a standard part of player gameplay strategy and also the way to interact with fans. For instance, players locate their adversaries’ flaws via data analysis for gameplay, or they gather data to set up ideal practice schedules. Audiences benefit from real-time statistical analysis and deterministic activity prognosis for matches.


Sources:
* "Tennis Player statistics Dataset" - 085b5d431fa81b0c723ec6c69bf004c7


## Dataset Generality
The data applied for this analysis includes an extensive selection of ATP tennis matches of the tournaments, which took place in 2005. The information could be players’ ratings, match results, coefficients, and specific details of the tournament which might be the type of surface. Included tournament levels cover International Series from one to nine, while surfaces range from clay, grass, and hard, which in a way represents actual competitive season the player is to experience.

The selection of participants also ranges between high-ranked players and the lower-ranked participants giving the aspect of varied playing styles and competitiveness. This variety enables the realization of feasible analysis across different contextual specification within professional tennis.

## Data Transformations
* Cleaning: Any rows containing missing data or any arbitrary values such as -1 were also dropped out to avoid being a source of further noise in the results. And also keep row in which column contain value like Australian Open and Wimbledon.
* Deduplication: All the same records were distinguished and excluded to reach the ideal number and have an accurate analysis of the results.
* Normalization: There are possibilities that some features may have been standardized to get a direct comparison on different scales though not mentioned in the script uploaded above.

These transformations retain the integrity of the matches’ dataset as they consistently preserve many core aspects of data while improving its quality for analyses.


## Visualizations

* Scatter Plot: Rank_1 vs Odd_1:
This scatter plot shows the relationship between the Rank_1 value and the Odd_1 value. Each data point represents a single observation, with the Rank_1 value on the x-axis and the Odd_1 value on the y-axis. The plot contains a large number of data points, indicating a substantial dataset. The data points are spread out across the plot, showing a general positive correlation between the two variables, with higher Rank_1 values associated with higher Odd_1 values.

* Scatter Plot: Rank_1 vs Odd_2:
This scatter plot is similar to the first one, but it shows the relationship between Rank_1 and Odd_2 values. Again, the data points are spread out across the plot, indicating a positive correlation between the two variables. However, the distribution of points appears to be denser in the lower-left portion of the plot, suggesting a more pronounced correlation at lower Rank_1 and Odd_2 values.

* Scatter Plot: Rank_1 vs Pts_1:
This scatter plot displays the relationship between Rank_1 and Pts_1 values. The data points are distributed in a distinctive curve-like pattern, with a steep slope at lower Rank_1 values and a more gradual slope at higher Rank_1 values. This suggests a nonlinear relationship between the two variables, where Pts_1 increases rapidly at lower Rank_1 values and then the rate of increase slows down at higher Rank_1 values.

* Scatter Plot: Rank_1 vs Pts_2:
This scatter plot is similar to the previous one, but it shows the relationship between Rank_1 and Pts_2 values. The data points display a similar curve-like pattern, indicating a nonlinear relationship between the two variables. However, the overall distribution of points appears to be more spread out compared to the Rank_1 vs Pts_1 plot, suggesting a different underlying relationship between Rank_1 and Pts_2.

* Scatter Plot: Rank_1 vs Rank_2:
This scatter plot depicts the relationship between Rank_1 and Rank_2 values. The data points are distributed across the plot, with a general positive correlation between the two variables. However, the pattern is more scattered, with a wider range of Rank_2 values for a given Rank_1 value, especially at lower Rank_1 values. This suggests a less linear relationship between the two rank variables compared to the previous plots.