import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model =load('rfrdone.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[str(x) for x in request.form.values()]]
    for i in range(8):
        a=['andere','bus','cabrio','coupe','kleinwagen','kombi','limousine','suv']
        if(x_test[0][0]==a[i]):
            x_test[0][0]=i
    for i in range(7):
        b=['andere','benzin','cng','diesel','elektro','hybrid','lpg']
        if(x_test[0][7]==b[i]):
            x_test[0][7]=i     
    for i in range(2):
        c=['yes','no']
        if(x_test[0][9]==c[i]):
            x_test[0][9]=i
    for i in range(2):
        d=['automatik','manuell']
        if(x_test[0][2]==d[i]):
            x_test[0][2]=i
    for i in range(40):
        e=['hyundai','audi','bmw','chevrolet','trabant','lancia','dacia','chrysler','daihatsu','citroen','ford','seat','smart','saab','jeep',
           'volvo','lada','kia','rover','mazda','mercedes_benz','fiat','subaru','nissan','honda','peugeot','suzuki','renault','jaguar','daewoo','opel',
           'skoda','mini','porsche','sonstige_autos','mitsubishi','toyota','land_rover','volkswagen','alfa_romeo']
        if(x_test[0][8]==e[i]):
            x_test[0][8]=i
    for i in range(251):
        f=['147', 'aveo', '7er', 'c_klasse', 'clk', 'galaxy', 'kangoo', '145', '2_reihe', 'tigra', 'c_max',
           '3er', 'kaefer', 'agila', '6_reihe', 'a_klasse', '850', 'berlingo', 'yeti', 'omega', 'slk',
           'lodgy', 'ypsilon', 'note', '9000', 'superb', 'xc_reihe', 'logan', 'eos', 'escort', 'cuore',
           'focus', '1er', 'polo', 'juke', 'justy', 'kalos', 'touran', 'altea', 'amarok', '5er',
           'antara', 'scirocco', 'fortwo', 'legacy', 'c3', 'delta', 'yaris', 'corsa', '200', '6er',
           'cordoba', 'fusion', 'corolla', 'bravo', 'modus', 'pajero', 'a2', 'm_klasse', 'v_klasse', 'astra',
           'andere', 'v50', 'megane', 'calibra', 'captiva', 'transit', 'cc', 'mx_reihe', 'aygo', 'sharan',
           'golf', 'grand', 'fabia', '3_reihe', 'passat', 'navara', 'ka', 'twingo', 'meriva', 'arosa', 'c4',
           'civic', 'transporter', 'punto', 'e_klasse', 'clio', 'kadett', 'one', 'b_klasse', 'signum', 'a8',
           'jetta', 'fiesta', 'micra', 'vito', 'sprinter', '156', 'forester', 'scenic', 'a4', 'a1', 'insignia',
           'combo', 'tt', 'a6', 'jazz', '80', 'glk', '100', 'z_reihe', 'sportage', 'sorento', 'v40', 'ibiza',
           'mustang', 'getz', 'a3', 'almera', 'lupo', 'r19', 'zafira', 'caddy', 'mondeo', 'colt', 'impreza',
           'vectra', 'tiguan', 'i_reihe', 'espace', 'panda', 'up', 'seicento', 'ceed', '5_reihe', 'octavia',
           'mii', 'rx_reihe', 'fox', 'matiz', 'beetle', 'c1', 'rio', 'touareg', 'spider', 's_max', 'x_reihe',
           'a5', 'viano', 's_klasse', '1_reihe', 'avensis', 'sl', 'roomster', 'q5', 'santa', 'cooper', 'leon',
           '4_reihe', '500', 'laguna', 'ptcruiser', 'primera', 'exeo', '159', 'qashqai', 'carisma', 'accord',
           'lanos', 'phaeton', 'boxster', 'verso', 'swift', 'rav', 'kuga', 'picanto', 'stilo', 'alhambra', '911',
           'm_reihe', 'roadster', 'cayenne', 'galant', '90', 'sirion', 'crossfire', 'duster', 'cr_reihe', 'discovery',
           'c_reihe', 'c5', 'carnival', 'bora', 'forfour', 'cl', '300c', 'q3', 'spark', 'v70', 'x_type', 'ducato',
           's_type', 'x_trail', 'toledo', 'voyager', 'range_rover', 'tucson', 'q7', 'citigo', 'jimny', 'cx_reihe',
           'wrangler', 'lybra', 'range_rover_sport', 'lancer', 'freelander', 'c2', 'range_rover_evoque', 'sandero',
           '900', 'defender', 'cherokee', 'clubman', 'samara', '601', 'auris', 'niva', 's60', 'nubira', 'vivaro',
           'g_klasse', 'serie_2', 'charade', 'croma', 'outlander', 'gl', 'doblo', 'musa', 'move', 'v60', 'b_max',
           'terios', 'rangerover', 'materia', 'kalina', 'elefantino', 'i3', 'kappa', 'serie_3', 'serie_1', 'discovery_sport']
        if(x_test[0][4]==f[i]):
            x_test[0][4]=i
            


        
    x_test[0][1]=int(x_test[0][1])   
    x_test[0][3]=int(x_test[0][3])       
    x_test[0][5]=int(x_test[0][5])    
    x_test[0][6]=int(x_test[0][6])        
        
     
       

    print(x_test)
    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('index.html', prediction_text='Price Predicted: {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)
