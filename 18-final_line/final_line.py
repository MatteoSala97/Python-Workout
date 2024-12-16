def get_final_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
        else:
            return None
        
filename = r'C:\Users\matteo.sala\Documents\Python Workout\18-final_line\example.txt'
print(get_final_line(filename))