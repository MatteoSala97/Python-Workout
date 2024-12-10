number_of_runs = 0
while True:
    run_timing = input("How long did you take to run your daily 10km? \n") 
    
    if not run_timing:
        break
    
    try:
        time = int(run_timing)
        print(f"Recorded time: {time} minutes.")
        number_of_runs += 1
        print(f"Number of runs: {number_of_runs}")
    except ValueError:
        print("Please use numbers only.")
        
x = time / number_of_runs

print(f"You averaged a total of {x} minutes per run. Well done!")