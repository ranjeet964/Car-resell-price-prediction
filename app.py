
from flask import Flask, render_template, redirect,request
from wtforms import SelectField, IntegerField, FloatField, StringField, Form
import pickle
import numpy as np

app = Flask(__name__)


# reading random forest randomized search cv ml model

rf_rscv = pickle.load(open('rf_rscv.pkl','rb'))

# tempm = pickle.load(open(filename,'rb'))

# loading xgboost ml model

xgboost_model = pickle.load(open('xgboost.pkl','rb'))


##########################################################################

company_choices = ['Maruti', 'Hyundai', 'Honda', 'Audi', 'Nissan', 'Toyota','Volkswagen', 'Land', 'Mitsubishi', 'Renault', 'Mercedes-Benz','BMW', 'Mahindra', 'Tata', 'Porsche', 'Ford', 'Jaguar', 'Volvo','Chevrolet', 'Skoda', 'Datsun', 'Mini', 'Fiat', 'Jeep','Ambassador', 'Isuzu', 'ISUZU', 'Force']

location_choices = ['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur','Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad']

year_choices = [x for x in range(2000, 2020)]

fuel_type_choices = ['CNG', 'Diesel', 'Petrol', 'LPG']

transm_choices = ['Manual', 'Automatic']

owner_type_choices = [1, 2, 3, 4]



def reset_dict():
	dict1 = dict.fromkeys(dict1, 0)

seats_choices = [2, 4, 5, 6, 7, 8, 9, 10]
def convert_var(company, location, transm, fuel_type):
	dict1= {'Company_Audi':0, 'Company_BMW':0,
		'Company_Chevrolet':0, 'Company_Datsun':0, 'Company_Fiat':0, 'Company_Force':0,
		'Company_Ford':0, 'Company_Honda':0, 'Company_Hyundai':0, 'Company_ISUZU':0,
		'Company_Isuzu':0, 'Company_Jaguar':0, 'Company_Jeep':0, 'Company_Land':0,
		'Company_Mahindra':0, 'Company_Maruti':0, 'Company_Mercedes-Benz':0,
		'Company_Mini':0, 'Company_Mitsubishi':0, 'Company_Nissan':0,
		'Company_Porsche':0, 'Company_Renault':0, 'Company_Skoda':0, 'Company_Tata':0,
		'Company_Toyota':0, 'Company_Volkswagen':0, 'Company_Volvo':0,
		'Location_Bangalore':0, 'Location_Chennai':0, 'Location_Coimbatore':0,
		'Location_Delhi':0, 'Location_Hyderabad':0, 'Location_Jaipur':0,
		'Location_Kochi':0, 'Location_Kolkata':0, 'Location_Mumbai':0,
		'Location_Pune':0, 'Transmission_Manual':0, 'Fuel_Type_Diesel':0,
		'Fuel_Type_LPG':0, 'Fuel_Type_Petrol':0}


	comp = "Company_"+company
	loct = "Location_"+location
	trans = "Transmission_"+transm
	fuel = "Fuel_Type_"+fuel_type
	temp_list = [comp, loct, trans, fuel]

	for i in temp_list:
		if i in dict1:
			dict1[i]=1

	
	return list(dict1.values())


class NewDataInput(Form):
	company = SelectField('Company', choices=company_choices)
	location = SelectField('Location', choices=location_choices)
	year = SelectField('Year', choices=year_choices)
	fuel_type = SelectField('Fuel Type', choices=fuel_type_choices)
	transm = SelectField('Transmission', choices=transm_choices)
	owner_type = SelectField('Owner Type', choices=owner_type_choices)
	kilo_driven = FloatField('Kilometer Driven')
	power = FloatField('Power (in bhp)')
	mileage = FloatField('Mileage')
	engine = FloatField('Engine (in CC)')
	seats = SelectField('Seats', choices=seats_choices)
	modelname = StringField('Model Name')


@app.route('/')
def index():
	return render_template('welcome.html')


@app.route('/model', methods=['GET', 'POST'])
def model():
	form = NewDataInput(request.form)
	if request.method=='POST' and form.validate():
		company = form.company.data
		location = form.location.data
		year = int(form.year.data)
		fuel_type = form.fuel_type.data
		transm = form.transm.data
		owner_type = int(form.owner_type.data)
		kilo_driven = form.kilo_driven.data
		power = form.power.data
		engine = form.engine.data
		mileage = form.mileage.data
		seats = int(form.seats.data)
		modelname = form.modelname.data

		para_list = convert_var(company, location, transm, fuel_type)
	
		inputs = [year, kilo_driven, owner_type, power, mileage, engine, seats]
		inputs = inputs + para_list

		inputs = [inputs]
		# xginp = np.array(inputs)
		# xginp = xginp.reshape(48,1)

		dis_dict = {
			'Company' : company,
			'Model' : modelname,
			'Location' : location,
			'M. Year' : year
		}

		# value_xg = xgboost_model.predict(inputs)[0]	
		value_rf = rf_rscv.predict(inputs)[0]
		# value_rf = round(value_rf, 2)
		value_max = value_rf * (1.025)
		value_min = value_rf * (0.975)
		return render_template('final.html', value_min=round(value_min, 2),value_max=round(value_max, 2) ,det=dis_dict)

	return render_template('model.html', form=form)
if __name__ == "__main__":
	app.run(debug=True)