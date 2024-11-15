from flask import Flask, request, render_template, redirect
import pickle

app = Flask(__name__, static_folder='static')

#importing pickle files
model = pickle.load(open('classifier.pkl','rb'))
ferti = pickle.load(open('fertilizer.pkl','rb'))
# @app.route('/signup',['GET,'POST'])
# def signup():
#     if request.method =='POST':
#         email=request.form['email']
#         password=request.form['password']
#         try:
#             user=auth.create_user(email=email,password=password)
#             flash('user created successfully!','success')
#             return redirect(url_for('login'))
#             except  Exception as e:
#                 flash (str(e),'error')
# def Home():
#     return render_template('index.html')





@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/Login', methods=['GET','POST'])
def Login():
    return render_template('login.html')

@app.route('/Signup' ,methods=['GET','POST'])
def SignUp():
    return render_template('signup.html')

@ app.route('/Model')
def Model():
    return render_template('model.html')

@ app.route('/Detail')
def Detail():
    return render_template('about.html')

@app.route('/signin',methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if None in (email, password) or not all(val.isdigit() for val in (email, password)):
        return render_template('login.html', x='Invalid input. Please provide numeric values for all fields.')
    return render_template('login.html', x=res)

@app.route('/register',methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    passwordAgain = request.form.get('passwordAgain')
    if None in (email, password) or not all(val.isdigit() for val in (email, password)):
        return render_template('signup.html', x='Invalid input. Please provide numeric values for all fields.')
# Convert values to integers
  
    
    return render_template('signup.html', x=res)

@app.route('/predict',methods=['POST'])
def predict():
    temp = request.form.get('temp')
    humi = request.form.get('humid')
    mois = request.form.get('mois')
    soil = request.form.get('soil')
    crop = request.form.get('crop')
    nitro = request.form.get('nitro')
    pota = request.form.get('pota')
    phosp = request.form.get('phos')
    if None in (temp, humi, mois, soil, crop, nitro, pota, phosp) or not all(val.isdigit() for val in (temp, humi, mois, soil, crop, nitro, pota, phosp)):
        return render_template('model.html', x='Invalid input. Please provide numeric values for all fields.')

# Convert values to integers
    input = [int(temp), int(humi), int(mois), int(soil), int(crop), int(nitro), int(pota), int(phosp)]
    res = ferti.classes_[model.predict([input])]
    return render_template('model.html', x=res)
if __name__ == "__main__":
    app.run(debug=True)