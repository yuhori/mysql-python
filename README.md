# mysql-python

## ローカル実行
```
USER='<user>' PASS='<pass>' <host>' DB='<db>' poetry run python3 -m mysql_python
```

### 作成された DB
```
mysql> describe users;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(200) | YES  |     | NULL    |                |
| age   | int          | YES  |     | NULL    |                |
| email | varchar(100) | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
4 rows in set (0.03 sec)
```