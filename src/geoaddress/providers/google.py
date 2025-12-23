from . import GeoaddressProvider


class GoogleProvider(GeoaddressProvider):
    name = "google"
    display_name = "Google"
    description = "Google provider"
    required_packages = ["google"]
    documentation_url = "https://google.com/docs"
    site_url = "https://google.com"
    config_keys = ["GOOGLE_API_KEY"]
    config_defaults = {
        "GOOGLE_API_KEY": None,
    }
    required_packages = ["requests"]

