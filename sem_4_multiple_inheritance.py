import aiohttp
import asyncio
import logging
from aiohttp import web


_PORT = 9898


class Base(web.View):

    async def _get(self, url):
        async with self.request.app['client'].get(url) as resp:
            assert resp.status == 200
            return await resp.text()


class Home(Base):

    async def get(self):
        return web.json_response({
            'list': [],
        }, status=200)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    session = aiohttp.ClientSession()
    app['client'] = session

    app.router.add_view(r'/', handler=Home)

    logging.getLogger('aiohttp.server').setLevel(logging.DEBUG)
    logging.getLogger('aiohttp.web').setLevel(logging.DEBUG)

    logger = logging.getLogger('aiohttp.access')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    logger.info('======== Running aiohttp (%s) ========\n',
                aiohttp.__version__, _PORT)

    web.run_app(
        app, host='localhost', port=_PORT,
        access_log=logger, access_log_format='%t %P %s %r (%a) [%{Referer}i] %Tf'
    )
