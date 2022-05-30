import keras.activations
import keras
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
import random,hashlib
import keras.losses
from sklearn.preprocessing import LabelEncoder
from flask import Flask,request,render_template,redirect,url_for
app=Flask('__app__')
data=pd.read_excel('Data.xlsx')
dat=[]
alpha='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
peddaalpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}":<>?.,/+*/'
r=random.choice(alpha)
r1=random.choice(num)
r2=random.choice(peddaalpha)
string1=f"{r}{r1}{r2}".encode()
sha1=hashlib.sha1(string1).hexdigest()
strings=hashlib.sha384('srh'.encode()).hexdigest()
print(strings)
@app.route('/',methods=["GET","POST"])
def mains():
    if request.method=="POST":
        a=request.form["email"]
        if a=="sripadkarthik@gmail.com":
            alpha='abcdefghijklmnopqrstuvwxyz'
            num='0123456789'
            peddaalpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            splchar='!@#~$%^&*()_+=:;"<,>.?/*'
            firstone=random.choice(alpha)
            sec=random.choice(num)
            thir=random.choice(peddaalpha)
            fourth=random.choice(splchar)
            final=f'{firstone}{sec}{thir}{fourth}'.encode()
            global md5
            md5=hashlib.md5(final).hexdigest()
            return redirect(url_for('pasd'))
    return render_template('hectic.html')
@app.route('/pasd',methods=["GET","POST"])
def pasd():
    if request.method=="POST":
        a=request.form["password"]
        if a == md5:
            return redirect(url_for('home'))
    return render_template('paswd.html',shai=sha1)
@app.route('/home')
def home():
    return render_template('first.html')
@app.route(f'/{sha1}')
def passwd():
    return md5
@app.route(f"/{strings}",methods=['GET','POST'])
def house():
    if request.method=="POST":
        a1=request.form['jb_inv']
        a2=request.form['feedback']
        a3=request.form['experience']
        a4=request.form['tick_solving_mgmt']
        a5=request.form['delivery']
        a6=request.form['env_satis']
        a7=request.form['psyco']
        a8=request.form['train_time']
        a9=request.form['working_hrs']
        a10=request.form['js']
        a11=request.form['project_completion']
        at_1 = float(a1)
        at_2 = float(a2)
        at_3 = float(a3)
        at_4 = float(a4)
        at_5 = float(a5)
        at_6 = float(a6)
        at_7 = float(a7)
        at_8 = float(a8)
        at_9 = float(a9)
        at_10 = float(a10)
        at_11 = float(a11)
        import sqlite3
        connection = sqlite3.connect('analyses.db')
        cursor = connection.cursor()
        a = cursor.execute('select * from performances').fetchmany(5044)
        import pandas as pd
        columns = ['EmpID', 'age', 'gender', 'Department', 'environment_satisfaction', 'JobInvolvement', 'Job_Level',
                   'JobSatisfaction', 'Experience', 'TrainingTime', 'WorkLifeBalance', 'Behaviour', 'delivery',
                   'feedbacks',
                   'ticket', 'project', 'income', 'work_hrs', 'wfh', 'social', 'overtime', 'attendance', 'corona',
                   'percent_salary', 'performance']
        data = pd.DataFrame(a, columns=columns)
        print(data.columns)
        data['performance'] = data['performance'].fillna(data['performance'].mean())
        data['percent_salary'] = data['percent_salary'].fillna(data['percent_salary'].mean())
        data['corona'] = data['corona'].fillna(data['corona'].mean())
        data['attendance'] = data['attendance'].fillna(data['attendance'].mean())
        data['overtime'] = data['overtime'].fillna(data['overtime'].mean())
        data['feedbacks'] = data['feedbacks'].fillna(data['feedbacks'].median())
        data['social'] = data['social'].fillna(data['social'].mean())
        data['wfh'] = data['wfh'].fillna(data['wfh'].mean())
        data['work_hrs'] = data['work_hrs'].fillna(data['work_hrs'].mean())
        data['income'] = data['income'].fillna(data['income'].mean())
        data['project'] = data['project'].fillna(data['project'].mean())
        data['ticket'] = data['ticket'].fillna(data['ticket'].mean())
        data['Behaviour'] = data['Behaviour'].fillna(data['Behaviour'].mean())
        data['WorkLifeBalance'] = data['WorkLifeBalance'].fillna(data['WorkLifeBalance'].mean())
        data['TrainingTime'] = data['TrainingTime'].fillna(data['TrainingTime'].mean())
        data['Experience'] = data['Experience'].fillna(data['Experience'].mean())
        data['JobSatisfaction'] = data['JobSatisfaction'].fillna(data['JobSatisfaction'].mean())
        data['Job_Level'] = data['Job_Level'].fillna(data['Job_Level'].mean())
        data['JobInvolvement'] = data['JobInvolvement'].fillna(data['JobInvolvement'].mean())
        data['environment_satisfaction'] = data['environment_satisfaction'].fillna(
            data['environment_satisfaction'].mean())
        data['Department'] = data['Department'].fillna(data['Department'].mean())
        data['delivery'] = data['delivery'].fillna(data['delivery'].mean())
        y = data['performance']
        x = data[['JobInvolvement','feedbacks','Experience','ticket','delivery','environment_satisfaction','social','TrainingTime','JobSatisfaction','work_hrs','project']]
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x, y)
        model = Sequential()
        model.add(Dense(input_dim=data[['JobInvolvement','feedbacks','Experience','ticket','delivery','environment_satisfaction','social','TrainingTime','work_hrs','JobSatisfaction','project']].shape[1], units=x_train.shape[1], activation=keras.activations.relu))
        model.add(Dense(input_dim=data[['JobInvolvement','feedbacks','Experience','ticket','delivery','environment_satisfaction','social','TrainingTime','work_hrs','JobSatisfaction','project']].shape[1], units=x_train.shape[1], activation=keras.activations.relu))
        model.add(Dense(input_dim=data[['JobInvolvement','feedbacks','Experience','ticket','delivery','environment_satisfaction','social','TrainingTime','work_hrs','JobSatisfaction','project']].shape[1], units=x_train.shape[1], activation=keras.activations.relu))
        model.add(Dense(units=1, activation=keras.activations.relu))
        model.compile(optimizer='adam', loss=keras.losses.mean_absolute_error, metrics=['mae'])
        model.fit(x_train,y_train, batch_size=10, epochs=20)
        pred = model.predict([[at_1,at_2,at_3,at_4,at_5,at_6,at_7,at_8,at_9,at_10,at_11]])
        for i in pred:
            if i >7.5:
                c=f'Employee is performing at his best---score:  {i}'
                return render_template('final.html',metric=c)
            elif i >5.0 or i < 7.5:
                d=f'Employee has a satisfactory performance---score:  {i}'
                return render_template('final.html',metric=d)
            elif i > 2.5 or i< 5.0:
                g=f'Employee has a weaker performance---score:  {i} '
                return render_template('final.html',metric=g)
        return render_template('employee_performance.html',shai=sha1)
if __name__=='__main__':
    app.run()