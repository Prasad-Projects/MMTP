DROP TABLE IF EXISTS mytable;
CREATE TABLE mytable(
  src_id INTEGER(5)  
, src_name VARCHAR(25) NOT NULL
, dest_id INTEGER(5)
, dest_name VARCHAR(25) NOT NULL
, bus_routeid INTEGER(7) NOT NULL
, bus_starttime INTEGER(4)
, bus_endtime INTEGER(4)
, bus_duration INTEGER(4)
, bus_fare INTEGER(4)
, bus_rating NUMERIC(3,1)
, bus_isAc VARCHAR(5) 
, bus_isNAc VARCHAR(5)
, bus_isSlpr VARCHAR(5) 
, operator VARCHAR(1)
, available_seat VARCHAR(1)
, FIELD16 VARCHAR(1),
PRIMARY KEY (src_name, dest_name, bus_routeid)
);