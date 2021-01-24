import pymysql


config = {
    'host': '172.17.13.173',
    'port': 12522,
    'user': 'root',
    'password': 'Bohui@123',
    'database': 'monitor',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor,
}


class MysqlDB(object):

    def __init__(self):
        self.connection = pymysql.connect(**config)

    def select_data(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def select_count(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":
    connection = pymysql.connect(**config)
    cursor = connection.cursor()
    cursor.execute('select id, column_title_id, split_template from t_setting_task')
    result = cursor.fetchall()
    cursor.close()
