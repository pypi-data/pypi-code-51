from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure

from cwinsdk.shared.ntdef import UCHAR

# Command Descriptor Block constants.

CDB6GENERIC_LENGTH = 6
CDB10GENERIC_LENGTH = 10
CDB12GENERIC_LENGTH = 12

SETBITON = 1
SETBITOFF = 0

MODE_PAGE_VENDOR_SPECIFIC = 0x00
MODE_PAGE_ERROR_RECOVERY = 0x01
MODE_PAGE_DISCONNECT = 0x02
MODE_PAGE_FORMAT_DEVICE = 0x03
MODE_PAGE_MRW = 0x03
MODE_PAGE_RIGID_GEOMETRY = 0x04
MODE_PAGE_FLEXIBILE = 0x05
MODE_PAGE_WRITE_PARAMETERS = 0x05
MODE_PAGE_VERIFY_ERROR = 0x07
MODE_PAGE_CACHING = 0x08
MODE_PAGE_PERIPHERAL = 0x09
MODE_PAGE_CONTROL = 0x0A
MODE_PAGE_MEDIUM_TYPES = 0x0B
MODE_PAGE_NOTCH_PARTITION = 0x0C
MODE_PAGE_CD_AUDIO_CONTROL = 0x0E
MODE_PAGE_DATA_COMPRESS = 0x0F
MODE_PAGE_DEVICE_CONFIG = 0x10
MODE_PAGE_XOR_CONTROL = 0x10
MODE_PAGE_MEDIUM_PARTITION = 0x11
MODE_PAGE_ENCLOSURE_SERVICES_MANAGEMENT = 0x14
MODE_PAGE_EXTENDED = 0x15
MODE_PAGE_EXTENDED_DEVICE_SPECIFIC = 0x16
MODE_PAGE_CDVD_FEATURE_SET = 0x18
MODE_PAGE_PROTOCOL_SPECIFIC_LUN = 0x18
MODE_PAGE_PROTOCOL_SPECIFIC_PORT = 0x19
MODE_PAGE_POWER_CONDITION = 0x1A
MODE_PAGE_LUN_MAPPING = 0x1B
MODE_PAGE_FAULT_REPORTING = 0x1C
MODE_PAGE_CDVD_INACTIVITY = 0x1D
MODE_PAGE_ELEMENT_ADDRESS = 0x1D
MODE_PAGE_TRANSPORT_GEOMETRY = 0x1E
MODE_PAGE_DEVICE_CAPABILITIES = 0x1F
MODE_PAGE_CAPABILITIES = 0x2A

MODE_SENSE_RETURN_ALL = 0x3f

MODE_SENSE_CURRENT_VALUES = 0x00
MODE_SENSE_CHANGEABLE_VALUES = 0x40
MODE_SENSE_DEFAULT_VAULES = 0x80
MODE_SENSE_SAVED_VALUES = 0xc0

# 6-byte commands:
SCSIOP_TEST_UNIT_READY = 0x00
SCSIOP_REZERO_UNIT = 0x01
SCSIOP_REWIND = 0x01
SCSIOP_REQUEST_BLOCK_ADDR = 0x02
SCSIOP_REQUEST_SENSE = 0x03
SCSIOP_FORMAT_UNIT = 0x04
SCSIOP_READ_BLOCK_LIMITS = 0x05
SCSIOP_REASSIGN_BLOCKS = 0x07
SCSIOP_INIT_ELEMENT_STATUS = 0x07
SCSIOP_READ6 = 0x08
SCSIOP_RECEIVE = 0x08
SCSIOP_WRITE6 = 0x0A
SCSIOP_PRINT = 0x0A
SCSIOP_SEND = 0x0A
SCSIOP_SEEK6 = 0x0B
SCSIOP_TRACK_SELECT = 0x0B
SCSIOP_SLEW_PRINT = 0x0B
SCSIOP_SET_CAPACITY = 0x0B
SCSIOP_SEEK_BLOCK = 0x0C
SCSIOP_PARTITION = 0x0D
SCSIOP_READ_REVERSE = 0x0F
SCSIOP_WRITE_FILEMARKS = 0x10
SCSIOP_FLUSH_BUFFER = 0x10
SCSIOP_SPACE = 0x11
SCSIOP_INQUIRY = 0x12
SCSIOP_VERIFY6 = 0x13
SCSIOP_RECOVER_BUF_DATA = 0x14
SCSIOP_MODE_SELECT = 0x15
SCSIOP_RESERVE_UNIT = 0x16
SCSIOP_RELEASE_UNIT = 0x17
SCSIOP_COPY = 0x18
SCSIOP_ERASE = 0x19
SCSIOP_MODE_SENSE = 0x1A
SCSIOP_START_STOP_UNIT = 0x1B
SCSIOP_STOP_PRINT = 0x1B
SCSIOP_LOAD_UNLOAD = 0x1B
SCSIOP_RECEIVE_DIAGNOSTIC = 0x1C
SCSIOP_SEND_DIAGNOSTIC = 0x1D
SCSIOP_MEDIUM_REMOVAL = 0x1E

# 10-byte commands
SCSIOP_READ_FORMATTED_CAPACITY = 0x23
SCSIOP_READ_CAPACITY = 0x25
SCSIOP_READ = 0x28
SCSIOP_WRITE = 0x2A
SCSIOP_SEEK = 0x2B
SCSIOP_LOCATE = 0x2B
SCSIOP_POSITION_TO_ELEMENT = 0x2B
SCSIOP_WRITE_VERIFY = 0x2E
SCSIOP_VERIFY = 0x2F
SCSIOP_SEARCH_DATA_HIGH = 0x30
SCSIOP_SEARCH_DATA_EQUAL = 0x31
SCSIOP_SEARCH_DATA_LOW = 0x32
SCSIOP_SET_LIMITS = 0x33
SCSIOP_READ_POSITION = 0x34
SCSIOP_SYNCHRONIZE_CACHE = 0x35
SCSIOP_COMPARE = 0x39
SCSIOP_COPY_COMPARE = 0x3A
SCSIOP_WRITE_DATA_BUFF = 0x3B
SCSIOP_READ_DATA_BUFF = 0x3C
SCSIOP_WRITE_LONG = 0x3F
SCSIOP_CHANGE_DEFINITION = 0x40
SCSIOP_WRITE_SAME = 0x41
SCSIOP_READ_SUB_CHANNEL = 0x42
SCSIOP_UNMAP = 0x42
SCSIOP_READ_TOC = 0x43
SCSIOP_READ_HEADER = 0x44
SCSIOP_REPORT_DENSITY_SUPPORT = 0x44
SCSIOP_PLAY_AUDIO = 0x45
SCSIOP_GET_CONFIGURATION = 0x46
SCSIOP_PLAY_AUDIO_MSF = 0x47
SCSIOP_PLAY_TRACK_INDEX = 0x48
SCSIOP_SANITIZE = 0x48
SCSIOP_PLAY_TRACK_RELATIVE = 0x49
SCSIOP_GET_EVENT_STATUS = 0x4A
SCSIOP_PAUSE_RESUME = 0x4B
SCSIOP_LOG_SELECT = 0x4C
SCSIOP_LOG_SENSE = 0x4D
SCSIOP_STOP_PLAY_SCAN = 0x4E
SCSIOP_XDWRITE = 0x50
SCSIOP_XPWRITE = 0x51
SCSIOP_READ_DISK_INFORMATION = 0x51
SCSIOP_READ_DISC_INFORMATION = 0x51
SCSIOP_READ_TRACK_INFORMATION = 0x52
SCSIOP_XDWRITE_READ = 0x53
SCSIOP_RESERVE_TRACK_RZONE = 0x53
SCSIOP_SEND_OPC_INFORMATION = 0x54
SCSIOP_MODE_SELECT10 = 0x55
SCSIOP_RESERVE_UNIT10 = 0x56
SCSIOP_RESERVE_ELEMENT = 0x56
SCSIOP_RELEASE_UNIT10 = 0x57
SCSIOP_RELEASE_ELEMENT = 0x57
SCSIOP_REPAIR_TRACK = 0x58
SCSIOP_MODE_SENSE10 = 0x5A
SCSIOP_CLOSE_TRACK_SESSION = 0x5B
SCSIOP_READ_BUFFER_CAPACITY = 0x5C
SCSIOP_SEND_CUE_SHEET = 0x5D
SCSIOP_PERSISTENT_RESERVE_IN = 0x5E
SCSIOP_PERSISTENT_RESERVE_OUT = 0x5F

# 12-byte commands
SCSIOP_REPORT_LUNS = 0xA0
SCSIOP_BLANK = 0xA1
SCSIOP_ATA_PASSTHROUGH12 = 0xA1
SCSIOP_SEND_EVENT = 0xA2
SCSIOP_SECURITY_PROTOCOL_IN = 0xA2
SCSIOP_SEND_KEY = 0xA3
SCSIOP_MAINTENANCE_IN = 0xA3
SCSIOP_REPORT_KEY = 0xA4
SCSIOP_MAINTENANCE_OUT = 0xA4
SCSIOP_MOVE_MEDIUM = 0xA5
SCSIOP_LOAD_UNLOAD_SLOT = 0xA6
SCSIOP_EXCHANGE_MEDIUM = 0xA6
SCSIOP_SET_READ_AHEAD = 0xA7
SCSIOP_MOVE_MEDIUM_ATTACHED = 0xA7
SCSIOP_READ12 = 0xA8
SCSIOP_GET_MESSAGE = 0xA8
SCSIOP_SERVICE_ACTION_OUT12 = 0xA9
SCSIOP_WRITE12 = 0xAA
SCSIOP_SEND_MESSAGE = 0xAB
SCSIOP_SERVICE_ACTION_IN12 = 0xAB
SCSIOP_GET_PERFORMANCE = 0xAC
SCSIOP_READ_DVD_STRUCTURE = 0xAD
SCSIOP_WRITE_VERIFY12 = 0xAE
SCSIOP_VERIFY12 = 0xAF
SCSIOP_SEARCH_DATA_HIGH12 = 0xB0
SCSIOP_SEARCH_DATA_EQUAL12 = 0xB1
SCSIOP_SEARCH_DATA_LOW12 = 0xB2
SCSIOP_SET_LIMITS12 = 0xB3
SCSIOP_READ_ELEMENT_STATUS_ATTACHED = 0xB4
SCSIOP_REQUEST_VOL_ELEMENT = 0xB5
SCSIOP_SECURITY_PROTOCOL_OUT = 0xB5
SCSIOP_SEND_VOLUME_TAG = 0xB6
SCSIOP_SET_STREAMING = 0xB6
SCSIOP_READ_DEFECT_DATA = 0xB7
SCSIOP_READ_ELEMENT_STATUS = 0xB8
SCSIOP_READ_CD_MSF = 0xB9
SCSIOP_SCAN_CD = 0xBA
SCSIOP_REDUNDANCY_GROUP_IN = 0xBA
SCSIOP_SET_CD_SPEED = 0xBB
SCSIOP_REDUNDANCY_GROUP_OUT = 0xBB
SCSIOP_PLAY_CD = 0xBC
SCSIOP_SPARE_IN = 0xBC
SCSIOP_MECHANISM_STATUS = 0xBD
SCSIOP_SPARE_OUT = 0xBD
SCSIOP_READ_CD = 0xBE
SCSIOP_VOLUME_SET_IN = 0xBE
SCSIOP_SEND_DVD_STRUCTURE = 0xBF
SCSIOP_VOLUME_SET_OUT = 0xBF
SCSIOP_INIT_ELEMENT_RANGE = 0xE7

# 16-byte commands
SCSIOP_XDWRITE_EXTENDED16 = 0x80
SCSIOP_WRITE_FILEMARKS16 = 0x80
SCSIOP_REBUILD16 = 0x81
SCSIOP_READ_REVERSE16 = 0x81
SCSIOP_REGENERATE16 = 0x82
SCSIOP_EXTENDED_COPY = 0x83
SCSIOP_POPULATE_TOKEN = 0x83
SCSIOP_WRITE_USING_TOKEN = 0x83
SCSIOP_RECEIVE_COPY_RESULTS = 0x84
SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION = 0x84
SCSIOP_ATA_PASSTHROUGH16 = 0x85
SCSIOP_ACCESS_CONTROL_IN = 0x86
SCSIOP_ACCESS_CONTROL_OUT = 0x87
SCSIOP_READ16 = 0x88
SCSIOP_COMPARE_AND_WRITE = 0x89
SCSIOP_WRITE16 = 0x8A
SCSIOP_READ_ATTRIBUTES = 0x8C
SCSIOP_WRITE_ATTRIBUTES = 0x8D
SCSIOP_WRITE_VERIFY16 = 0x8E
SCSIOP_VERIFY16 = 0x8F
SCSIOP_PREFETCH16 = 0x90
SCSIOP_SYNCHRONIZE_CACHE16 = 0x91
SCSIOP_SPACE16 = 0x91
SCSIOP_LOCK_UNLOCK_CACHE16 = 0x92
SCSIOP_LOCATE16 = 0x92
SCSIOP_WRITE_SAME16 = 0x93
SCSIOP_ERASE16 = 0x93
SCSIOP_ZBC_OUT = 0x94
SCSIOP_ZBC_IN = 0x95
SCSIOP_READ_DATA_BUFF16 = 0x9B
SCSIOP_READ_CAPACITY16 = 0x9E
SCSIOP_GET_LBA_STATUS = 0x9E
SCSIOP_GET_PHYSICAL_ELEMENT_STATUS = 0x9E
SCSIOP_REMOVE_ELEMENT_AND_TRUNCATE = 0x9E
SCSIOP_SERVICE_ACTION_IN16 = 0x9E
SCSIOP_SERVICE_ACTION_OUT16 = 0x9F

# 32-byte commands
SCSIOP_OPERATION32 = 0x7F

SERVICE_ACTION_OVERWRITE = 0x01
SERVICE_ACTION_BLOCK_ERASE = 0x02
SERVICE_ACTION_CRYPTO_ERASE = 0x03
SERVICE_ACTION_EXIT_FAILURE = 0x1f

SERVICE_ACTION_XDWRITE = 0x0004
SERVICE_ACTION_XPWRITE = 0x0006
SERVICE_ACTION_XDWRITEREAD = 0x0007
SERVICE_ACTION_WRITE = 0x000B
SERVICE_ACTION_WRITE_VERIFY = 0x000C
SERVICE_ACTION_WRITE_SAME = 0x000D
SERVICE_ACTION_ORWRITE = 0x000E

SERVICE_ACTION_POPULATE_TOKEN = 0x10
SERVICE_ACTION_WRITE_USING_TOKEN = 0x11

SERVICE_ACTION_RECEIVE_TOKEN_INFORMATION = 0x07

SERVICE_ACTION_CLOSE_ZONE = 0x01
SERVICE_ACTION_FINISH_ZONE = 0x02
SERVICE_ACTION_OPEN_ZONE = 0x03
SERVICE_ACTION_RESET_WRITE_POINTER = 0x04

SERVICE_ACTION_REPORT_ZONES = 0x00

REPORT_ZONES_OPTION_LIST_ALL_ZONES = 0x00
REPORT_ZONES_OPTION_LIST_EMPTY_ZONES = 0x01
REPORT_ZONES_OPTION_LIST_IMPLICITLY_OPENED_ZONES = 0x02
REPORT_ZONES_OPTION_LIST_EXPLICITLY_OPENED_ZONES = 0x03
REPORT_ZONES_OPTION_LIST_CLOSED_ZONES = 0x04
REPORT_ZONES_OPTION_LIST_FULL_ZONES = 0x05
REPORT_ZONES_OPTION_LIST_READ_ONLY_ZONES = 0x06
REPORT_ZONES_OPTION_LIST_OFFLINE_ZONES = 0x07

REPORT_ZONES_OPTION_LIST_RWP_ZONES = 0x10
REPORT_ZONES_OPTION_LIST_NON_SEQUENTIAL_WRITE_RESOURCES_ACTIVE_ZONES = 0x11

REPORT_ZONES_OPTION_LIST_NOT_WRITE_POINTER_ZONES = 0x3F

SERVICE_ACTION_READ_CAPACITY16 = 0x10
SERVICE_ACTION_GET_LBA_STATUS = 0x12
SERVICE_ACTION_GET_PHYSICAL_ELEMENT_STATUS = 0x17
SERVICE_ACTION_REMOVE_ELEMENT_AND_TRUNCATE = 0x18

SERVICE_ACTION_REPORT_TIMESTAMP = 0x0F

SERVICE_ACTION_SET_TIMESTAMP = 0x0F

CDB_RETURN_ON_COMPLETION = 0
CDB_RETURN_IMMEDIATE = 1

CDB_FORCE_MEDIA_ACCESS = 0x08

SCSIOP_DENON_EJECT_DISC = 0xE6
SCSIOP_DENON_STOP_AUDIO = 0xE7
SCSIOP_DENON_PLAY_AUDIO = 0xE8
SCSIOP_DENON_READ_TOC = 0xE9
SCSIOP_DENON_READ_SUBCODE = 0xEB

SCSIMESS_ABORT = 0x06
SCSIMESS_ABORT_WITH_TAG = 0x0D
SCSIMESS_BUS_DEVICE_RESET = 0X0C
SCSIMESS_CLEAR_QUEUE = 0X0E
SCSIMESS_COMMAND_COMPLETE = 0X00
SCSIMESS_DISCONNECT = 0X04
SCSIMESS_EXTENDED_MESSAGE = 0X01
SCSIMESS_IDENTIFY = 0X80
SCSIMESS_IDENTIFY_WITH_DISCON = 0XC0
SCSIMESS_IGNORE_WIDE_RESIDUE = 0X23
SCSIMESS_INITIATE_RECOVERY = 0X0F
SCSIMESS_INIT_DETECTED_ERROR = 0X05
SCSIMESS_LINK_CMD_COMP = 0X0A
SCSIMESS_LINK_CMD_COMP_W_FLAG = 0X0B
SCSIMESS_MESS_PARITY_ERROR = 0X09
SCSIMESS_MESSAGE_REJECT = 0X07
SCSIMESS_NO_OPERATION = 0X08
SCSIMESS_HEAD_OF_QUEUE_TAG = 0X21
SCSIMESS_ORDERED_QUEUE_TAG = 0X22
SCSIMESS_SIMPLE_QUEUE_TAG = 0X20
SCSIMESS_RELEASE_RECOVERY = 0X10
SCSIMESS_RESTORE_POINTERS = 0X03
SCSIMESS_SAVE_DATA_POINTER = 0X02
SCSIMESS_TERMINATE_IO_PROCESS = 0X11

SCSIMESS_MODIFY_DATA_POINTER = 0X00
SCSIMESS_SYNCHRONOUS_DATA_REQ = 0X01
SCSIMESS_WIDE_DATA_REQUEST = 0X03

SCSIMESS_MODIFY_DATA_LENGTH = 5
SCSIMESS_SYNCH_DATA_LENGTH = 3
SCSIMESS_WIDE_DATA_LENGTH = 2

class ATA_PASSTHROUGH12(Structure):
	__slots__ = ()
	_fields_ = [
		("OperationCode", UCHAR), # SCSIOP_ATA_PASSTHROUGH12
		("Reserved1", UCHAR, 1),
		("Protocol", UCHAR, 4),
		("MultipleCount", UCHAR, 3),
		("TLength", UCHAR, 2),
		("ByteBlock", UCHAR, 1),
		("TDir", UCHAR, 1),
		("Reserved2", UCHAR, 1),
		("CkCond", UCHAR, 1),
		("Offline", UCHAR, 2),
		("Features", UCHAR),
		("SectorCount", UCHAR),
		("LbaLow", UCHAR),
		("LbaMid", UCHAR),
		("LbaHigh", UCHAR),
		("Device", UCHAR),
		("Command", UCHAR),
		("Reserved3", UCHAR),
		("Control", UCHAR),
	]
