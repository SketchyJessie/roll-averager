import random as r

def roll(d):
    return r.randint(1, d)
    
def random_test(d, times):
    rolls = []
    for i in range(times):
        rolls.append(roll(d))
    return rolls

def averager(data):
    return sum(data) / len(data)

def main():
    roll_data = random_test(20, 10)
    average = averager(roll_data)
    print(f"rolls: {roll_data} \naverage: {average}")
    
main()