import os
import random
import csv
from datetime import datetime, timedelta

from faker import Faker

fake = Faker(locale='en-GB')


col_names = ["client", "gender", "age", "hours_slept", "sleep_quality", "main_food_taken", "food_taken_amount", "drink",
             "temperature(deg)", "exercise", "medication", "breakfast_time", "lunch_time", "supper_time", 
             "visit_restroom", "times_visited", "avg_relieve_time(min)", "soiled"]

food = ["Fruits", "Veggies", "Meat", "Chapati", "Ugali", "Rice", "Snacks"]
drinks = ["Tea", "Porridge", "Coffee", "Soft drink", "Water", "Milk"]

def generate_data(rows: int, columns: list = col_names):
    data = []
    
    for i in range(rows):
        client = str(fake.name()).split()[1]
        gender = random.choice(["Male", "Female"])
        age = round(random.normalvariate(8.0, 2.0))
        hrs_slept = round(random.gauss(7.0, 1.0))
        
        if hrs_slept <= 4:
            sleep_qlt = "Fair"
        elif hrs_slept <= 6:
            sleep_qlt = "Good"
        elif hrs_slept <= 8:
            sleep_qlt = "Excellent"
        else:
            sleep_qlt = "Concerning"
            
        food_taken = fake.word(ext_word_list=food)
        food_amount = random.choice(["Heavy", "Normal", "Small"])
        drink = fake.word(ext_word_list=drinks)
        temp = round(random.normalvariate(20.5, 3.54), 1)
        exercise = random.choice(["Yes", "No"])
        medication = random.choice(["Yes", "No"])
        breakfast_time = random_time(datetime.strptime('08:00:00', '%H:%M:%S'),
                                   datetime.strptime('10:00:00', '%H:%M:%S'))
        lunch_time = random_time(datetime.strptime('12:30:00', '%H:%M:%S'), 
                            datetime.strptime('14:00:00', '%H:%M:%S'))
        supper_time = random_time(datetime.strptime('18:00:00', '%H:%M:%S'), 
                               datetime.strptime('20:00:00', '%H:%M:%S'))
        restroom = random.choice(["Yes", "No"])
        if restroom == "No":
            restroom_times = 0
        else:
            restroom_times = round(random.normalvariate(3.0, 1.0))
            while restroom_times <= 0:
                restroom_times = random.randint(1, 5)

        relieve_time = round(random.normalvariate(20.0, 2.0))
        soiled = random.choice(["Yes", "No"])
        
        row_data = [client, gender, age, hrs_slept, sleep_qlt, 
                    food_taken, food_amount, drink, temp, exercise, medication, 
                    breakfast_time.strftime('%H:%M'), 
                    lunch_time.strftime('%H:%M'),
                    supper_time.strftime('%H:%M'), 
                    restroom, restroom_times, relieve_time, soiled]
        
        data.append(row_data)
        
    return columns, data

def random_time(start_time: datetime, end_time: datetime):
    time_delta = end_time - start_time
    random_seconds = random.randint(0, time_delta.total_seconds())
    
    return start_time + timedelta(seconds=random_seconds)

def save_csv(rows: int, columns: list):
    current = os.path.dirname(os.path.realpath(__name__))
    datasets = os.path.join(current, "datasets")
    if not os.path.exists(datasets):
        os.makedirs(datasets)
        
    file_path = os.path.join(datasets, "soiling.csv")
    
    column_names, sample = generate_data(rows, columns)
    
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        
        writer.writerow(column_names)
        writer.writerows(sample)
        
    print("Generated data saved to", file_path)


if __name__ == "__main__":    
    samples = 28532
    columns = col_names
    save_csv(samples, columns)
