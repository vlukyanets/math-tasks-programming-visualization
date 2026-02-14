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

def calculate_secret_santa_probability_monte_carlo(n: int, iterations: int, progress: bool) -> float:
    """
    :param n: Number of people in Secret Santa event
    :param iterations: Number of iterations for Monte Carlo simulation
    :param progress: Show progress bar
    :return: Probability that somebody picked themselves in Secret Santa event with n people
    """
    positive_events = 0
    rng = tqdm.tqdm(range(iterations)) if progress else range(iterations)
    for _ in rng:
        sample = secret_santa_generate_sample(n)
        is_positive, themselves_picker_number = verify_secret_santa_sample_somebody_picked_themselves(sample)
        if is_positive:
            positive_events += 1
    return positive_events / iterations


def calculate_secret_santa_probability_taylor_series(n: int, progress: bool) -> float:
    """
    :param n: Number of people in Secret Santa event
    :param progress: Show progress bar
    :return: Probability that somebody picked themselves in Secret Santa event with n people
    """
    # Formula is sum for each k from 0 to +inf (or to specified limit) series member (-1)^k / k!
    f, sgn, s = 1, 1, 0
    rng = tqdm.tqdm(range(1, n + 1)) if progress else range(1, n + 1)
    for it in rng:
        s += sgn / f
        f *= it
        sgn *= -1
    return 1 - s


def main(arguments):
    n = arguments.n
    iterations = arguments.iterations
    precision = arguments.precision
    progress = arguments.progress
    random.seed(time.time())
    p_monte_carlo = calculate_secret_santa_probability_monte_carlo(n, iterations, progress)
    p_taylor_series = calculate_secret_santa_probability_taylor_series(n, progress)
    print(f"Probability (Monte Carlo method): {p_monte_carlo:.{precision}f}")
    print(f"Probability (Taylor series method): {p_taylor_series:.{precision}f}")


def parse_args():
    parser = argparse.ArgumentParser(description="Secret Santa task CLI arguments")
    parser.add_argument("-n", type=int, required=True, help="Number of people in Secret Santa event")
    parser.add_argument("--iterations", "-it", type=int, required=True, help="Number of iterations for Monte Carlo simulation")
    parser.add_argument("--precision", "-p", type=int, default=6, help="Precision of output probability")
    parser.add_argument("--progress", action="store_true", help="Show progress bar")
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
