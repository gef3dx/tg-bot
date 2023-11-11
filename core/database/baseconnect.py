import sqlite3


class Database:
    def __init__(self, db_file):
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

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `user_id` = ?", (active, user_id,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `users`").fetchall()

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
            return self.cursor.execute("SELECT `user_id` from `users` WHERE `is_admin` = 1").fetchall()

    def add_admin(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `is_admin` = 1 WHERE `user_id` = ?", (user_id,))

    def remove_admin(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `is_admin` = 0 WHERE `user_id` = ?", (user_id,))
