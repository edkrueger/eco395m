from datetime import date
from enum import Enum

import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from psycopg2.extras import RealDictCursor

from database import ConnectionDep

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


@app.get("/db")
def db_health_check(conn: ConnectionDep):
	with conn.cursor() as cur:
		cur.execute("SELECT 1")
		result = cur.fetchone()[0]

	return JSONResponse(
		content={"message": "ok", "result": result},
		status_code=200,
	)


@app.get("/reactions")
def get_reactions(
	conn: ConnectionDep,
	start_date: date | None = None,
	end_date: date | None = None,
	status_type: list[StatusType] | None = Query(default=None),
):
	if start_date is not None and end_date is not None and start_date > end_date:
		raise HTTPException(
			status_code=400,
			detail="start_date must be on or before end_date",
		)

	params: list = []
	sql = """
		SELECT
			status_id,
			status_message,
			link_name,
			status_type,
			status_link,
			to_char(status_published, 'YYYY-MM-DD"T"HH24:MI:SS') AS status_published,
			num_reactions,
			num_comments,
			num_shares,
			num_likes,
			num_loves,
			num_wows,
			num_hahas,
			num_sads,
			num_angrys
		FROM reaction_counts
		WHERE 1=1
	"""

	if start_date is not None:
		sql += " AND status_published::date >= %s"
		params.append(start_date)
	if end_date is not None:
		sql += " AND status_published::date <= %s"
		params.append(end_date)
	if status_type is not None:
		sql += " AND status_type = ANY(%s)"
		params.append([t.value for t in status_type])


	with conn.cursor(cursor_factory=RealDictCursor) as cur:
		cur.execute(sql, params)
		return cur.fetchall()


if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)
