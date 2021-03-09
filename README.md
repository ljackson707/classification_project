# classification_project
This is a repo for the classification project using telcom data.


# Audience

    - Your target audience for your notebook walkthrough is the Codeup Data Science team. This should guide your language and level of explanations in your walkthrough.


# Deliverables

You are expected to deliver the following:

    - a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

    - a README.md file containing the project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), key findings, recommendations, and takeaways from your project.

    - a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn)

    - individual modules, .py files, that hold your functions to acquire and prepare your data.

    - a notebook walkthrough presentation with a high-level overview of your project (5 minutes max). You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.

# (__PLAN__)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Goal 
- Find significant factors of churn within the Telco corparation.

# Script

plan 
- create script
- state my hypothesis and alt. hypothesis
- include a data dictionary

# What are we looking for? 

Problem 1:

- Is churn dependent on internet service? 

HO: There is no diffrence in churn between customers with diffrent internet services.

HA: There is a significant diffrence in churn beteen the internet services. 

Problem 2:

- Are customers with fiber optic and no online security more likly to churn?

HO: There is no diffrence in churn dependent on if the customer has online security and fiber optic.

HA: There is a significant diffrence in churn dependening on if the customer has online secur citizen and has fiber optic.


# Acquire

- create a fucntion that will acquire telco.csv
- take a look at its values (info, describe, and head)
- plot some histograms showing the distributions of         variables of intrest

# Prepare
- create acquire.py, prepare.py, and explore.py
- split data (train/validate/test)
- handle missing values in any
- encode with get_dummies any values
- if you have time (Create any new features, if you decided to make any for this project)
- get an (MVP)
    - create new feature for tenure in years
    - create single var. (dependents and partner = family)

# Explore
- run at least 2 statistical tests (2 hypothesis)
- document findings
- create visualizations (discover variable relationships)
- identify features that relate to churn(target)

# Model & Evaluate 
- You are required to establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models.

- Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.

- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.

- Feature Selection (optional): Are there any variables that seem to provide limited to no additional information? If so, remove them.

- Based on the evaluation of your models using the train and validate datasets, choose your best model that you will try with your test data, once.

- Test the final model on your out-of-sample data (the testing dataset), summarize the performance, interpret and document your results.

# Delviver
- Introduce yourself and your project goals at the very beginning of your notebook walkthrough.

- Summarize your findings at the beginning like you would for an Executive Summary. Just because you don't have a slide deck for this presentation, doesn't mean you throw out everything you learned from Storytelling.

- Walk us through the analysis you did to answer our questions and that lead to your findings. Relationships should be visualized and takeaways documented. Please clearly call out the questions and answers you are analyzing as well as offer insights and recommendations based on your findings.

        For example: If you find that month-to-month customers churn more, we won't be surprised, but Telco is not getting rid of that plan. The fact that customers churn is not because they can; it's because they can and they are motivated to do so. We want your insights into why they are motivated to do so. We realize you will not be able to do a full causal experiment, but we would like to see some solid evidence of your conclusions.

- Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.

- Remember you have a time limit of 5 minutes for your presentation. Make sure you practice your notebook walkthrough keeping this time limit in mind; it will go by very quickly.

# Data Dictionary

Knn = 

LogReg = 

Rforerst = 

Forest = 