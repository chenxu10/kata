/*
Given a table of song Ids, artist Ids, and their number of plays per day
    songId, artistIds, numberofplays, Date
    1         1              3         12
    1         5              10        13
    2         2              1         14

Find the most popular song in the past week
*/

-- SELECT songId, sum(numberofplays) as totalplays
-- FROM s
-- GROUP BY songId, Date
-- HAVING Date >= current_date at time zone 'UTC' - interval '7 days'
-- DESC 1

SELECT 
    song_id, sum(number_of_plays) as totalplays
FROM 
    song
WHERE
    play_date >= current_date at time zone 'UTC' - interval '7 days'
GROUP BY
    song_id
ORDER BY 
    totalplays DESC
LIMIT
    1
