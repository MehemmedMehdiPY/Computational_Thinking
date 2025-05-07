from random import randint

class Coin():
    def __init__(self):
        pass

    def flip(self):
        event = randint(0, 1)
        return event
    
    def analyze_events(self, events, k):

        extreme_k = int(k * 0.4)
        events_prev = events[:k // 2]
        events_current = events[k // 2:]

        count_prev_0 = events_prev.count(0)
        count_current_0 = events_current.count(0)

        cond_prev_T = (count_prev_0 >= extreme_k)
        cond_prev_H = (count_prev_0 <= (k // 2 - extreme_k))
        
        cond_current_T = (count_current_0 >= extreme_k)
        cond_current_H = (count_current_0 <= (k // 2 - extreme_k))

        if cond_prev_H and cond_current_T:
            return "phct"
        
        if cond_prev_H and cond_current_H:
            return "phch"
        if cond_prev_T and cond_current_T:
            return "ptct"
        if cond_prev_T and cond_current_H:
            return "ptch"
        
        if cond_prev_H and not (cond_current_H or cond_current_T):
            return "phne"
        
        if cond_prev_T and not(cond_current_H or cond_current_T):
            return "ptne"
        
        return "ne"
    

coin = Coin()

k = 20

events = [coin.flip() for _ in range(k)]

report = {
    "phct": 0,
    "phch": 0,
    "phne": 0,
    "ptct": 0,
    "ptch": 0,
    "ptne": 0,
    "ne": 0
}
for _ in range(10 ** 6):
    out = coin.analyze_events(events, k=k)
    report[out] += 1

    new_events = [coin.flip() for _ in range(k // 2)]
    events = events[k // 2:] + new_events

print(report)

total = sum(report.values())
for key in report.keys():
    print("The key {} --> {}%".format(key.upper(), report[key] / total * 100))