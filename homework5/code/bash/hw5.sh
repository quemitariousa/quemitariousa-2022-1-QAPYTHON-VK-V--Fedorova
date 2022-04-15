#!/bin/bash

echo "Общее количество запросов:"
wc -l access.log
echo "________________________"
echo "Общее количество запросов по типу:"
awk '{print$6}' access.log | sort | uniq -c | sort -rn
echo "________________________"
echo "Топ 10 самых частых запросов:"
awk '{print $7}' access.log | sort | uniq -c | sort -rn | head -n 10
echo "______________________"
echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской ошибкой (4ХХ)"
awk '{print $7, $9, $10, $1}' access.log | grep -E '4.. ' | sort -rn -k3 | head -n5
echo "_______________________"
echo "Топ 5 пользователей по количеству запросов, которые завершились серверной ошибкой (5ХХ)"
awk '{print $1, $9}' access.log | grep -E '5..$' | awk '{print $1}' | sort | uniq -c | sort -rn | head -n 5
echo "___________________"
