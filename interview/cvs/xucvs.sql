/*
 * Converted by ned@appacademy.io from
 * http://exaples.oreilly.co/9780596007270/LearningSQLExaple.sql
 *
 * This doesn't follow all the conventions we'll learn, because we
 * didn't write it; this is a port of code provided by the Learning SQL
 * author.
*/

/* begin table creation */

create table song
(id serial,
song_id varchar(20) not null,
artist_id varchar(20) not null,
number_of_plays integer not null,
play_date date not null,
primary key (song_id, artist_id)
);

/* employee data */
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('1', '1', 12, to_date('2022-07-17', 'YYYY-MM-DD'));
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('1', '2', 32, to_date('2022-07-16', 'YYYY-MM-DD'));
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('1', '3', 30, to_date('2022-06-16', 'YYYY-MM-DD'));
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('2', '3', 30, to_date('2022-07-16', 'YYYY-MM-DD'));
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('2', '4', 30, to_date('2022-07-15', 'YYYY-MM-DD'));
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('3', '4', 30, to_date('2022-07-15', 'YYYY-MM-DD'));
insert into song (song_id, artist_id, number_of_plays, play_date)
values ('3', '6', 200, to_date('2022-05-15', 'YYYY-MM-DD'));