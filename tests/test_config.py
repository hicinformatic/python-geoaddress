"""Test configuration for address backends.

This configuration provides test settings for all geoaddress backends.
Environment variables from .env file will override default values if present.
"""

import os


def _get_env_or_default(key: str, default: str) -> str:
    """Get environment variable or return default value."""
    return os.getenv(key, default)


# Address verification backends configuration
# Ordered list: the first working backend is used
GEOADDRESS_BACKENDS = [
    {
        "class": "geoaddress.backends.nominatim.NominatimAddressBackend",
        "config": {
            "NOMINATIM_USER_AGENT": _get_env_or_default("NOMINATIM_USER_AGENT", "python-geoaddress/1.0"),
            "NOMINATIM_BASE_URL": _get_env_or_default("NOMINATIM_BASE_URL", "https://nominatim.openstreetmap.org"),
        },
    },
    {
        "class": "geoaddress.backends.photon.PhotonAddressBackend",
        "config": {
            "PHOTON_BASE_URL": _get_env_or_default("PHOTON_BASE_URL", "https://photon.komoot.io"),
        },
    },
    {
        "class": "geoaddress.backends.locationiq.LocationIQAddressBackend",
        "config": {
            "LOCATIONIQ_API_KEY": _get_env_or_default("LOCATIONIQ_API_KEY", ""),
            "LOCATIONIQ_BASE_URL": _get_env_or_default("LOCATIONIQ_BASE_URL", "https://api.locationiq.com/v1"),
        },
    },
    {
        "class": "geoaddress.backends.opencage.OpenCageAddressBackend",
        "config": {
            "OPENCAGE_API_KEY": _get_env_or_default("OPENCAGE_API_KEY", ""),
            "OPENCAGE_BASE_URL": _get_env_or_default("OPENCAGE_BASE_URL", "https://api.opencagedata.com/geocode/v1"),
        },
    },
    {
        "class": "geoaddress.backends.geocode_earth.GeocodeEarthAddressBackend",
        "config": {
            "GEOCODE_EARTH_API_KEY": _get_env_or_default("GEOCODE_EARTH_API_KEY", ""),
            "GEOCODE_EARTH_BASE_URL": _get_env_or_default("GEOCODE_EARTH_BASE_URL", "https://api.geocode.earth/v1"),
        },
    },
    {
        "class": "geoaddress.backends.geoapify.GeoapifyAddressBackend",
        "config": {
            "GEOAPIFY_API_KEY": _get_env_or_default("GEOAPIFY_API_KEY", ""),
            "GEOAPIFY_BASE_URL": _get_env_or_default("GEOAPIFY_BASE_URL", "https://api.geoapify.com/v1"),
        },
    },
    {
        "class": "geoaddress.backends.maps_co.MapsCoAddressBackend",
        "config": {
            "MAPS_CO_API_KEY": _get_env_or_default("MAPS_CO_API_KEY", ""),
            "MAPS_CO_BASE_URL": _get_env_or_default("MAPS_CO_BASE_URL", "https://geocode.maps.co"),
        },
    },
    {
        "class": "geoaddress.backends.google_maps.GoogleMapsAddressBackend",
        "config": {
            "GOOGLE_MAPS_API_KEY": _get_env_or_default("GOOGLE_MAPS_API_KEY", ""),
        },
    },
    {
        "class": "geoaddress.backends.mapbox.MapboxAddressBackend",
        "config": {
            "MAPBOX_ACCESS_TOKEN": _get_env_or_default("MAPBOX_ACCESS_TOKEN", ""),
        },
    },
    {
        "class": "geoaddress.backends.here.HereAddressBackend",
        "config": {
            "HERE_APP_ID": _get_env_or_default("HERE_APP_ID", ""),
            "HERE_APP_CODE": _get_env_or_default("HERE_APP_CODE", ""),
        },
    },
]


# Example of how to instantiate a backend for testing
def get_backend(backend_class_path: str):
    """Get a backend instance by class path.
    
    Args:
        backend_class_path: Full path to backend class (e.g., "geoaddress.backends.nominatim.NominatimAddressBackend")
        
    Returns:
        Instance of the backend with config from GEOADDRESS_BACKENDS
    """
    from importlib import import_module
    
    # Find the backend config
    backend_config = None
    for config in GEOADDRESS_BACKENDS:
        if config["class"] == backend_class_path:
            backend_config = config["config"]
            break
    
    if backend_config is None:
        raise ValueError(f"Backend {backend_class_path} not found in GEOADDRESS_BACKENDS")
    
    # Import and instantiate the backend
    module_path, class_name = backend_class_path.rsplit(".", 1)
    module = import_module(module_path)
    backend_class = getattr(module, class_name)
    
    return backend_class(config=backend_config)

