def solution(bridge_length, weight, truck_weights):
    sec = 0
    on_the_bridge = [0] * bridge_length #FIFO
    truck_weights = truck_weights[::-1]
    while 1:
        sec += 1
        # 대기 트럭 인덱스 에러 때문에 비어있으면 값 0이라고 해버림
        next_truck = truck_weights[-1] if truck_weights != [] else 0

        if sum(on_the_bridge) + next_truck <= weight:
        #다음 트럭 올라올수 있을때
            if truck_weights == []:#마지막일때 실행
                sec += bridge_length - 1
                break
            else:
                on_the_bridge.pop(0)
                on_the_bridge.append(truck_weights.pop())
        #다음 트럭 못올라올때
        else:
            #맨앞 트럭 빠지면 올라올수 있을때
            if sum(on_the_bridge) + next_truck - on_the_bridge[0] <= weight:
                on_the_bridge.pop(0)
                on_the_bridge.append(truck_weights.pop())
            #빠져도 못올라올때
            else:
                on_the_bridge.append(0)
                on_the_bridge.pop(0)
    return sec
print(solution(2,10,[7,4,5,6]), solution(2,10,[7,4,5,6]) == 8)
print(solution(100,100,[10]), solution(100,100,[10]) == 101)
print(solution(100,100,[10]*10), solution(100,100,[10]*10) == 110)
print(solution(5,6,[1,2,3,1,2]), solution(5,6,[1,2,3,1,2]) == 12) #my test case
