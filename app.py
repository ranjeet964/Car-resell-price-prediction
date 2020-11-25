from flask import Flask, render_template, redirect,request
from wtforms import SelectField, IntegerField, FloatField, StringField, Form
import pickle

app = Flask(__name__)


company_choices = ['Maruti', 'Hyundai', 'Honda', 'Audi', 'Nissan', 'Toyota','Volkswagen', 'Land', 'Mitsubishi', 'Renault', 'Mercedes-Benz','BMW', 'Mahindra', 'Tata', 'Porsche', 'Ford', 'Jaguar', 'Volvo','Chevrolet', 'Skoda', 'Datsun', 'Mini', 'Fiat', 'Jeep','Ambassador', 'Isuzu', 'ISUZU', 'Force']

location_choices = ['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur','Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad']

year_choices = [x for x in range(2000, 2020)]

fuel_type_choices = ['CNG', 'Diesel', 'Petrol', 'LPG']

transm_choices = ['Manual', 'Automatic']

owner_type_choices = [1, 2, 3, 4]

seats_choices = [2, 4, 5, 6, 7, 8, 9, 10]

def convert_var(company, location, transm, fuel_type):
	Company_Audi = 0
	Company_BMW = 0
	Company_Chevrolet = 0 
	Company_Datsun = 0 
	Company_Fiat = 0 
	Company_Force = 0
	Company_Ford = 0
	Company_Honda = 0 
	Company_Hyundai=0
	Company_ISUZU=0
	Company_Isuzu=0 
	Company_Jaguar=0 
	Company_Jeep=0 
	Company_Land=0
	Company_Mahindra=0
	Company_Maruti=0
	Company_Mercedes_Benz=0
	Company_Mini=0
	Company_Mitsubishi=0
	Company_Nissan=0
	Company_Porsche=0
	Company_Renault=0
	Company_Skoda=0
	Company_Tata=0
	Company_Toyota=0
	Company_Volkswagen=0
	Company_Volvo=0
	Location_Bangalore=0
	Location_Chennai=0
	Location_Coimbatore=0
	Location_Delhi=0
	Location_Hyderabad=0
	Location_Jaipur=0
	Location_Kochi=0
	Location_Kolkata=0
	Location_Mumbai=0
	Location_Pune=0
	Transmission_Manual=0
	Fuel_Type_Diesel=0
	Fuel_Type_LPG=0
	Fuel_Type_Petrol=0


	comp = ('Company_'+company)
	print(comp)
	vars()[comp] = 1
	loc = ('Location_'+location)
	vars()[loc] = 1
	fu = ('Fuel_Type_'+fuel_type)
	vars()[fu] = 1
	tran = ('Transmission_' + transm)
	vars()[tran] = 1

	return (Company_Audi ,Company_BMW , Company_Chevrolet, Company_Datsun, Company_Fiat, Company_Force, Company_Ford, Company_Honda, Company_Hyundai,Company_ISUZU, Company_Isuzu, Company_Jaguar,Company_Jeep,	Company_Land,Company_Mahindra,Company_Maruti,Company_Mercedes_Benz,Company_Mini,Company_Mitsubishi,Company_Nissan,Company_Porsche,Company_Renault,Company_Skoda,Company_Tata,Company_Toyota,Company_Volkswagen,	Company_Volvo,Location_Bangalore,Location_Chennai,Location_Coimbatore,Location_Delhi,Location_Hyderabad,Location_Jaipur,Location_Kochi,	Location_Kolkata,Location_Mumbai,Location_Pune,	Transmission_Manual,Fuel_Type_Diesel,Fuel_Type_LPG,	Fuel_Type_Petrol)


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



# form_list = [company, location, year, fuel_type, transm, owner_type, kilo_driven, power, engine, seats]

rfmodel = pickle.load(open('rfmodel.pkl','rb'))

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
		engine = form.power.data
		mileage = form.mileage.data
		seats = int(form.seats.data)

		Company_Audi ,Company_BMW , Company_Chevrolet, Company_Datsun, Company_Fiat, Company_Force, Company_Ford, Company_Honda, Company_Hyundai,    Company_ISUZU, Company_Isuzu, Company_Jaguar,Company_Jeep,	Company_Land,Company_Mahindra,Company_Maruti,Company_Mercedes_Benz,Company_Mini,Company_Mitsubishi,Company_Nissan,Company_Porsche,Company_Renault,Company_Skoda,Company_Tata,Company_Toyota,Company_Volkswagen,	Company_Volvo,Location_Bangalore,Location_Chennai,Location_Coimbatore,Location_Delhi,Location_Hyderabad,Location_Jaipur,Location_Kochi,	Location_Kolkata,Location_Mumbai,Location_Pune,	Transmission_Manual,Fuel_Type_Diesel,Fuel_Type_LPG,	Fuel_Type_Petrol = convert_var(company, location, transm, fuel_type)

		inputs = [[year, kilo_driven, owner_type, power, mileage, engine, seats, Company_Audi ,Company_BMW , Company_Chevrolet, Company_Datsun, Company_Fiat, Company_Force, Company_Ford, Company_Honda, Company_Hyundai,Company_ISUZU, Company_Isuzu, Company_Jaguar,Company_Jeep,Company_Land,Company_Mahindra,Company_Maruti,Company_Mercedes_Benz,Company_Mini,Company_Mitsubishi,Company_Nissan,Company_Porsche,Company_Renault,Company_Skoda,Company_Tata,Company_Toyota,Company_Volkswagen,Company_Volvo,Location_Bangalore,Location_Chennai,Location_Coimbatore,Location_Delhi,Location_Hyderabad,Location_Jaipur,Location_Kochi,	Location_Kolkata,Location_Mumbai,Location_Pune,	Transmission_Manual,Fuel_Type_Diesel,Fuel_Type_LPG,	Fuel_Type_Petrol]]

		value = rfmodel.predict(inputs)
		print(value)
		return render_template('final.html', value = value)
	return render_template('model.html', form=form)
if __name__ == "__main__":
	app.run(debug=True)