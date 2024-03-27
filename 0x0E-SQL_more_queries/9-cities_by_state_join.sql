--  lists all cities contained in the database hbtn_0d_usa
SELECT id, name FROM cities
join
SELECT name FROM states;

