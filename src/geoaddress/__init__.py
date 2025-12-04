"""Geoaddress - Address verification and geocoding backends."""

__version__ = "0.1.0"

from .address import Address
from .backends import (
    BaseAddressBackend,
    GeocodeEarthAddressBackend,
    GeoapifyAddressBackend,
    GoogleMapsAddressBackend,
    HereAddressBackend,
    LocationIQAddressBackend,
    MapsCoAddressBackend,
    MapboxAddressBackend,
    NominatimAddressBackend,
    OpenCageAddressBackend,
    PhotonAddressBackend,
)
from .helpers import (
    describe_address_backends,
    get_address_backend_by_attribute,
    get_address_backends_from_config,
    get_address_by_reference,
    search_addresses,
)

__all__ = [
    "__version__",
    "Address",
    "BaseAddressBackend",
    "GeocodeEarthAddressBackend",
    "GeoapifyAddressBackend",
    "GoogleMapsAddressBackend",
    "HereAddressBackend",
    "LocationIQAddressBackend",
    "MapsCoAddressBackend",
    "MapboxAddressBackend",
    "NominatimAddressBackend",
    "OpenCageAddressBackend",
    "PhotonAddressBackend",
    # Helper functions
    "describe_address_backends",
    "get_address_backend_by_attribute",
    "get_address_backends_from_config",
    "get_address_by_reference",
    "search_addresses",
]
