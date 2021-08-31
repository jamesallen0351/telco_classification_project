# Telco Classification Project


## Project Objectives

- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.

- Create modules (acquire.py, prepare.py) that make your process repeateable.

- Construct a model to predict customer churn using classification techniques.

- Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.

- Answer panel questions about your code, process, findings and key takeaways, and model.

## Business Goals

- Find drivers for customer churn at Telco. Why are customers churning?

- Construct a ML classification model that accurately predicts customer churn.

- Document your process well enough to be presented or read like a report.

## Data Dictionary

Name | Description | Type
:---: | :---: | :---:
senior_citizen | Indicates if customer is a senior citizen | int
tenure | Months customer has subscribed to service | int
monthly_charges | Dollar cost per month | float
total_charges | Dollar cost accumulated during tenure | float
internet_extras | Indicates if customer pays for internet add-ons | int
streaming_entertainment | Indicates if customer has streaming movies or tv | int
family | Indicates if customer has dependents or partner | int
gender_Male | Indicates if customer identifies as male | int
phone_service_Yes | Indicates if customer has at least 1 phone line | int
paperless_billing_Yes | Indicates if customer uses paperless billing | int
churn_Yes | Indicates if customer has left the company | int
contract_type_Month-to-month | Indicates if customer pays on a monthly basis | int
contract_type_One_year | Indicates if customer pays annually | int
contract_type_Two_year | Indicates if customer pays bi-annually | int
internet_service_type_DSL | Indicates if customer has DSL internet | int
internet_service_type_Fiber_optic | Indicates if customer has fiber optic internet | int
internet_service_type_None | Indicates if customer does not have internet | int
payment_type_Bank_transfer | Indicates if customer pays using a bank account | int
payment_type_Credit_card | Indicates if customer pays using a credit card | int
payment_type_Electronic_check | Indicates if customer pays using e-check | int
payment_type_Mailed_check | Indicates if customer pays using paper check | int


## Project Planning Steps

1. Aquire telco data from codeup database
2. Clean and prepare the telco data
3. Analyze and explore the telco data to identify drivers of churn
4. Split the telco data into train, validate, and test
5. Run at least two different models on the telco data
6. Identify the best model to run on the test telco data
7. Put the telco data into a .csv to identify who is likely to churn
8. Conclusion and next steps


## To reproduce this project:

- You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 

- [ ] Read this README.md
- [ ] Download the aquire.py, prepare.py, and telco_final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the telco_final_report.ipynb notebook
