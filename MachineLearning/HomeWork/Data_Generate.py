import csv
import random

def generate_student_id():
    return "2252" + str(random.randint(1000, 9999))

def generate_data():
    student_data = []
    for _ in range(500):
        student_id = generate_student_id()
        study_time = random.uniform(1, 10)  # Thời gian đi học theo ngày
        midterm_score = random.uniform(6, 10)  # Điểm giữa kì (cao)
        if study_time > 4:
            final_score = random.uniform(midterm_score, 10)  # Điểm cuối kì (cao hơn điểm giữa kì)
        else:
            final_score = random.uniform(0, midterm_score)  # Điểm cuối kì (thấp hơn điểm giữa kì)
        student_data.append([student_id, study_time, midterm_score, final_score])

    return student_data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Study Time", "Midterm Score", "Final Score"])
        writer.writerows(data)

data = generate_data()
save_to_csv(data, "student_data.csv")