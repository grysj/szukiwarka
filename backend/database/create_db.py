import sqlite3
import json
from tqdm import tqdm


def db_init():
    con = sqlite3.connect("database/sites.db")

    cur = con.cursor()

    cur.execute('''
    CREATE TABLE links (
        idx INTEGER PRIMARY KEY AUTOINCREMENT,  
        link TEXT,                              
        title TEXT                             
    )
    ''')



    pbar = tqdm(total=20_000, desc="Creating DB")
    with open("crawled.jsonl", 'r', encoding='utf-8') as file:
        for line in file:
            jsonData = json.loads(line.strip())
            cur.execute("INSERT INTO links (link, title) VALUES (?, ?)", (jsonData['link'], jsonData['title']))
            con.commit()
            pbar.update(1)
    con.commit()
    con.close()