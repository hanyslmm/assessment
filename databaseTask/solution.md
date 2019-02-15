# Database Task:

## 1. Which movies are supplied by "Joe's House of Video" or "Video Warehouse"?

### Create view movie_name

CREATE view movie_name as\
SELECT MovieSupplier.SupplierID, Movies.MovieName\
FROM MovieSupplier JOIN Movies\
ON MovieSupplier.MovieID = Movies.MovieID;

### Join movie_name & Supplier then execute select query

SELECT Movies.MovieName\
FROM Suppliers JOIN movie_name\
ON Suppliers.SupplierID = MovieSupplier.SupplierID\
WHERE SupplierName = "Joe's House of Video"\
OR SupplierName  = "Video Warehouse";

## 2. Which movie was rented for the longest duration (by any customer)?

### Create view tap_rental

CREATE view tap_rental as\
SELECT Inventory.MovieID, Rentals.Duration\
FROM Inventory JOIN Rentals\
ON Inventory.TapeID = Rentals.TapeID;

### Join tap_rental & Movies then execute select query

SELECT Movies.MovieName\
FROM Movies JOIN tap_rental\
ON Movies.MovieID = tap_rental.MovieID\
ORDER BY Duration\
DESC\
LIMIT 1;


## 3. Which suppliers supply all the movies in the inventory? (Hint: first get a list of the movie suppliers and all the movies in the inventory using the cross product. Then find out which of these tuples are invalid.)

### Create view list all movies inside inventory invent_movie

CREATE view invent_movie\
SELECT Inventroy.MovieID, Movies.MovieName\
FROM Inventory JOIN Movies\
ON Movies.MovieID = Inventory.MovieID\


### Create view list all movies supplier name movie_supp

CREATE view movie_supp\
SELECT Suppliers.SupplierName, MovieSupplier.MovieID\
FROM Suppliers JOIN MovieSupplier\
ON Suppliers.SupplierID = MovieSupplier.SupplierID\


### Create list of the movie suppliers and all the movies in the inventory using the cross product

CREATE view cross_product\
SELECT * from invent_movie CROSS JOIN movie_supp\

### Execute select query which suppliers supply all the movies

SELECT SupplierName from cross_product\
WHERE MovieID IS NOT NULL;

## 4. How many movies in the inventory does each movie supplier supply? That is, for each movie supplier, calculate the number of movies it supplies that also happen to be movie in the inventory.

### Aggregation through joining the two created views movie_supp and invent_movie

SELECT SupplierName, Count(*) AS movieCount\
FROM movie_supp JOIN invent_movie\
ON movie_supp.MovieID = invent_movie.MovieID\
GROUP BY SupplierName;


## 5. Which movies have more than 4 copies been ordered? 

### Apply where condition after join Movies with Orders

SELECT Movies.MovieName, Orders.Copies\
FROM Movies join Orders\
ON Movies.MovieID = Orders.MovieID\
WHERE Orders.Copies > 4;

