### This file reads from data.sqlite in the same folder, and iterates through the 'users' table, and creates a dictionary of id:first_name + last_name
# Then it iterates through each item in the dictionary, and searches through the "site" directory, and in each html file, it finds every instance of the userid, and replaces the uid with the corresponding username

import sqlite3
import os
import re

# Create a dictionary of user_id:username
def create_dict():
    conn = sqlite3.connect('/Users/michael/Coding_Projects/tg-jan16-mk/data.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT id, first_name || " " || last_name FROM users')
    user_dict = dict(cur.fetchall())
    conn.close()
    return user_dict

# Iterate through each item in the dictionary, and search through the "site" directory, and in each html file, find every instance of the userid, and replace the uid with the corresponding username
def uid_usr(user_dict):
    for uid, usr in user_dict.items():
        if usr == "None" or None or "Null" or "null" or "NULL" or "none" or "NONE":
            continue
        else:
            for filename in os.listdir('site'):
                if not filename.endswith('.html'):
                    continue
                else:
                    with open('site/' + filename, 'r') as f:
                        filedata = f.read()
                        filedata = re.sub(r'(?<!\w)' + str(uid) + r'(?!\w)', str(usr), filedata)
                    with open('site/' + filename, 'w') as f:
                        f.write(filedata)
                    print('Replaced ' + str(uid) + ' with ' + str(usr) + ' in ' + filename)

        print('Done')

if __name__ == '__main__':
    user_dict = create_dict()
    uid_usr(user_dict)
# This file is not used in the final version of the website, but is kept for reference
