from .base import api_function
from .request import Request

__all__ = (
    'EtcdConfig',
)


class EtcdConfig:
    '''
    Provides a way to get or set ETCD configurations.

    .. note::

      All methods in this function class require your API access key to
      have the *superadmin* privilege.
    '''

    session = None
    '''The client session instance that this function class is bound to.'''

    @api_function
    @classmethod
    async def get(cls, key: str, prefix: bool = False) -> dict:
        '''
        Get configuration from ETCD with given key.

        :param key: Name of the key to fetch.
        :param prefix: get all keys prefixed with the give key.
        '''
        rqst = Request(cls.session, 'POST', '/config/get')
        rqst.set_json({
            'key': key,
            'prefix': prefix,
        })
        async with rqst.fetch() as resp:
            data = await resp.json()
            return data.get('result', None)

    @api_function
    @classmethod
    async def set(cls, key: str, value: str) -> dict:
        '''
        Set configuration into ETCD with given key and value.

        :param key: Name of the key to set.
        :param value: Value to set.
        '''
        rqst = Request(cls.session, 'POST', '/config/set')
        rqst.set_json({
            'key': key,
            'value': value,
        })
        async with rqst.fetch() as resp:
            data = await resp.json()
            return data

    @api_function
    @classmethod
    async def delete(cls, key: str, prefix: bool = False) -> dict:
        '''
        Delete configuration from ETCD with given key.

        :param key: Name of the key to delete.
        :param prefix: delete all keys prefixed with the give key.
        '''
        rqst = Request(cls.session, 'POST', '/config/delete')
        rqst.set_json({
            'key': key,
            'prefix': prefix,
        })
        async with rqst.fetch() as resp:
            data = await resp.json()
            return data
