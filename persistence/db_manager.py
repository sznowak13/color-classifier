from persistence.db_helper import connection_handler

@connection_handler
def add_entry(cursor, entry):
    SQL = ("INSERT INTO color_data (red, green, blue, entry_name, color_guess, session_id)"
           "VALUES (%(red)s, %(green)s, %(blue)s, %(entry_name)s, %(color_guess)s, %(session_id)s) RETURNING *;")
    cursor.execute(SQL, {'red': entry['red'], 'green': entry['green'],
                        'blue': entry['blue'], 'entry_name': entry['entry_name'],
                        'color_guess': entry['color_label'], 'session_id': entry['id']})
    result = cursor.fetchone()

    return result


@connection_handler
def get_data_set(cursor):
    SQL = ("SELECT red, green, blue, color_guess from color_data;")
    cursor.execute(SQL)
    res = cursor.fetchall()

    return res