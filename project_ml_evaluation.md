#### SER594: Machine Learning Evaluation
#### Title: “Analysis of Professional Tennis Match Statistics for Outcome Prediction”
#### Author: “Aksh Rajesh Chauhan””
#### Date: 11/25/2024

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error (MSE)

**Choice Justification:** The MSE is considered a crucial metric for regression models since the squaring of the differences between actual and predicted values penalizes large errors more than small ones, hence making huge deviations of predictions to take more importance, thus being a reliable metric that will indicate the model inaccuracies. For a better model reliability, a reduced larger prediction error will be of importance when using the model to predict the results of tennis matches.



**Interpretation:** 
* Lower MSE: Shows model performance is more accurate with smaller large error margins.
* Higher MSE: Relates to larger errors and bad prognosis. With 95% confidence level the RMSE value of 0 means the model is perfect without any prediction error.


### Metric 2
**Name:** Root Mean Squared Error (RMSE)

**Choice Justification:** RMSE is chosen for its intuitive interpretability; it represents the errors in the same units as the outcome variable. This makes it particularly useful for the analysis of predictions in real-world contexts, such as tennis statistics, where stakeholders may prefer metrics with straightforward, practical implications.


**Interpretation:** 
* Lower RMSE: Better prediction where the average error magnitude might or might not be smaller.
* Higher RMSE: Suggests worse efficiency, and higher variability from the true measurements.


### Metric 3
**Name:** R-Squared (R²)

**Choice Justification:**  It has been selected because it describes the proportion of variance in the dependent variable explained by the model, which will be very important to consider when judging the overall goodness-of-fit of the model. For this project, R² helps in answering how much of the variation in tennis match outcomes is accounted for by the model.


**Interpretation:** 
* Value close to 1: Indicates that the model explains most of the variance in the data, suggesting a good fit.
* Value close to 0: Suggests that the model does not explain much of the variance, implying poor performance.


### Metric 4
**Name:** Mean Absolute Error (MAE)

**Choice Justification:**  MAE provides a straightforward average of absolute errors, offering an intuitive and balanced measure of prediction accuracy. Unlike MSE, MAE does not amplify the impact of large deviations, making it useful for evaluating average performance in predicting tennis outcomes.

**Interpretation:** 
* Lower MAE: Disperses better accuracy, in terms of averaging the total quantity of error throughout predictions.
* Higher MAE: Suggests that the model has a higher average error as compared to what has been noticed in the previous iterations.


## Alternative Models
### Alternative 1
**Construction:** Ridge Regression (alpha = 0.1)

**Evaluation:** 
* MSE: 7,816.7324
* RMSE: 88.4123
* R²: 0.5111
* MAE: 72.1063

**Analysis:** Ridge Regression introduces slight regularization, which helps reduce overfitting. However, the model’s performance metrics are only moderately improved, with minimal gains in MSE, RMSE, and R². This suggests that the data may not require heavy regularization, as the variance is already relatively controlled.

### Alternative 2
**Construction:** Lasso Regression

**Evaluation:**
* MSE: 7,816.4065
* RMSE: 88.4104
* R²: 0.5111
* MAE: 72.1061

**Analysis:** Lasso Regression is performing in the same way as Ridge Regression with similar metrics. Minor improvements in MSE and MAE indicate that regularization is not much effective on this data set. However, the feature selection capability of Lasso may make it more useful in a high-dimensional data set.

### Alternative 3
**Construction:** K-Nearest Neighbors (k=3)

**Evaluation:**
* MSE: 6,801.3527
* RMSE: 82.4703
* R²: 0.5746
* MAE: 53.6242

**Analysis:** KNN is performing much better for k=3, showing significantly lower error metrics, with a much better R-squared value, than those of Ridge and Lasso Regression. Its smaller neighborhood size enables it to give much more localized and exact predictions. Still, the limited generalization indicates further improvement by increasing the neighborhood size.

### Alternative 4
**Construction:** K-Nearest Neighbors (k=10)

**Evaluation:**
* MSE: 5,733.5737
* RMSE: 75.7204
* R²: 0.6414
* MAE: 53.8520

**Analysis:** KNN (k=10) is the top-performing model, achieving the lowest MSE, RMSE, and MAE and the highest R². The larger neighborhood size enhances the model’s ability to generalize, reducing overfitting and producing the most reliable predictions. This balance between bias and variance makes KNN (k=10) the most suitable model for this project.

## Best Model

**Model:** K-Nearest Neighbors (k=10)

**Justification:**
KNN (k=10) emerges as the best model due to its superior performance across all evaluation metrics, including the lowest MSE and RMSE, the highest R², and the lowest MAE. Its generalization power, resulting from the larger neighborhood size (k=10), allows it to effectively balance bias and variance, making it the most robust model for this dataset.
