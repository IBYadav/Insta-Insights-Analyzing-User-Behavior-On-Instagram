# -- Load the sql extention ----

# --- Load your mysql db using credentials from the "DB" area ---
%sql mysql+pymysql://bcce390e:Cab#22se@localhost/bcce390e
USE bcce390e;

SELECT id, comment_text, user_id, photo_id, created_at
FROM comments;

SELECT *
FROM users
ORDER BY created_at
LIMIT 5;

SELECT
DATE_FORMAT(created_at,'%W') AS 'day of the week',
COUNT(*) AS 'total registration'
FROM users
GROUP BY '1'
ORDER BY 'total registration' DESC;

SELECT users.username
FROM users
LEFT JOIN photos ON users.id = photos.user_id
WHERE photos.id IS NULL;

%%sql
SELECT p.id AS photo_id, COUNT(l.user_id) AS total_likes
FROM photos p
LEFT JOIN likes l ON p.id = l.photo_id
GROUP BY p.id;

%%sql
SELECT ROUND((SELECT COUNT(*)FROM photos)/(SELECT COUNT(*) FROM users),2);

%%sql
SELECT users.username,COUNT(photos.image_url)
FROM users
JOIN photos ON users.id = photos.user_id
GROUP BY users.id
ORDER BY 2 DESC;

%%sql

SELECT SUM(user_posts.total_posts_per_user)
FROM (SELECT users.username,COUNT(photos.image_url) AS total_posts_per_user
FROM users
JOIN photos ON users.id = photos.user_id
GROUP BY users.id) AS user_posts;

%%sql
SELECT COUNT(DISTINCT(users.id)) AS total_number_of_users_with_posts
FROM users
JOIN photos ON users.id = photos.user_id;

%%sql
SELECT tag_name, COUNT(tag_name) AS total
FROM tags
JOIN photo_tags ON tags.id = photo_tags.tag_id
GROUP BY tags.id
ORDER BY total DESC;

%%sql
SELECT users.id,username, COUNT(users.id) As total_likes_by_user
FROM users
JOIN likes ON users.id = likes.user_id
GROUP BY users.id
HAVING total_likes_by_user = (SELECT COUNT(*) FROM photos);

%%sql
SELECT users.username, comments.comment_text
FROM users
LEFT JOIN comments ON users.id = comments.user_id
WHERE comments.comment_text is NULL;

%%sql
SELECT tableA.total_A ,
/*100 * tableA.total_A/(SELECT COUNT(*) FROM users) AS '% Number Of Users who never commented',*/
100 * tableB.total_B/(SELECT COUNT(*) FROM users) AS '%Number of Users who like every photo',
tableB.total_B 
FROM
(SELECT 
    COUNT(TEMP1.`Number Of Users who never commented`) AS total_A

        FROM 
        (
            SELECT COUNT(*) AS `Number Of Users who never commented`
            FROM users
            LEFT JOIN comments
            ON users.id=comments.user_id
            WHERE comments.comment_text IS NULL  
            GROUP BY users.id

        )TEMP1) tableA,
(SELECT
        COUNT(TEMP2.`Number of Users who like every photo`) AS total_B
    FROM
        (
        SELECT COUNT(*) AS `Number of Users who like every photo`
        FROM users
        JOIN likes
        ON users.id = likes.user_id
        GROUP BY users.id
        HAVING COUNT(DISTINCT likes.photo_id)=(SELECT COUNT(*) FROM photos)       
        )TEMP2) tableB
        
        
%%sql
SELECT TEMP2.username, COUNT(*)
FROM
(SELECT TEMP.username, TEMP.comment_text
FROM
(SELECT users.id, users.username, comments.user_id, comments.comment_text
FROM users

LEFT JOIN comments ON users.id=comments.user_id) TEMP
HAVING comment_text IS NOT NULL) TEMP2
GROUP BY TEMP2.username

%%sql
SELECT 
    100 * SUM(CASE WHEN TEMP.comment_text is NULL THEN 1 ELSE 0 END)/COUNT(DISTINCT TEMP.id) AS `%Celebrity_count`,
    round(100 *SUM(CASE WHEN TEMP.comment_text is NULL THEN 1 ELSE 0 END)/COUNT(DISTINCT TEMP.id)) AS `Number Of Users Who Never Commented`,

    100 - 100 * SUM(CASE WHEN TEMP.comment_text is NULL THEN 1 ELSE 0 END)/COUNT(DISTINCT TEMP.id) AS `%Bot_count`,
    100- round(100 *SUM(CASE WHEN TEMP.comment_text is NULL THEN 1 ELSE 0 END)/COUNT(DISTINCT TEMP.id)) AS `Number Of Users Who Always Commented`


FROM
    (SELECT users.id, comments.comment_text
    FROM users
    LEFT JOIN comments
    ON users.id=comments.user_id)TEMP
