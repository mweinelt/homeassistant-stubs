from . import Recorder as Recorder
from .const import MAX_ROWS_TO_PURGE as MAX_ROWS_TO_PURGE
from .models import Events as Events, RecorderRuns as RecorderRuns, States as States
from .repack import repack_database as repack_database
from .util import retryable_database_job as retryable_database_job, session_scope as session_scope
from collections.abc import Callable as Callable
from datetime import datetime
from sqlalchemy.orm.session import Session as Session
from typing import Any

_LOGGER: Any

def purge_old_data(instance: Recorder, purge_before: datetime, repack: bool, apply_filter: bool = ...) -> bool: ...
def _select_event_ids_to_purge(session: Session, purge_before: datetime) -> list[int]: ...
def _select_state_ids_to_purge(session: Session, purge_before: datetime, event_ids: list[int]) -> set[int]: ...
def _purge_state_ids(instance: Recorder, session: Session, state_ids: set[int]) -> None: ...
def _evict_purged_states_from_old_states_cache(instance: Recorder, purged_state_ids: set[int]) -> None: ...
def _purge_event_ids(session: Session, event_ids: list[int]) -> None: ...
def _purge_old_recorder_runs(instance: Recorder, session: Session, purge_before: datetime) -> None: ...
def _purge_filtered_data(instance: Recorder, session: Session) -> bool: ...
def _purge_filtered_states(instance: Recorder, session: Session, excluded_entity_ids: list[str]) -> None: ...
def _purge_filtered_events(instance: Recorder, session: Session, excluded_event_types: list[str]) -> None: ...
def purge_entity_data(instance: Recorder, entity_filter: Callable[[str], bool]) -> bool: ...
