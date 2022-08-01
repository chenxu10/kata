SELECT 
    artist_id, sum(number_of_plays) as total_plays
FROM
    song
WHERE
    play_date >= current_date at time zone 'UTC' - interval '7 days'
GROUP BY
    artist_id
ORDER BY 
    totalplays DESC
LIMIT
    1
