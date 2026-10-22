"""MCP server for the same reaction-counts data as class-topics/python_api.

    python class-topics/python_mcp/main.py
"""

from datetime import date
from enum import Enum
from pathlib import Path

import pandas as pd
from fastmcp import FastMCP

CSV_PATH = Path(__file__).parent / "reaction_counts.csv"

df = (
	pd.read_csv(CSV_PATH)
	.assign(status_published=lambda df_: pd.to_datetime(df_["status_published"]))
)

mcp = FastMCP("reaction-counts")


class StatusType(str, Enum):
	photo = "photo"
	video = "video"
	link = "link"
	status = "status"
	event = "event"


@mcp.tool
def health_check() -> dict:
	"""Check that the reaction-counts server is running."""
	return {"message": "ok"}


@mcp.tool
def get_reactions(
	start_date: date | None = None,
	end_date: date | None = None,
	status_type: list[StatusType] | None = None,
) -> list[dict]:
	"""Return Facebook post reaction counts, optionally filtered by date and status type.

	Dates are inclusive and use YYYY-MM-DD. status_type may include any of:
	photo, video, link, status, event.
	"""
	if start_date is not None and end_date is not None and start_date > end_date:
		raise ValueError("start_date must be on or before end_date")

	filtered = df

	if start_date is not None:
		filtered = filtered[filtered["status_published"].dt.date >= start_date]
	if end_date is not None:
		filtered = filtered[filtered["status_published"].dt.date <= end_date]
	if status_type is not None:
		allowed = {t.value for t in status_type}
		filtered = filtered[filtered["status_type"].isin(allowed)]

	out = filtered.copy()
	out["status_published"] = out["status_published"].dt.strftime("%Y-%m-%dT%H:%M:%S")
	records = out.astype(object).where(pd.notnull(out), None).to_dict(orient="records")

	return records


if __name__ == "__main__":
	mcp.run(transport="http", host="127.0.0.1", port=8888)
