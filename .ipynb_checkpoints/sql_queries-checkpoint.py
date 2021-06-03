# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = (""" 
Create table if not exists songplays 
    (
        songplay_id serial PRIMARY KEY, 
        start_time timestamp NOT NULL, 
        user_id int NOT NULL, 
        level varchar NOT NULL, 
        song_id varchar NULL, 
        artist_id varchar NULL, 
        session_id int NOT NULL, 
        location varchar NOT NULL, 
        user_agent text NOT NULL
    )
""")

user_table_create = (""" 
Create table if not exists users 
    (
        user_id int PRIMARY KEY, 
        first_name varchar NOT NULL, 
        last_name varchar NOT NULL, 
        gender varchar NOT NULL, 
        level varchar NOT NULL
    )
""")

song_table_create = ("""
Create table if not exists songs 
    (
        song_id varchar PRIMARY KEY, 
        title varchar NOT NULL, 
        artist_id varchar NOT NULL, 
        year int NOT NULL, 
        duration numeric NOT NULL
    )
""")

artist_table_create = ("""
Create table if not exists artists 
    (
        artist_id varchar PRIMARY KEY, 
        name varchar NOT NULL, 
        location text NOT NULL, 
        latitude varchar null, 
        longitude varchar null
    )
""")

time_table_create = ("""
Create table if not exists time 
    (
        start_time timestamp PRIMARY KEY, 
        hour int NOT NULL, day int NOT NULL, 
        week int NOT NULL, 
        month int NOT NULL, 
        year int NOT NULL, 
        weekday int NOT NULL
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
Insert into songplays 
    (
        start_time, 
        user_id, 
        level, 
        song_id, 
        artist_id, 
        session_id, 
        location, 
        user_agent
    ) 
    values (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
Insert into users 
    (
        user_id, 
        first_name, 
        last_name, 
        gender, 
        level
    ) 
    values (%s,%s,%s,%s,%s) 
    ON CONFLICT (user_id) DO UPDATE SET level = %s;
""")

song_table_insert = ("""
Insert into songs 
    (
        song_id, 
        title, 
        artist_id, 
        year, 
        duration
    ) 
    values (%s,%s,%s,%s,%s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
Insert into artists 
    (
        artist_id, 
        name, 
        location, 
        latitude, 
        longitude
    ) 
    values (%s,%s,%s,%s,%s)
    ON CONFLICT (artist_id) DO UPDATE SET location = %s, latitude = %s, longitude= %s;
""")


time_table_insert = ("""
Insert into time 
    (
        start_time, 
        hour, 
        day, 
        week, 
        month, 
        year, 
        weekday
    ) 
    values (to_timestamp(%s),%s,%s,%s,%s,%s,%s)
    ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
Select song_id, songs.artist_id 
From songs 
Join artists on songs.artist_id= artists.artist_id 
Where title=%s and artists.name=%s and duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]