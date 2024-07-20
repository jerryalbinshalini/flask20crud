from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='silviya'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)
@app.route('/')
def home():
    con=mysql.connection.cursor()
    sql='select * from siltable'
    con.execute(sql)
    res=con.fetchall()
    return render_template('home.html',data=res)
# .....crete new user....
@app.route('/adduser',methods=['GET','POST'])
def adduser():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        dob=request.form['dob']
        address=request.form['address']
        con=mysql.connection.cursor()
        sql="insert into siltable(name,age,dob,address) values(%s,%s,%s,%s)"
        values=[name,age,dob,address]
        con.execute(sql,values)
        mysql.connection.commit()
        con.close()
        return redirect(url_for('home'))
    return render_template('register.html')
# .......update data
@app.route('/editdata/<string:id>',methods=['GET','POST'])
def editdata(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        dob=request.form['dob']
        address=request.form['address']
        con = mysql.connection.cursor()
        sql="update ktable set name=%s,age=%s,dob=%s,address=%s where id=%s"
        values=[name,age,dob,address,id]
        con.execute(sql,values)
        mysql.connection.commit()
        con.close()
        return redirect(url_for('home'))
    sql="select * from ktable where id=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template('edit.html',data=res)
# ......Delete data.....
@app.route('/deletedata/<string:id>',methods=['GET','POST'])
def deletedata(id):
    con=mysql.connection.cursor()
    sql="delete from ktable where id=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)