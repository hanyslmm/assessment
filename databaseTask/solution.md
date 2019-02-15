# Database Task:

## 1. Which movies are supplied by "Joe's House of Video" or "Video Warehouse"?

### Create view movie_name

CREATE view movie_name as\
SELECT MovieSupplier.SupplierID, Movies.MovieName\
FROM MovieSupplier join Movies\
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
FROM Inventory join Rentals\
ON Inventory.TapeID = Rentals.TapeID;

### Join tap_rental & Movies then execute select query

SELECT Movies.MovieName\
FROM Movies join tap_rental\
ON Movies.MovieID = tap_rental.MovieID\
ORDER BY Duration\
DESC\
LIMIT 1;


## 3. Which suppliers supply all the movies in the inventory? (Hint: first get a list of the movie
suppliers and all the movies in the inventory using the cross product. Then find out which of
these tuples are invalid.) 
