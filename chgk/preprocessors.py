from chgk.context_processor import static_files_context_processor
from settings import db


async def on_startup():
    await db.create_connection_pool()


async def on_shutdown():
    await db.close_all_connections()


async def context_processor():
    static_function = static_files_context_processor
    return {
        'static': static_function,
    }
