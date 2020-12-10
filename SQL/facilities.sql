/* 
How can you produce a list of the start times for 
bookings by members named 'David Farrell'? 
*/
SELECT b.starttime
FROM cd.bookings b
	INNER JOIN cd.members m
	ON m.memid = b.memid
WHERE m.surname = 'Farrell' and m.firstname = 'David';

/* 
How can you produce a list of the start times for bookings 
for tennis courts, for the date '2012-09-21'? Return a list of 
start time and facility name pairings, ordered by the time. 
*/
SELECT b.starttime AS start, f.name
FROM cd.bookings b
	INNER JOIN cd.facilities f
	ON b.facid = f.facid
WHERE f.name LIKE 'Tennis Court%' 
	AND b.starttime BETWEEN '2012-09-21' AND '2012-09-22'
ORDER BY
	b.starttime ASC;

/* 
How can you output a list of all members who have recommended 
another member? Ensure that there are no duplicates in the list, 
and that results are ordered by (surname, firstname).
*/
SELECT DISTINCT m2.firstname, m2.surname
FROM cd.members m1
	INNER JOIN cd.members m2
	ON m2.memid = m1.recommendedby
ORDER BY m2.surname, m2.firstname;

/* 
How can you output a list of all members, including the individual 
who recommended them (if any)? Ensure that results are ordered by 
(surname, firstname).
*/
SELECT 
	mems.firstname as memfname,
	mems.surname as memsname,
	recs.firstname as recfname,
	recs.surname as recsname
FROM cd.members mems
	LEFT JOIN cd.members recs
	ON mems.recommendedby = recs.memid
ORDER BY memsname, memfname;

/* 
How can you produce a list of all members who have used a tennis 
court? Include in your output the name of the court, and the name 
of the member formatted as a single column. Ensure no duplicate data, 
and order by the member name followed by the facility name.
*/
SELECT DISTINCT
	mems.firstname || ' ' || mems.surname as member,
	fac.name as facility
FROM cd.members mems
	INNER JOIN cd.bookings b ON b.memid = mems.memid
	INNER JOIN cd.facilities fac ON fac.facid = b.facid
WHERE 
	fac.name LIKE 'Tennis Court%'
ORDER BY
	member, facility;
	