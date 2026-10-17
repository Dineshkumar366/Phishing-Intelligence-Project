from urllib.parse import urlparse
import math
from collections import Counter


def calculate_char_continuation_rate(url):
    """
    Calculates the rate of consecutive repeated characters.
    """

    if len(url) <= 1:
        return 0.0

    continuation_count = 0

    for i in range(1, len(url)):
        if url[i].lower() == url[i - 1].lower():
            continuation_count += 1

    return continuation_count / (len(url) - 1)


def calculate_url_char_probability(url):
    """
    Calculates character probability based on
    character frequency distribution.
    """

    if not url:
        return 0.0

    counter = Counter(url)
    length = len(url)

    probability_score = 0.0

    for count in counter.values():
        probability = count / length

        if probability > 0:
            probability_score += probability * math.log2(
                1 / probability
            )

    return probability_score


def get_tld(url):
    """
    Extracts TLD from hostname.
    """

    parsed = urlparse(url)

    hostname = parsed.netloc.lower()

    hostname = hostname.split("@")[-1]
    hostname = hostname.split(":")[0]

    parts = hostname.split(".")

    if len(parts) >= 2:
        return parts[-1]

    return ""


def calculate_statistical_features(url):

    features = {}

    features["CharContinuationRate"] = (
        calculate_char_continuation_rate(url)
    )

    features["URLCharProb"] = (
        calculate_url_char_probability(url)
    )

    features["TLD"] = get_tld(url)

    return features


if __name__ == "__main__":

    test_url = "https://www.google.com"

    print("\n==============================")
    print("STATISTICAL FEATURE ANALYSIS")
    print("==============================")

    result = calculate_statistical_features(
        test_url
    )

    for key, value in result.items():
        print(f"{key}: {value}")