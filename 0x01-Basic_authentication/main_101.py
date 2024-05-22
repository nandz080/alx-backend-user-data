#!/usr/bin/env python3
""" Main script to test Auth class. """

from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/status", ["/api/v1/stat*"]))  # Expected: False
print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))   # Expected: False
print(a.require_auth("/api/v1/users", ["/api/v1/stat*"]))   # Expected: True
print(a.require_auth("/api/v1/status", ["/api/v1/status"])) # Expected: False
print(a.require_auth("/api/v1/stats", ["/api/v1/status"]))  # Expected: True
print(a.require_auth("/api/v1/users", ["/api/v1/status"]))  # Expected: True
