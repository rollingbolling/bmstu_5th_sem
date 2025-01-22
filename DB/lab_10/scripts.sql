# time series vis. (кол-во питомцев по дню рождения)
SELECT birthDate, COUNT(*) AS "Количество питомцев"
FROM pet
GROUP BY birthDate
ORDER BY birthDate;

# bar gauge vis. (кол-во питомцев по весу)
SELECT count(*), weightp FROM pet GROUP BY weightp;

# bar chart vis. (кол-во питомцев по типу клетки)
SELECT c.cageType, COUNT(*) AS "Количество питомцев"
FROM pet p
JOIN cage c ON p.roomNumber = c.id
GROUP BY c.cageType
order by c.cageType;

# pie chart vis. (кол-во питомцев по полу)
SELECT count(*), gender FROM pet GROUP BY gender;

# gauge vis. (кол-во питомцев в диапозоне веса + оценка этого веса)
SELECT 
  CASE 
    WHEN weightp < 10 THEN 'Легкий'
    WHEN weightp >= 10 AND weightp < 20 THEN 'Нормальный'
    WHEN weightp >= 20 AND weightp < 30 THEN 'Тяжелый'
    ELSE 'Очень тяжелый'
  END AS "Оценка веса", 
  COUNT(*) AS "Количество"
FROM pet
GROUP BY "Оценка веса";
