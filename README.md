# python-geoaddress

Address verification and geocoding backends library.

## Features

- 📍 Structured Address dataclass with geocoding support
- 🗺️ 10+ geocoding backends (Nominatim, Google Maps, Mapbox, HERE, etc.)
- ✅ Address validation and normalization
- 🌍 International address support
- 🔌 Pluggable backend system

## Installation

```bash
pip install python-geoaddress
```

## Quick Start

```python
from geoaddress import Address, NominatimAddressBackend

# Create address backend
backend = NominatimAddressBackend(config={
    "user_agent": "my-app/1.0"
})

# Geocode an address
result = backend.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print(f"Coordinates: {result['latitude']}, {result['longitude']}")

# Create Address object
address = Address(
    line1="123 Main St",
    city="Paris",
    postal_code="75001",
    country="France"
)
```

## Available Backends

- **NominatimAddressBackend** - OpenStreetMap (FREE)
- **GoogleMapsAddressBackend** - Google Maps Geocoding
- **MapboxAddressBackend** - Mapbox Geocoding
- **HereAddressBackend** - HERE Location Services
- **LocationIQAddressBackend** - LocationIQ
- **OpenCageAddressBackend** - OpenCage Geocoder
- **PhotonAddressBackend** - Photon (Komoot)
- **GeocodeEarthAddressBackend** - Geocode Earth
- **GeoapifyAddressBackend** - Geoapify
- **MapsCoAddressBackend** - Maps.co

## Development

```bash
# Setup
python dev.py venv
python dev.py install-dev

# Tests
python dev.py test
```

## Used by

- **djgeoaddress** (django-geoaddress) - Django integration
- **pymissive** (python-missive) - Imports Address and backends from geoaddress (optional)

## License

MIT


