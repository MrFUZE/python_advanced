SELECT Customers.Name AS CustomerName, Sellers.Name AS SellerName, Orders.Amount, Orders.Date
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.ID
JOIN Sellers ON Orders.SellerID = Sellers.ID;
