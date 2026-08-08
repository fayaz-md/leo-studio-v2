"""
Leo Studio Service Container
"""


class Services:

    def __init__(self):

        self._services = {}

    # =====================================================
    # Register
    # =====================================================

    def register(
        self,
        name,
        service,
    ):

        self._services[name] = service

    # =====================================================
    # Get
    # =====================================================

    def get(
        self,
        name,
    ):

        return self._services.get(name)

    # =====================================================
    # Exists
    # =====================================================

    def has(
        self,
        name,
    ):

        return name in self._services