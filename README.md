# Project: Data Modeling with Postgres
goal: what songs users are listening to?
tool requirement: Postgres database
output: create a database schema and ETL pipeline for this analysis

## Schema for Song Play Analysis

### Fact Table
- songplays - records in log data associated with song plays i.e. records with page NextSong
`songplays(songplay_id serial, start_time timestamp, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent text)`
### Dimension Tables
- users - users in the app; 
insert if duplicated then update current level: someone subscribes by paying a fee who happened to be a free user before.
`users(user_id int, first_name varchar, last_name varchar, gender varchar, level varchar)`
- songs - songs in music database
`songs(song_id varchar, title varchar, artist_id varchar, year int, duration numeric)`
- artists - artists in music database
`artists(artist_id varchar, name varchar, location text, latitude varchar null, longitude varchar null)`
-time - timestamps of records in songplays broken down into specific units
`time(start_time timestamp, hour int null, day int null, week int null, month int null, year int null, weekday int null)`

## ETL Pipeline
using pandas to process json file.
- process song file 
```
1. open file
2. select song data from dataframe, then insert into songs table
3. select artist data from dataframe, then insert into artists table
```
- process log file
```
1. open file
2. filter dataframe by NextSong action
3. select timestamp data from dataframe and convert into datatime, then insert into time table
4. select user data from dataframe, then insert into users table
5. using song title, artist name and duration to search songId and artistId from songs and artists tables
6. insert data into songplays table
```

## Test
open terminal first.
1. using Python3 execute create_table.py
2. using Python3 execute etl.py
3. open test.ipynb to show execution result

select sonplays query: `SELECT * FROM songplays LIMIT 2;`
select sonplays result:
|songplay_id|start_time|user_id|level|song_id|artist_id|session_id|location|user_agent|
|1|2018-11-30 00:22:07.796000|91|free|None|None|829|Dallas-Fort Worth-Arlington, TX|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)|
2|2018-11-30 01:08:41.796000|73|paid|None|None|1049|Tampa-St. Petersburg-Clearwater, FL|"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"|
