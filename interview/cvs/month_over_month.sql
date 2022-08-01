WITH s AS (
SELECT
    song_id,
    sum(number_of_plays) as total_plays, 
    extract('MONTH' from play_date) as month_of_play   
FROM
    song
GROUP by
    song_id, month_of_play
ORDER BY
    song_id, month_of_play)


SELECT
    song_id,
    LAG(s.total_plays,1) OVER (PARTITION BY s.song_id) AS PrevMonthTotal,
    total_plays -  LAG(s.total_plays,1) OVER (PARTITION BY s.song_id) AS Delta
FROM
    s;
