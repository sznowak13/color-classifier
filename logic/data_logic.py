from persistence import db_manager as dh
from util import Result

def add_color_entry(entry_data):
    result = Result('success', 'Entry added successfully.', {})
    entry = dh.add_entry(entry_data)
    result.body = entry

    return result