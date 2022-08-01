SELECT
    song_id,
    -- LAG(s.total_plays,1) OVER (ORDER BY s.week_of_play) AS PrevWeekTotal,
    s.total_plays - LAG(s.total_plays,1) 
OVER (
    PARTITION BY song_id
    ORDER BY week_of_play) AS Delta
FROM(
SELECT 
    song_id,
    sum(number_of_plays) as total_plays, 
    extract('WEEK' from play_date) as week_of_play
FROM
    song
WHERE
    play_date > date_trunc('week', CURRENT_DATE) - interval '2 week'
GROUP BY
    song_id, week_of_play
    ) AS s;