import os
import sqlite3


class Database:
    def __init__(self, db_file):
        if not os.path.exists(db_file):
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()

            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            user_id INTEGER UNIQUE,
                            user_name TEXT,
                            is_admin INTEGER DEFAULT 0,
                            is_block INTEGER DEFAULT 0
                        )''')

            self.connection.commit()
        else:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def user_add(self, user_id, user_name):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `user_name`) VALUES (?, ?)",
                                       (user_id, user_name))

    def set_block(self, user_id, is_block):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `is_block` = ? WHERE `user_id` = ?", (is_block, user_id,))

    def is_block(self, user_id):
        with self.connection:
            block = self.cursor.execute("SELECT `is_block` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            if block[0][0] == 1:
                return True
            else:
                return False

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `is_block` FROM `users`").fetchall()

    def get_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)

    def is_admin(self, user_id):
        with self.connection:
            is_admin = self.cursor.execute("SELECT `is_admin` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(
                1)
            if is_admin[0][0] == 1:
                return True
            else:
                return False

    def all_admins_id(self):
        with self.connection:
            try:
                return self.cursor.execute("SELECT `user_id` from `users` WHERE `is_admin` = 1").fetchall()
            except:
                pass

    def set_admin(self, user_id, admin):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `is_admin` = ? WHERE `user_id` = ?", (admin, user_id,))


db = Database("db.sqlite")
