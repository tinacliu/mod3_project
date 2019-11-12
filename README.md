# mod3_project



* a. Listing project members
Tina Liu, Zaria Rankine

* b. Dataset

We will be using the BreezoMeter API with hourly Air Quality reports, and the London Borough Demographics Data CSV.

https://api.breezometer.com/air-quality/v2/historical/hourly?lat=48.857456&lon=2.354611&key=YOUR_API_KEY&datetime=2019-11-07T14:00:00
https://www.kaggle.com/marshald/london-boroughs#london-borough-profiles-2016%20Data%20set.csv

* c. Goals

We look to explore air quality data for different boroughs of London, in an aim to provide insights useful to potential house buyers. Stakeholder would be house websites like Rightmove, Zoopla, as they often provide area guides for their customers being house buyers.

We define air quality using the aqi score from BreezoMeter.

Hypothesis 1:
- H0: Air quality of boroughs in Inner London = Air quality of boroughs in Outer London
- H1: Air quality of boroughs in Inner London != Air quality of boroughs in Outer London

Inner London and Outer London is as defined by the borough dataset.

Hypothesis 2:
- H0: Air quality of borough of interest 1 = Air quality of borough of interest 2
- H1: Air quality of borough of interest 1 > Air quality of borough of interest 2

Areas of interest are defined as:
Boroughs with highest and lowest Greenspace - Havering and City of London

Hypothesis 3:

H0: Air quality of borough of interest 1 = Air quality of borough of interest 2
H1: Air quality of borough of interest 1 > Air quality of borough of interest 2
Areas of interest are defined as: Boroughs with highest and lowest House Prices - 'Kensington and Chelsea' and 'Barking and Dagenham'


Note: the borough of interest will depend on the explotory data analysis results from looking at the stats info we have on the boroughs. I.e. the most expensive borough by median house price versus the most affordable borough.

* d. Responsibilities

Tina
- London borough data load and clean
- re-test calling API and refactor into functions
- Hypothesis 1


Zaria
- Initial BreezoMeter API check in Jypiter notebook
- London borough data EDA
- Hypothesis 2




* e. Summary of the files in the repository
