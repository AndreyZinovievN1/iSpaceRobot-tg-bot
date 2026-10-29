from contextvars import ContextVar

trace_id_var = ContextVar("trace_id", default=None)
event_name_var = ContextVar("event_name", default=None)
user_id_var = ContextVar("user_id", default=None)
chat_id_var = ContextVar("chat_id", default=None)
