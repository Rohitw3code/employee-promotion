from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('model0.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

labels = {'department': {'Sales & Marketing': 0,
  'Operations': 1,
  'Technology': 2,
  'Analytics': 3,
  'R&D': 4,
  'Procurement': 5,
  'Finance': 6,
  'HR': 7,
  'Legal': 8},
 'region': {'region_7': 0,
  'region_22': 1,
  'region_19': 2,
  'region_23': 3,
  'region_26': 4,
  'region_2': 5,
  'region_20': 6,
  'region_34': 7,
  'region_1': 8,
  'region_4': 9,
  'region_29': 10,
  'region_31': 11,
  'region_15': 12,
  'region_14': 13,
  'region_11': 14,
  'region_5': 15,
  'region_28': 16,
  'region_17': 17,
  'region_13': 18,
  'region_16': 19,
  'region_25': 20,
  'region_10': 21,
  'region_27': 22,
  'region_30': 23,
  'region_12': 24,
  'region_21': 25,
  'region_32': 26,
  'region_6': 27,
  'region_33': 28,
  'region_8': 29,
  'region_24': 30,
  'region_3': 31,
  'region_9': 32,
  'region_18': 33},
 'education': {"Master's & above": 0, "Bachelor's": 1, 'Below Secondary': 2},
 'gender': {'f': 0, 'm': 1},
 'recruitment_channel': {'sourcing': 0, 'other': 1, 'referred': 2}}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data_entry', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        experience = request.form.get('exp')
        department = request.form.get('deprt')
        age = int(request.form.get('age'))
        education = request.form.get('rad-exp')
        gender = request.form.get('rad-gender')
        gender = 'm' if gender == 'on' else 'f'
        no_of_trainings = int(request.form.get('no_of_training'))
        prev_year_rating = int(request.form.get('prev_year_rating'))
        length_of_service = int(request.form.get('address'))
        avg_training_score = int(request.form.get('avg_training_score'))
        region = request.form.get('region')
        kpls_gt_80 = request.form.get('rad-kp')
        awards_won = request.form.get('rad-award')
        awards_won = 1 if awards_won == 'on' else 0 


        print(f'Full Name: {full_name}')
        print(f'Experience: {experience}')
        print(f'Department: {department}')
        print(f'Age: {age}')
        print(f'Education: {education}')
        print(f'Gender: {gender}')
        print(f'Number of Trainings: {no_of_trainings}')
        print(f'Previous Year Rating: {prev_year_rating}')
        print(f'Length of Service: {length_of_service}')
        print(f'Average Training Score: {avg_training_score}')
        print(f'Region: {region}')
        print(f'KPLS > 80: {kpls_gt_80}')
        print(f'Awards Won: {awards_won}')


        # features = [labels['department'][department],
        #             labels['region'][region],
        #             labels['gender'][gender],no_of_trainings,age,prev_year_rating,length_of_service,awards_won,avg_training_score]
        
        features = [0,
                    labels['region'][region],
                    labels['gender'][gender],no_of_trainings,age,prev_year_rating,length_of_service,awards_won,avg_training_score]

        print('Features : ',features)
        y_pred = loaded_model.predict([features])[0]
        print("Prediction ",y_pred)
        data = {}
        if y_pred == 1:
            data['bonus'] = "$300"
            data['prom'] = f"{full_name} is legel to promote"
            data['reason'] = "Becuase of his experience"
            data['perform'] = "May be higher based on persistence"
        else:
            data['bonus'] = "$0"
            data['prom'] = f"{full_name} is not legel to promote"
            data['reason'] = "Becuase of his experience"
            data['perform'] = "May be higher based on his poor work"

       # Redirect to the result page with the predicted value
        return render_template("result.html", prediction_result=y_pred,name=full_name,data=data)


    return render_template("data.html")


if __name__ == '__main__':
    app.run(debug=True)
