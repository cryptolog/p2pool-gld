import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'e7420652'.decode('hex') #pchmessagestart
P2P_PORT = 19667
ADDRESS_VERSION = 0 #pubkey_address
RPC_PORT = 19666
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Grimaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 65000000*100000000 if height==1 else 1*100000000 if height<=250 && height>1 else 5*100000000 if height<=500 && height>250 else 10*100000000 if height<=1000 && height>500 else 25*100000000 if height<=2000 && height>1000 else 75*100000000 if height<=3000 && height>2000 else 200*100000000 if height<=9000 && height>3000 else 10*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 64 # s
SYMBOL = 'GRIM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'GrimMasterNode') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/GrimMasterNode/') if platform.system() == 'Darwin' else os.path.expanduser('~/.GrimMN'), 'Grim.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.reaper.rocks/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.reaper.rocks/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.reaper.rocks/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0
