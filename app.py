#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def jjkgkjg():
    return render_template('pen.html')
@app.route('/userinput',methods=['POST'])
def lkkl():
    if(request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        t=num1+num2
        return render_template('pen.html',water=t)
if __name__=='__main__':
    app.run()

