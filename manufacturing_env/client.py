"""Validator-friendly client module for OpenEnv discovery."""

from .env import ManufacturingEnv as _ManufacturingEnvironment


class ManufacturingEnv(_ManufacturingEnvironment):
    """Thin alias so OpenEnv can resolve the expected client class name."""


__all__ = ["ManufacturingEnv"]
