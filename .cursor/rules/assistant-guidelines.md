## Assistant Guidelines

### Project Purpose

**python-geoaddress** is a library for address verification and geocoding. It provides a unified interface to multiple address backends (geocoding services, postal services, verification APIs) to:
- Validate and normalize addresses
- Geocode addresses (convert to coordinates)
- Reverse geocode (convert coordinates to addresses)
- Autocomplete addresses during input
- Standardize international address formats

### Backend Organization

Backends are organized by **service type and provider**:
```
geoaddress/
└── backends/
    ├── geocoding/
    │   ├── nominatim.py          # OpenStreetMap Nominatim
    │   ├── google_maps.py        # Google Maps Geocoding API
    │   ├── mapbox.py             # Mapbox Geocoding
    │   └── here.py               # HERE Location Services
    ├── postal/
    │   ├── french_postal.py      # La Poste API
    │   ├── usps.py               # USPS Address Verification
    │   └── royal_mail.py         # Royal Mail API
    └── validation/
        ├── loqate.py             # Loqate (PCA Predict)
        └── smarty_streets.py     # SmartyStreets
```

Each backend must implement a common interface (BaseAddressBackend) for consistency.

### Development Guidelines

- Always execute project tooling through `python dev.py <command>`.
- Default to English for all code artifacts (comments, docstrings, logging, error strings, documentation snippets, etc.) regardless of the language used in discussions.
- Keep comments minimal and only when they clarify non-obvious logic.
- Avoid reiterating what the code already states clearly.
- Add comments only when they resolve likely ambiguity or uncertainty.
- Do not introduce any dependency on Django or other web frameworks (imports, settings, or implicit coupling).
- **Testing**: Use pytest for all tests. Place tests in `tests/` directory.
- **Type Hints**: All public functions and methods must have complete type hints.
- **Docstrings**: Use Google-style docstrings for all public classes, methods, and functions.
- **Address Backends**: When adding new backends:
  - Create a module in `geoaddress/backends/{service_type}/provider_name.py`
  - Implement BaseAddressBackend interface
  - Each backend must specify its capabilities (geocoding, validation, autocomplete, reverse_geocoding)
  - Never hardcode API keys or credentials
  - Always handle rate limiting and errors gracefully
- **Backend Discovery**: Never hardcode the list of backends. Always resolve via dynamic loading.
- **Data Privacy**: Never log complete addresses or personal information.
