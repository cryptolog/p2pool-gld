from p2pool.bitcoin import networks

PARENT = networks.nets['goldcoin']
SHARE_PERIOD=10
CHAIN_LENGTH=24*60*60//10
REAL_CHAIN_LENGTH=12*60*60//10
TARGET_LOOKBEHIND=20
SPREAD=50
IDENTIFIER='1ffa2b25a2e30009'.decode('hex')
PREFIX='1ffa2b25a2e3000a'.decode('hex')
P2P_PORT=8123
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=8124
BOOTSTRAP_ADDRS='crypto.office-on-the.net'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-gld'
VERSION_CHECK=lambda v: True
