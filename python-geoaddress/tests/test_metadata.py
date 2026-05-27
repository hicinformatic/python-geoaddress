"""Tests for public geoaddress metadata."""

from geoaddress import (
    GEOADDRESS_FIELDS_DESCRIPTIONS,
    GEOADDRESS_FIELDS_ESSENTIALS,
    GEOADDRESS_FIELDS_EXTENDED,
    GEOADDRESS_FULL_FIELDS,
)


def test_public_field_maps_are_consistent() -> None:
    """Core field registries should expose expected public keys."""
    assert "address_line1" in GEOADDRESS_FIELDS_ESSENTIALS
    assert "confidence" in GEOADDRESS_FIELDS_EXTENDED
    assert "latitude" in GEOADDRESS_FULL_FIELDS
    assert GEOADDRESS_FIELDS_DESCRIPTIONS["address_line1"]["format"] == "str"
    assert GEOADDRESS_FIELDS_DESCRIPTIONS["confidence"]["format"] == "float"
