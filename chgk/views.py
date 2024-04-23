from quart import render_template


async def index():
    return await render_template('index.html')
