-- cities of carlifornia subquery
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = 'Carlifonia' ORDER BY cities.id ASC;
