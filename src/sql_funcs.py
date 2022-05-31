import sqlite3

def safe_insert(
    cursor: sqlite3.Cursor,
    table: str,
    data_dict: dict
) -> None:

    # execute insert query unless it is a duplicate
    cursor.execute(
    f"""
    INSERT OR IGNORE INTO {table} ({', '.join(data_dict.keys())}) 
    VALUES ({', '.join("?" for itm in data_dict)});
    """, tuple(data_dict.values()))

def safe_select(
    cursor: sqlite3.Cursor,
    table: str,
    select_dict: dict,
    num: int
) -> list:

    # execute select query
    cursor.execute(
    f"""
    SELECT * FROM {table} {f"WHERE {' AND '.join(str(i) for i in select_dict)}" if select_dict != {} else ''} LIMIT {num}
    """, tuple(select_dict.values())
    )

    # get rows
    rows = cursor.fetchall()

    return rows

def safe_update(
    cursor: sqlite3.Cursor,
    table: str,
    update_dict: dict,
    condition_dict: dict
):

    # execute update query
    cursor.execute(
    f"""
    UPDATE {table}
    SET {" AND ".join(update_dict.keys())}
    WHERE {" AND ".join(condition_dict.keys())}
    """, tuple(update_dict.values()) + tuple(condition_dict.values())
    )