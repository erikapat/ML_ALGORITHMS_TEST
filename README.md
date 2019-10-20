

## List of examples:

**CLASSIFICATION**

* Binomial GLM (H2O) classification

* Deep neural network classifier (H2O)

* Dropout Additive Regression Trees Classifier

* Elastic-Net Classifier (L1 / Binomial Deviance)

* Elastic-Net Classifier (L2 / Binomial Deviance)

* Elastic-Net Classifier (mixing alpha=0.5 / Binomial Deviance). Matrix of word-grams occurrences 

* Eureqa Generalized Additive Model Classifier 

* eXtreme Gradient Boosted Trees Classifier with Early Stopping (Fast Feature Binning)

* eXtreme Gradient Boosted Trees Classifier with Early Stopping (Fast Feature Binning) and Unsupervised Learning Features

* Generalized Additive Model

* Gradient Boosted Greedy Trees Classifier with Early Stopping

* Gradient Boosted Trees Classifier

*  H2O GBM Classifier High Bias/Low Variance

* Light Gradient Boosted Trees Classifier with Early Stopping

* Light Gradient Boosting on ElasticNet Predictions

* Majority Class Classifier

* Nystroem Kernel SVM Classifier

* Nystroem Kernel SVM Classifier

* RuleFit Classifier

* Vowpal Wabbit Classifier

* Vowpal Wabbit Low Rank Quadratic Classifier

* Vowpal Wabbit Stagewise Polynomial Classifier

* CatBoost


**REGRESSION**

* Breiman and Cutler Random Forest Regressor

* Bayesian Additive Regression Trees (BART) 

* Bayesian Treed Models

**INTERPRETABLE ML**

*  **Partial Dependence Plot (PDP)**: 

A partial dependence plot can show whether the relationship between the target and a feature is linear, monotonic or more complex. It can be used with any methodology of ML, if it is applied to a linear regression model, partial plot always show a linear relationship. It shows the marginal effect of one or two features have on the predicted outcome of a machine learning model

For classification where the machine learning model outputs are probabilities, the partial dependence plot displays the probability for a certain class given different values for the features. An easy way to deal with multiple classes is to draw one line or plot per class.

It works for continous and categorical variables.

**Characteristics**

* Partial dependence plots has a causal interpretation. We intervenue on a feature and measure the changes in the predictions.

* This method works perfectly when the variables are uncorrelated between each other. The interpretation would be more complicated in the case of correlated variables. For correlated data it os better to use **Accumulated Local Effect plots or short ALE plots** that works with the **conditional** instead of the **marginal distribution**.

* The maximun number of features to study in partial dependence function is two.


**Packages and Modules**

* There are a number of R packages that implement PDPs. I used the iml package for the examples, but there is also pdp or DALEX. In Python you can use Skater.

* Alternatives to PDPs are ALE plots and ICE curves.


* **ITERACTION STRENGTH**


