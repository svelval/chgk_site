class MultipleObjectsExist(Exception):
    pass


class ObjectDoesNotExist(Exception):
    pass


class ConnectionPoolCannotBeCreated(Exception):
    pass


class ConnectionPoolDoesNotExist(Exception):
    pass


class InternalDatabaseError(Exception):
    pass