from pathlib import Path

from dagster import (
    asset,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    graph_asset,
    link_code_references_to_git,
    load_assets_from_package_module,
    op,
    with_source_code_references,
)
from dagster._core.definitions.metadata.source_code import AnchorBasedFilePathMapping

daily_refresh_schedule = ScheduleDefinition(
    job=define_asset_job(name="all_assets_job"), cron_schedule="0 0 * * *"
)


@op
def foo_op():
    return 5


@graph_asset
def my_asset():
    return foo_op()

@asset(aslkdjaskld=5)
def broken_asset():
    return 1

defs = Definitions(
    assets=[broken_asset],
    schedules=[daily_refresh_schedule],
)
