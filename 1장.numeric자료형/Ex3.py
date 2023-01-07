def run_timing():
    run_time = 0
    run_count = 0
    while True :
        run_history = input("Enter 10 km run time :")
        if not run_history :
            break
        else :
            run_time += float(run_history)
            run_count += 1

    print(f'Average of {run_time / run_count}')

run_timing()