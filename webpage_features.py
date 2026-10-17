import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def analyse_webpage(url):

    result = {
        "NoOfURLRedirect": 0,
        "NoOfSelfRedirect": 0,
        "HasExternalFormSubmit": 0,
        "HasPasswordField": 0,
        "NoOfExternalRef": 0
    }

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=8,
            allow_redirects=True
        )

        # -----------------------------
        # Redirect analysis
        # -----------------------------

        result["NoOfURLRedirect"] = len(
            response.history
        )

        original_domain = urlparse(url).netloc.lower()

        final_domain = urlparse(
            response.url
        ).netloc.lower()

        if original_domain and final_domain:
            if original_domain == final_domain:
                result["NoOfSelfRedirect"] = len(
                    response.history
                )

        # -----------------------------
        # HTML analysis
        # -----------------------------

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Password field
        password_fields = soup.find_all(
            "input",
            {"type": "password"}
        )

        if password_fields:
            result["HasPasswordField"] = 1

        # -----------------------------
        # Form analysis
        # -----------------------------

        forms = soup.find_all("form")

        for form in forms:

            action = form.get("action", "").strip()

            if not action:
                continue

            absolute_action = urljoin(
                response.url,
                action
            )

            action_domain = urlparse(
                absolute_action
            ).netloc.lower()

            if (
                action_domain
                and original_domain
                and action_domain != original_domain
            ):
                result["HasExternalFormSubmit"] = 1

        # -----------------------------
        # External references
        # -----------------------------

        external_refs = set()

        tags = soup.find_all(
            ["a", "img", "script", "link", "iframe"]
        )

        for tag in tags:

            attribute = None

            if tag.name == "a":
                attribute = tag.get("href")

            elif tag.name in ["img", "script", "iframe"]:
                attribute = tag.get("src")

            elif tag.name == "link":
                attribute = tag.get("href")

            if not attribute:
                continue

            absolute_url = urljoin(
                response.url,
                attribute
            )

            ref_domain = urlparse(
                absolute_url
            ).netloc.lower()

            if (
                ref_domain
                and original_domain
                and ref_domain != original_domain
            ):
                external_refs.add(ref_domain)

        result["NoOfExternalRef"] = len(
            external_refs
        )

    except Exception as error:

        print(
            f"[!] Webpage analysis failed: {error}"
        )

    return result


if __name__ == "__main__":

    test_url = "https://www.google.com"

    print("\n==============================")
    print("WEBPAGE FEATURE ANALYSIS")
    print("==============================")

    features = analyse_webpage(
        test_url
    )

    for key, value in features.items():
        print(f"{key}: {value}")