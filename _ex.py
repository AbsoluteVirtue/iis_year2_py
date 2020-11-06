import aiohttp
import aiohttp_jinja2
import asyncio
import jinja2
import os
from aiohttp import web


class List:
    pass


if __name__ == '__main__':
    app = web.Application(loop=asyncio.get_event_loop())

    app['client'] = aiohttp.ClientSession()
    app.router.add_view(r'/', handler=List)

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.abspath('templates')))
    web.run_app(app, host='localhost', port=9980)
