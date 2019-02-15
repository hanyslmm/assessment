# Database Task:

## 1. Which movies are supplied by "Joe's House of Video" or "Video Warehouse"?

### first create view movie_name

CREATE view movie_name as\
SELECT SupplierID, MovieName\
FROM MovieSupplier join Movies\
ON MovieSupplier.MovieID = Movies.MovieID;

### then join movie_name & Supplier and execute select query

SELECT MovieName\
FROM Suppliers JOIN movie_name\
ON Suppliers.SupplierID = MovieSupplier.SupplierID\
WHERE SupplierName = "Joe's House of Video"\
OR SupplierName  = "Video Warehouse";

## 2. Which movie was rented for the longest duration (by any customer)?

### first create view tap_rental

CREATE view tap_rental as\
SELECT MovieID, Duration\
FROM Inventory join Rentals\
ON Inventory.TapeID = Rentals.TapeID;

### then join tap_rental & Movies and execute select query

SELECT MovieName\
FROM Movies join tap_rental\
ON Movies.MovieID = tap_rental.MovieID\
ORDER BY Duration\
DESC\
LIMIT 1;


 
