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

**H-statistic**

One way to estimate the interaction strength is to measure how much of the variation of the prediction depends on the interaction of the features.

It is possible to measure two cases:

1. First, a two-way interaction measure that tells us whether and to what extend two features in the model interact with each other; 
2. second, a total interaction measure that tells us whether and to what extend a feature interacts in the model with all the other features.

In theory, arbitrary interactions between any number of features can be measured, but these two are the most interesting cases.

**Characteristics**

* The interaction H-statistic takes a long time to compute, because it is computationally expensive.

**Packages and Modules**

The R package iml, which is available on CRAN and on Github. There are other implementations as the R package 'pre' that implements RuleFit and H-statistic. The R package **gbm implements gradient boosted models and H-statistic**.


**Alternatives:** N-Way ANOVA, Variable Interaction Networks (VIN) 

**GLOBAL SURROGATE MODELS**

**Packages and Modules**

I used the iml R package for the examples.

**Local Surrogate (LIME)**

**Scoped Rules (Anchors)**

**Shapley Values**

**Example-Based Explanations**