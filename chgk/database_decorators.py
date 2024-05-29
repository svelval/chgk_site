from inspect import iscoroutinefunction

from pymysql import OperationalError

from chgk.database_exceptions import ConnectionPoolDoesNotExist, ConnectionPoolCannotBeCreated, InternalDatabaseError, \
    ObjectDoesNotExist


def database_errors_handler(fun):
    async def async_wrapper(*args, **kwargs):
        try:
            return await fun(*args, **kwargs)
        except (AttributeError, NameError):
            raise ConnectionPoolDoesNotExist('Connection pool does not exist')
        except OperationalError as ex:
            raise ConnectionPoolCannotBeCreated(f'Connection pool cannot be created: {ex}')
        except ObjectDoesNotExist as obj_not_exist_ex:
            raise ObjectDoesNotExist(str(obj_not_exist_ex))
        except Exception as other_ex:
            raise InternalDatabaseError(f'Internal database error: {other_ex}')

    def sync_wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except (AttributeError, NameError):
            raise ConnectionPoolDoesNotExist('Connection pool does not exist')
        except OperationalError as ex:
            raise ConnectionPoolCannotBeCreated(f'Connection pool cannot be created: {ex}')
        except Exception as other_ex:
            raise InternalDatabaseError(f'Internal database error: {other_ex}')
    if iscoroutinefunction(fun):
        return async_wrapper
    else:
        return sync_wrapper