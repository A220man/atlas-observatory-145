"""Learning surface access control."""
from typing import Set

def assert_learning_surface(surface: str, allowed_surfaces: Set[str]) -> None:
    if surface not in allowed_surfaces:
        raise PermissionError(
            f"Learning surface '{surface}' is not allowed. "
            f"Allowed surfaces: {sorted(allowed_surfaces)}"
        )