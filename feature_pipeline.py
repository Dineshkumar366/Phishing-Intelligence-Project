from urllib.parse import urlparse
import re
import math


FEATURES = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "URLSimilarityIndex",
    "CharContinuationRate",
    "TLDLegitimateProb",
    "URLCharProb",
    "TLDLength",
    "NoOfSubDomain",
    "HasObfuscation",
    "ObfuscationRatio",
    "NoOfLettersInURL",
    "LetterRatioInURL",
    "NoOfDegitsInURL",
    "DegitRatioInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "NoOfOtherSpecialCharsInURL",
    "SpacialCharRatioInURL",
    "IsHTTPS",
    "NoOfURLRedirect",
    "NoOfSelfRedirect",
    "HasExternalFormSubmit",
    "HasPasswordField",
    "NoOfExternalRef"
]


def calculate_entropy(text):
    if not text:
        return 0.0

    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    entropy = 0.0
    length = len(text)

    for count in frequency.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy


def extract_url_features(url):
    parsed = urlparse(url)

    hostname = parsed.netloc.lower()

    # Remove username/password and port
    hostname_clean = hostname.split("@")[-1].split(":")[0]

    url_length = len(url)
    domain_length = len(hostname_clean)

    # IPv4 address detection
    is_domain_ip = 1 if re.fullmatch(
        r"\d{1,3}(\.\d{1,3}){3}",
        hostname_clean
    ) else 0

    # TLD
    domain_parts = hostname_clean.split(".")
    tld = domain_parts[-1] if len(domain_parts) > 1 else ""

    tld_length = len(tld)

    # Subdomain count
    no_of_subdomain = max(len(domain_parts) - 2, 0)

    # Obfuscation
    obfuscation_patterns = [
        "@",
        "%",
        "\\x",
        "javascript:"
    ]

    obfuscated_count = sum(
        url.lower().count(pattern)
        for pattern in obfuscation_patterns
    )

    has_obfuscation = 1 if obfuscated_count > 0 else 0

    obfuscation_ratio = (
        obfuscated_count / url_length
        if url_length else 0
    )

    # Letters and digits
    letters = sum(char.isalpha() for char in url)
    digits = sum(char.isdigit() for char in url)

    letter_ratio = (
        letters / url_length
        if url_length else 0
    )

    digit_ratio = (
        digits / url_length
        if url_length else 0
    )

    # Query characters
    no_of_equals = url.count("=")
    no_of_qmark = url.count("?")
    no_of_ampersand = url.count("&")

    # Other special characters
    special_set = "!#$%&'()*+,;:=?@[\\]^_`{|}~"

    no_of_other_special_chars = sum(
        1 for char in url
        if char in special_set
    )

    special_ratio = (
        no_of_other_special_chars / url_length
        if url_length else 0
    )

    # HTTPS
    is_https = 1 if parsed.scheme.lower() == "https" else 0

    # Character continuation rate
    # Measures repeated consecutive character behaviour.
    continuation_count = 0

    for i in range(1, len(url)):
        if url[i].lower() == url[i - 1].lower():
            continuation_count += 1

    char_continuation_rate = (
        continuation_count / (url_length - 1)
        if url_length > 1 else 0
    )

    # URL character probability proxy.
    # Uses character entropy of the URL.
    url_char_prob = calculate_entropy(url)

    # These require webpage/domain intelligence.
    # We keep them explicitly unavailable rather than
    # inventing values.
    url_similarity_index = 0.0
    tld_legitimate_prob = 0.0

    no_of_url_redirect = 0
    no_of_self_redirect = 0
    has_external_form_submit = 0
    has_password_field = 0
    no_of_external_ref = 0

    return {
        "URLLength": url_length,
        "DomainLength": domain_length,
        "IsDomainIP": is_domain_ip,

        "URLSimilarityIndex": url_similarity_index,
        "CharContinuationRate": char_continuation_rate,
        "TLDLegitimateProb": tld_legitimate_prob,
        "URLCharProb": url_char_prob,

        "TLDLength": tld_length,
        "NoOfSubDomain": no_of_subdomain,

        "HasObfuscation": has_obfuscation,
        "ObfuscationRatio": obfuscation_ratio,

        "NoOfLettersInURL": letters,
        "LetterRatioInURL": letter_ratio,

        "NoOfDegitsInURL": digits,
        "DegitRatioInURL": digit_ratio,

        "NoOfEqualsInURL": no_of_equals,
        "NoOfQMarkInURL": no_of_qmark,
        "NoOfAmpersandInURL": no_of_ampersand,

        "NoOfOtherSpecialCharsInURL":
            no_of_other_special_chars,

        "SpacialCharRatioInURL": special_ratio,

        "IsHTTPS": is_https,

        "NoOfURLRedirect": no_of_url_redirect,
        "NoOfSelfRedirect": no_of_self_redirect,

        "HasExternalFormSubmit":
            has_external_form_submit,

        "HasPasswordField":
            has_password_field,

        "NoOfExternalRef":
            no_of_external_ref
    }


def prepare_model_input(url):
    """
    Returns the features in the exact order
    expected by the saved Random Forest model.
    """

    extracted = extract_url_features(url)

    return [
        extracted[feature]
        for feature in FEATURES
    ]


if __name__ == "__main__":

    test_url = "https://www.google.com"

    result = extract_url_features(test_url)

    print("\n==============================")
    print("26-FEATURE URL PIPELINE")
    print("==============================")

    for feature in FEATURES:
        print(f"{feature}: {result[feature]}")

    model_input = prepare_model_input(test_url)

    print("\n==============================")
    print("MODEL INPUT")
    print("==============================")

    print(f"Feature count: {len(model_input)}")
    print(model_input)