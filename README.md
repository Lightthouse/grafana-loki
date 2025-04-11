![logo.png](logo.png)

## Сервис для обработки логов и создания дашбордов

[Страница проекта](https://grafana.com/oss/loki/)


Сервис состоит из 3 компонентов:
- promtail: агент сбора логов
- loki: хранение логов
- grafana: отрисовка графиков/дашбордов


В папках loki-confgi, promtail-config лежат конфиги для этих компонентов, которые можно скачать на самом 
[сайте](https://grafana.com/docs/loki/latest/get-started/quick-start/), как и docker-compose файл


Существует несколько библиотек для интеграции с python. Они [предложены](https://grafana.com/docs/loki/latest/send-data/) 
grafana, но разработаны не ими:
- https://github.com/xente/loki-logger-handler
- https://github.com/RomanR-dev/python-logging-loki
- https://github.com/sourav-py/nextlog


### Старт сервиса
- создайте .env файл и заполните его
- docker compose up -d (должно появиться 3 контейнера)
- проверим, что работает loki - http://localhost:3100/ready
- проверим работу grafana - http://localhost:3000 (admin/admin)
- заходим в grafana и добавляем новый источник loki


### Пример работы с моделями из проекта kinopolka

You can explore the schema in Grafana’s query editor or by running:
```sqlite
SELECT name FROM sqlite_master WHERE type='table';
```


Show the average Kinopoisk rating (rating_kp) for movies in each genre.
Visualization: Bar chart or pie chart.
In Grafana, create a new panel, select the DjangoSQLite data source, and paste the query.
Set the panel type to Bar Chart, with genre on the X-axis and avg_rating on the Y-axis.
```sqlite
SELECT g.name AS genre, AVG(m.rating_kp) AS avg_rating
FROM lists_genre g
JOIN lists_movie_genres mg ON g.name = mg.genre_id
JOIN lists_movie m ON mg.movie_id = m.kp_id
GROUP BY g.name;
```

Display the number of movies premiered each year.
Visualization: Time series or bar chart.
Use a Time Series panel, with year as the time field and movie_count as the value.
Note: SQLite’s strftime extracts the year from the premiere datetime field.
```sqlite
SELECT strftime('%Y', premiere) AS year, COUNT(*) AS movie_count
FROM lists_movie
GROUP BY year
ORDER BY year;
```

Use a Table panel to display name and rating_kp.
```sqlite
SELECT name, rating_kp
FROM lists_movie
ORDER BY rating_kp DESC
LIMIT 10;
```

Count users notes
```sqlite
SELECT u.username, COUNT(n.id) AS note_count
FROM auth_user u
LEFT JOIN lists_note n ON u.id = n.user_id
GROUP BY u.id, u.username;
```

Count movies by genres
```sqlite
SELECT name, watch_counter
FROM lists_genre
ORDER BY watch_counter DESC;
```

Count budget
```sqlite
SELECT name, budget, fees
FROM lists_movie
WHERE budget > 0 AND fees > 0
LIMIT 20;
```
