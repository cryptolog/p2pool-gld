from p2pool.bitcoin import networks

PARENT = networks.nets['grimcoin']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 30 # blocks
IDENTIFIER = '6B70A9DD349FBADE'.decode('hex')
PREFIX = '2D3A1616DFB4D029'.decode('hex')
P2P_PORT = 7042
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 3035
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
