from flask import Flask,render_template,request,jsonify,redirect,url_for
from utils import ConcreteStrength
import config
import traceback

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("concrete_strength.html")

@app.route('/predicted_strength',methods=['GET','POST'])
def predicted_strength():
    try:
        if request.method=='GET':
            data=request.args.get
            print("data:",data)
            cement=eval(data('cement'))
            slag=eval(data('slag'))
            flyash=eval(data('flyash'))
            water=eval(data('water'))
            superplasticizer=eval(data('superplasticizer'))
            coarseaggregate=eval(data('coarseaggregate'))
            fineaggregate=eval(data('fineaggregate'))
            age=eval(data('age'))
            concrete=ConcreteStrength(cement,slag,flyash,water,superplasticizer,coarseaggregate,fineaggregate,age)
            predict_strength=concrete.get_predicted_strength()

            return render_template("concrete_strength.html",prediction=predict_strength)
        else:    
            data=request.form.get
            print("data:",data)
            cement=data['cement']
            slag=data['slag']
            flyash=data['flyash']
            water=data['water']
            superplasticizer=data['superplasticizer']
            coarseaggregate=data['coarseaggregate']
            fineaggregate=data['fineaggregate']
            age=data['age']
            concrete=ConcreteStrength(cement,slag,flyash,water,superplasticizer,coarseaggregate,fineaggregate,age)
            predict_strength=concrete.get_predicted_strength()


            return render_template("concrete_strength.html",prediction=predict_strength)
    except:
        print(traceback.print_exc())
        #return redirect(url_for('/predicted_strength'))

if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)