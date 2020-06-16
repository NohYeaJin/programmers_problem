def solution(bridge_length, weight, truck_weights):
    running = []
    num = len(truck_weights)
    total_weights = 0
    answer = 0
    i = 0
    while(truck_weights):
        print(truck_weights)
        print(running)
        print(answer)
        if(((total_weights+truck_weights[0])<=weight)and(len(running)<=bridge_length)):
           total_weights += truck_weights[0]
           running.append(truck_weights.pop(0))
        else:
            total_weights = total_weights-running[0]
            answer = answer + bridge_length + len(running) -1
            while(running):
                running.pop(0)

    answer = answer + bridge_length + len(running)
    return answer

print(solution(2,10,[7,4,5,6]))