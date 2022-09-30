
# hw-flights

## Goals:

* EDA with flights dataset
* Experience with SQLite
* Simple and complex SQL queries

## Data

The [nycflights13](https://github.com/tidyverse/nycflights13) database is available in the
[rdata](https://github.com/ds5110/rdata/tree/main/data) repo both as a collection of CSV files 
and as a SQLite database: "mydb.sqlite".

## Assignment

### Question 1

Remove the 2 distant outliers that we identified in class from the flights table, and plot the joint histogram of
distance vs flight using a [Seaborn joint histogram](https://seaborn.pydata.org/examples/joint_histogram.html).
In one or two sentences, describe the most interesting features in the visualization.

### Question 2

The scatterplot that we created in class does not clearly show a relationship
between arrival delay and distance. Group the data by destination so that your scatterplot
more clearly demonstrates whether or not there's a relationship.
Briefly explain your conclusion.

### Question 3

The following figure is from [Chapter 13 of R for Data Science](https://r4ds.had.co.nz/relational-data.html) 
by Hadley Whickam.

<img src="figs/relational-nycflights.png" width="500">

Given that the primary key for a table in a RDBMS must be unique and that you can use multiple fields as a key,
can the grayed fields in the flights table be used as a primary key for the flights table?
Write a short python program that reads flights.csv to demonstrate your answer.

### Question 4

Get a copy of the SQLite database in the rdata directory for the course.
Write two SQL queries -- one using a JOIN and the other using WHERE -- to produce the following:

* print the carrier, tail number, month and day for each flight
* order the results by these fields (in the order specified)
* get only those flights for which the plane is a made by "AIRBUS INDUSTRIE"
* get only the first 10 flights

The two queries should produce the same results.  Include the results in your README.md.
