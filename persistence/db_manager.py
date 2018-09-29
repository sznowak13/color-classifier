from persistence.db_helper import connection_handler

@connection_handler
def add_entry(cursor, entry):
    SQL = ("INSERT INTO color_data (red, green, blue, entry_name, color_guess, session_id)"
           "VALUES (%(red)s, %(green)s, %(blue)s, %(entry_name)s, %(color_guess)s, %(session_id)s);")
    cursor.execute(SQL, {'red': entry['red'], 'green': entry['green'],
                        'blue': entry['blue'], 'entry_name': entry['entry_name'],
                        'color_guess': entry['color_guess'], 'session_id': entry['id']})