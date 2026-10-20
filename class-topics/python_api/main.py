from datetime import date
from enum import Enum
from pathlib import Path

import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

CSV_PATH = Path(__file__).parent / "reaction_counts.csv"

df = (
	pd.read_csv(CSV_PATH)
	.assign(status_published=lambda df_: pd.to_datetime(df_["status_published"]))
)

app = FastAPI()


class StatusType(str, Enum):
	photo = "photo"
	video = "video"
	link = "link"
	status = "status"
	event = "event"


@app.get("/")
def health_check():
	return JSONResponse(
		content={"message": "ok"},
		status_code=200,
	)


@app.get("/reactions")
def get_reactions(
	start_date: date | None = None,
	end_date: date | None = None,
	status_type: list[StatusType] | None = Query(default=None),
):
	if start_date is not None and end_date is not None and start_date > end_date:
		raise HTTPException(
			status_code=400,
			detail="start_date must be on or before end_date",
		)

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
	uvicorn.run(app, host="127.0.0.1", port=8000)
