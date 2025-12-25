from pathlib import Path
from typing import Any

from providerkit.helpers import get_providers, try_providers


def get_address_providers(
    *,
    json: str | Path | None = None,
    lib_name: str = "geoaddress",
    config: list[dict[str, Any]] | None = None,
    dir_path: str | Path | None = None,
    base_module: str | None = None,
    query_string: str | None = None,
    search_fields: list[str] | None = None,
    attribute_search: dict[str, str] | None = None,
    format: str | None = None,
) -> dict[str, Any] | str:
    """Get address providers."""
    providers = get_providers(  # type: ignore[no-any-return]
        json=json,
        lib_name=lib_name,
        config=config,
        dir_path=dir_path,
        base_module=base_module,
        query_string=query_string,
        search_fields=search_fields,
        attribute_search=attribute_search,
        format=format,
    )
    if not len(providers):
        raise ValueError("No providers found")
    return providers


def get_address_provider(
    name: str,
) -> Any:
    """Get address provider."""
    providers = get_providers(  # type: ignore[no-any-return]
        lib_name="geoaddress",
        attribute_search={"name": name},
        format="python",
    )
    if len(providers) > 1:
        raise ValueError(f"Expected 1 provider, got {len(providers)}")
    return providers[0]
    

def search_addresses(
    query: str,
    *,
    providers: dict[str, Any] | None = None,
    json: str | Path | None = None,
    lib_name: str = "geoaddress",
    config: list[dict[str, Any]] | None = None,
    dir_path: str | Path | None = None,
    base_module: str | None = None,
    query_string: str | None = None,
    search_fields: list[str] | None = None,
    **kwargs: Any,
) -> Any:
    """Search addresses using providers."""
    return try_providers(
        "search_addresses",
        query,
        providers=providers,
        json=json,
        lib_name=lib_name,
        config=config,
        dir_path=dir_path,
        base_module=base_module,
        query_string=query_string,
        search_fields=search_fields,
        **kwargs,
    )


def get_address_by_reference(
    reference: str,
    *,
    providers: dict[str, Any] | None = None,
    json: str | Path | None = None,
    lib_name: str = "geoaddress",
    config: list[dict[str, Any]] | None = None,
    dir_path: str | Path | None = None,
    base_module: str | None = None,
    query_string: str | None = None,
    search_fields: list[str] | None = None,
    **kwargs: Any,
) -> Any:
    """Get address by reference using providers."""
    return try_providers(
        "get_address_by_reference",
        reference,
        providers=providers,
        json=json,
        lib_name=lib_name,
        config=config,
        dir_path=dir_path,
        base_module=base_module,
        query_string=query_string,
        search_fields=search_fields,
        **kwargs,
    )
