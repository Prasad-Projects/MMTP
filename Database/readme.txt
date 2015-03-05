MMTP Database


The table in the database has a composite primary key which comprises of src_name, dest_name, bus_routeid


The table has more than 10000 entries, hence to avoid PHP timeout and breaking of transactions, entries have been divided in five files


To import 
1) Create a database 
2) Start by importing buses1.sql, buses2.sql till buses5.sql in order
3) For flight data just import the airline.sql 






