from chgk.context_processor import static_files_context_processor


async def context_processor():
    static_function = static_files_context_processor
    return {
        'static': static_function,
    }
