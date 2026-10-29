from dataclasses import dataclass


@dataclass
class DebugConfig:
    enabled: bool = True

    log_chat_id: int = 0  # TODO: Commercial logic

    topic_errors: int = 462677 # DEBUG ERROR 
    topic_slow_updates: int = 441146 # DEBUG
    topic_slow_db: int = 462730 # DEBUG DB
    topic_summary: int = 462652 # DEBUG SUMMARY
    topic_warnings: int = 462705 # DEBUG WARNINGS
    topic_minor: int = 466000  # DEBUG MINOR

    slow_update_ms: float = 1000.0
    slow_db_ms: float = 300.0
    slow_db_acquire_ms: float = 200.0

    flush_summary_every_sec: int = 600
    queue_maxsize: int = 1000