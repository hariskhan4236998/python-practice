score = input("Enter Score: ")
score = float(score)
if score >= 0.9:
    print(f'A')
elif score >= 0.8 and score < 0.9:
    print(f'B')
elif score >= 0.7 and score < 0.8:
    print(f'C')
elif score >= 0.6 and score < 0.7:
    print(f'D')
else:
    print(f'F')