import aiohttp
import aiohttp_jinja2
import asyncio
import jinja2
import logging
import os.path
from aiohttp import web


_PORT = 9898


class Base(web.View):

    async def _get(self, url):
        async with self.request.app['client'].get(url) as resp:
            assert resp.status == 200
            return await resp.text()

    # async def get(self):
    #     return web.json_response({
    #         'list': [],
    #     }, status=200)


class Home(Base):

    async def get(self):
        data = {
            'data': [{
                'name': 'Ivan Petrov',
                'group': 'MI-192',
                'grade': '7.9',
                'status': 'public',
            }],
            'count': 1,
        }
        response = aiohttp_jinja2.render_template('home.html', self.request, context=data)
        return response


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    session = aiohttp.ClientSession()
    app['client'] = session

    app.router.add_view(r'/', handler=Home)

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.abspath('templates')))

    logging.getLogger('aiohttp.server').setLevel(logging.DEBUG)
    logging.getLogger('aiohttp.web').setLevel(logging.DEBUG)

    logger = logging.getLogger('aiohttp.access')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    logger.info('======== Running aiohttp (%s) ========\n', aiohttp.__version__)

    web.run_app(
        app, host='localhost', port=_PORT,
        access_log=logger, access_log_format='%t %P %s %r (%a) [%{Referer}i] %Tf'
    )
