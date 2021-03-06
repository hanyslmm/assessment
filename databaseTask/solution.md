# Database Task:

## 1. Which movies are supplied by "Joe's House of Video" or "Video Warehouse"?

### Create view :point_right: movie_name

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

### Create view :point_right: tap_rental

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

### Create view list all movies inside inventory :point_right: invent_movie

CREATE view invent_movie\
SELECT Inventroy.MovieID, Movies.MovieName\
FROM Inventory JOIN Movies\
ON Movies.MovieID = Inventory.MovieID;


### Create view list all movies supplier name  :point_right: movie_supp

CREATE view movie_supp\
SELECT Suppliers.SupplierName, MovieSupplier.MovieID\
FROM Suppliers JOIN MovieSupplier\
ON Suppliers.SupplierID = MovieSupplier.SupplierID;


### Create list of the movie suppliers and all the movies in the inventory :point_right: cross_product

CREATE view cross_product\
SELECT * from invent_movie CROSS JOIN movie_supp\

### Execute select query which suppliers supply all the movies

SELECT SupplierName from cross_product\
WHERE MovieID IS NOT NULL;

## 4. How many movies in the inventory does each movie supplier supply? That is, for each movie supplier, calculate the number of movies it supplies that also happen to be movie in the inventory.

### Aggregation through joining the two created views :point_right: movie_supp and :point_right: invent_movie

SELECT SupplierName, Count(*) AS movieCount\
FROM movie_supp JOIN invent_movie\
ON movie_supp.MovieID = invent_movie.MovieID\
GROUP BY SupplierName;


## 5. Which movies have more than 4 copies been ordered? 

### Apply where condition after join Movies with Orders

SELECT Movies.MovieName, Orders.Copies\
FROM Movies JOIN Orders\
ON Movies.MovieID = Orders.MovieID;
WHERE Orders.Copies > 4;

## 6. Which customers rented "Fatal Attraction 1987" or rented a movie supplied by "VWS Video"?

### CREATE view :point_right: supplier_tape list supplier name & movies name & inventory.TapeID

CREATE view supplier_tape\
SELECT Suppliers.SupplierName, Movies.MovieName, Inventory.TapeID\
FROM Suppliers JOIN MovieSupplier\
ON Suppliers.SupplierID = MovieSupplier.SupplierID\
JOIN Movies\
ON Movies.MovieID = MoviesSupplier.MovieID\
JOIN Inventory\
ON Movies.MovieID = Inventory.MovieID;

### CREATE view :point_right: customer_rental list rental details with customer name :shipit:

CREATE view customer_rental\
SELECT Rentals.TapeID, Customers.FirstName, Customers.LastName\
FROM Rentals JOIN Customers\
ON Rentals.CustomerID = Customers.CustID;

### EXECUTE the required select query through joining the two above views :shipit:

SELECT Customers.FirstName, Customers.LastName\
FROM supplier_tape JOIN customer_rental\
ON supplier_tape.TapeID = Rentals.TapeID\
WHERE MovieName = "Fatal Attraction 1987"\
OR SupplierName = "VWS Video";

## 7. For which movies are there more than 1 copy in our inventory? (Note that the TapeI in inventory is different for different copies of the same MovieID)

### INNER join between Movies and Inventory table and aggregate :shipit:

SELECT Movies.MovieName, COUNT(*) as copies\
FROM Movies JOIN Inventory\
ON Movies.MovieID = Inventroy.MovieID\
GROUP BY MovieName\
HAVING copies > 1;

## 8. Which customers rented movies for 5 days or more?

### EXECUTE the required query through joining Rentals and Customers tables :shipit:

SELECT Customers.FirstName, Customers.LastName\
FROM Rentals JOIN Customers\
ON Rentals.CustomerID = Customers.CustID\
WHERE Duration >= 5;

## 9. Which supplier has the cheapest price for the movie "Almost Angels 1962"?

### EXECUTE the required query through joining Suppliers, MovieSupplier and Movies tables :shipit:

SELECT Suppliers.SupplierName, MovieSupplier.Price\
FROM Suppliers JOIN MovieSupplier\
ON Suppliers.SupplierID = MovieSupplier.SupplierID\
JOIN Movies\
ON MovieSupplier.MovieID = Movies.MovieID\
ORDER BY MovieSupplier.Price\
ASC LIMIT 1;

## 10. Which movies aren't in the inventory?

### EXECUTE left outer join on Movies and Inventory tables :shipit:

SELECT Movies.MovieName\
FROM Movies LEFT OUTER JOIN Inventory\
ON Movies.MovieID = Inventory.MoviesID\
WHERE TapeID IS NULL;

