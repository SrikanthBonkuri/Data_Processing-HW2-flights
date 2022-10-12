
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

#### Result:

![Joint histogram of distance vs delay](https://user-images.githubusercontent.com/45035308/195239824-b4ad5c9d-bb73-47c4-81d8-9ac697dbf2c6.png)

* The removed outliers are from Hawaii and Alaska which has distance above 3000
* Most of the instances in the distribution has less arrival delay.


### Question 2

The scatterplot that we created in class does not clearly show a relationship
between arrival delay and distance. Group the data by destination so that your scatterplot
more clearly demonstrates whether or not there's a relationship.
Briefly explain your conclusion.

#### Result:

![Distance vs arrival delay grouped by dest](https://user-images.githubusercontent.com/45035308/195239848-d093d46f-c931-49f5-afa7-2cbc6931a626.png)

* A negative slope linear relation pattern is observed.
* As distance increases, average arrival delay decreases linearly.


### Question 3

The following figure is from [Chapter 13 of R for Data Science](https://r4ds.had.co.nz/relational-data.html) 
by Hadley Whickam.

<img src="figs/relational-nycflights.png" width="500">

Given that the primary key for a table in a RDBMS must be unique and that you can use multiple fields as a key,
can the grayed fields in the flights table be used as a primary key for the flights table?
Write a short python program that reads flights.csv to demonstrate your answer.

#### Result:

* Columns: ('year', 'month', 'day', 'hour', 'flight')
* Indexable rows: 333831
* Total rows: 336776
* No, the grayed columns cannot be primary key

### Question 4

Get a copy of the SQLite database in the rdata directory for the course.
Write two SQL queries -- one using a JOIN and the other using WHERE -- to produce the following:

* print the carrier, tail number, month and day for each flight
* order the results by these fields (in the order specified)
* get only those flights for which the plane is a made by "AIRBUS INDUSTRIE"
* get only the first 10 flights

The two queries should produce the same results.  Include the results in your README.md.

#### Result:
* WHERE query
   carrier tailnum  month  day
0      B6  N516JB      1    1
1      DL  N326NB      1    1
2      UA  N459UA      1    1
3      US  N807AW      1    1
4      US  N178US      1    1
5      DL  N327NW      1    1
6      DL  N318NB      1    1
7      UA  N838UA      1    1
8      UA  N841UA      1    1
9      UA  N488UA      1    1

* JOIN query
   carrier tailnum  month  day
0      B6  N516JB      1    1
1      DL  N326NB      1    1
2      UA  N459UA      1    1
3      US  N807AW      1    1
4      US  N178US      1    1
5      DL  N327NW      1    1
6      DL  N318NB      1    1
7      UA  N838UA      1    1
8      UA  N841UA      1    1
9      UA  N488UA      1    1

* Yes, both queries produce same results.
