import json

def print_scores(input_file):
    scores = {}

    with open(input_file) as infile:
        data = json.load(infile)
        for subject, score_data in data.items():
            scores.setdefault(subject, [])
            for key, value in score_data.items():
                if key == 'max':
                    scores[subject].append(value)

    for subject, subject_scores in scores.items():
        min_score = min(subject_scores)
        max_score = max(subject_scores)
        average_score = sum(subject_scores) / len(subject_scores)

        print(subject)
        print(f'\tmin {min_score}')
        print(f'\tmax {max_score}')
        print(f'\taverage {average_score}')

# Percorsi ai file
p1 = r'C:\Users\matteo.sala\Documents\Python Workout\23-json\9a.json'
p2 = r'C:\Users\matteo.sala\Documents\Python Workout\23-json\9b.json'


print("Scores for p1:")
print_scores(p1)
print("\nScores for p2:")
print_scores(p2)