-- Import the given data dump then list all shows contain in that database that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
