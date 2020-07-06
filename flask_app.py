from flask import Flask, request
import pymysql
import uuid

app = Flask(__name__)
SA = 'server-app-link'
UN = 'username'
PS = 'password'
DB = 'database'
UPD_P_R = "UPDATE participants SET session='%s' WHERE login='%s' AND hash='%s'"
LI_P_R = "SELECT * FROM participants WHERE login='%s' AND hash='%s'"

@app.route('/getInitValues')
def getInitValues():
    value = ""
    con = pymysql.connect(SA, UN, PS, DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM keyValues WHERE name='initValues'")
    value = cur.fetchone()[2]
    cur.close()
    con.close()
    return value

@app.route('/reloadAll')
def reloadAll():
    value = ""
    con = pymysql.connect(SA, UN, PS, DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM keyValues WHERE name='reloadAll'")
    value = cur.fetchone()[2]
    cur.close()
    con.close()
    return value

@app.route('/getRadioData')
def getRadioData():
    value = ""
    con = pymysql.connect(SA, UN, PS, DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM keyValues WHERE name='radioData'")
    value = cur.fetchone()[2]
    cur.close()
    con.close()
    return value

@app.route('/login', methods=['POST'])
def login():
    L = pymysql.escape_string(request.form['name'])
    H = pymysql.escape_string(request.form['hash']) # hashlib.sha3_256(b"pass").hexdigest()
    S = str(uuid.uuid4()).replace('-', '')
    con = pymysql.connect(SA, UN, PS, DB)
    cur = con.cursor()
    cur.execute(UPD_P_R % (S, L, H))
    cur.execute(LI_P_R % (L, H))
    data = cur.fetchone()
    if data is None:
        return "Oops! There is a problem."
    cur.close()
    con.close()
    return '{ "id": %i, "email": "%s", "name": "%s", "role": %i, "description": "%s", "active": %i, "campShift": %i, "session": "%s", "age": %i, "worksWith": "%s", "city": "%s", "uni": "%s", "profileIconUrl": "%s" }' % (data[0], data[3], data[4], data[5], data[6], int(bool(data[7])), data[8], data[9], data[10], data[11], data[12], data[13], data[14])
