import random
import time
import argparse
import tqdm


def secret_santa_generate_sample(n: int) -> list[int]:
    """
    :param n: Number of people in Secret Santa event
    :return: Array where value at index i (0-based) represents number of person (0-based) who picked the person number i
    """
    sample = list(range(n))
    random.shuffle(sample)
    return sample


def verify_secret_santa_sample_somebody_picked_themselves(sample: list[int]) -> tuple[bool, int]:
    """
    :param sample: Array where value at index i (0-based) represents number of person (0-based) who picked the person number i
    :return: Tuple with two values. First is True if somebody picked themselves, False otherwise; second is number of the first person who picked themselves
    """
    for picked, picker in enumerate(sample):
        if picked == picker:
            return True, picked
    return False, -1

def calculate_secret_santa_probability_monte_carlo(n: int, iterations: int) -> float:
    """
    :param n: Number of people in Secret Santa event
    :param iterations: Number of iterations for Monte Carlo simulation
    :return: Probability that nobody picked themselves in Secret Santa event with n people
    """
    positive_events = 0
    for _ in tqdm.tqdm(range(iterations)):
    #for _ in range(iterations):
        sample = secret_santa_generate_sample(n)
        is_positive, themselves_picker_number = verify_secret_santa_sample_somebody_picked_themselves(sample)
        if is_positive:
            positive_events += 1
    return positive_events / iterations


def main(arguments):
    n = arguments.n
    iterations = arguments.iterations
    precision = arguments.precision
    random.seed(time.time())
    probability = calculate_secret_santa_probability_monte_carlo(n, iterations)
    print(f"Probability: {probability:.{precision}f}")


def parse_args():
    parser = argparse.ArgumentParser(description="Secret Santa task CLI arguments")
    parser.add_argument("-n", type=int, required=True, help="Number of people in Secret Santa event")
    parser.add_argument("--iterations", "-it", type=int, required=True, help="Number of iterations for Monte Carlo simulation")
    parser.add_argument("--precision", "-p", type=int, default=6, help="Precision of output probability")
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
