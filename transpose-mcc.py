import re

with open("mcc-results.txt") as f:
    for _ in range(11): next(f)
    nu = [0.001, 0.005, 0.01, 0.05, 0.1]
    try:
        print(','.join([
            'Nu',
            'Iteration',
            'Reward.Mean',
            'Reward.Std',
            'Success.Mean',
            'Success.Std',
            'Turns.Mean',
            'Turns.Std'
            ]))
        nuCtr = 0
        while True:
            for _ in range(11): next(f)
            section = []
            for _ in range(7):
                line = next(f)
                section.append(line.strip())

            # transpose section
            print('\n'.join(
                map(
                    lambda x: str(nu[nuCtr]) + ',' + ','.join(list(x)),
                    list(zip(*map(
                        lambda x: re.split(r"\s+", x)[2:],
                        section))))))
            nuCtr += 1
    except StopIteration:
        pass
