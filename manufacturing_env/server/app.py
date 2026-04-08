"""Compatibility wrapper for the deployed FastAPI application."""

from server.app import app, main

__all__ = ["app", "main"]
