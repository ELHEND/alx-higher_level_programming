#!/usr/bin/python3
"""Defines Python class-to-JSON function."""


def class_to_json(obj):
    """Return dictionary represntation of a simple data structure."""
    return obj.__dict__
