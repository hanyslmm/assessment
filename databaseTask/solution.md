# Database Task:

## 1. Which movies are supplied by "Joe's House of Video" or "Video Warehouse"?

// first create view movie_name

CREATE view movie_name as

SELECT SupplierID, MovieName

FROM MovieSupplier join Movies

ON MovieSupplier.MovieID = Movies.MovieID;

// then join movie_name and Supplier and select 

SELECT MovieName 

FROM Suppliers JOIN movie_name

ON Suppliers.SupplierID = MovieSupplier.SupplierID

WHERE MovieName = "Joe's House of Video"

OR MovieName = "Video Warehouse"; 
