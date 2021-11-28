from enum import Enum


class SessionType(Enum):
    ACTIVE = 0
    SCREEN_OFF = 1
    SLEEP = 2
    STANDBY = 3
    HYBRID_SLEEP = 4
    HIBERNATE = 5
    HYBRID_SHUTDOWN = 6
    SHUTDOWN = 7
    SYSTEM_SLEEP_TRANSITION_UNKNOWN_TYPE = 8
    ABNORMAL_SHUTDOWN = 9
    BUGCHECK = 10
    REPORT_GENERATED = 11
