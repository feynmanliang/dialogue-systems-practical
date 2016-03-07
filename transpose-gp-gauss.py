import re

with open("gp-gauss-results.txt") as f:
    for _ in range(11): next(f)
    nu = [
            'Gaussian (p=1;l=2)',
            'Gaussian (p=1;l=3)',
            'Gaussian (p=2;l=2)',
            'Gaussian (p=2;l=3)',
            'Gaussian (p=3;l=2)',
            'Gaussian (p=3;l=3)',
            'Gaussian (p=4;l=2)',
            'Gaussian (p=4;l=3)',
            'Gaussian (p=5;l=2)',
            'Gaussian (p=5;l=3)'
            ]
    try:
        print(','.join([
            'Kernel',
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
