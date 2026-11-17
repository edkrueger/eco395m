import csv
from pathlib import Path

from tqdm import tqdm

from database import connect

CSV_PATH = Path(__file__).parent / "reaction_counts.csv"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS reaction_counts (
	status_id TEXT PRIMARY KEY,
	status_message TEXT,
	link_name TEXT,
	status_type TEXT,
	status_link TEXT,
	status_published TIMESTAMP,
	num_reactions INTEGER,
	num_comments INTEGER,
	num_shares INTEGER,
	num_likes INTEGER,
	num_loves INTEGER,
	num_wows INTEGER,
	num_hahas INTEGER,
	num_sads INTEGER,
	num_angrys INTEGER
)
"""

INSERT_SQL = """
INSERT INTO reaction_counts (
	status_id,
	status_message,
	link_name,
	status_type,
	status_link,
	status_published,
	num_reactions,
	num_comments,
	num_shares,
	num_likes,
	num_loves,
	num_wows,
	num_hahas,
	num_sads,
	num_angrys
) VALUES (
	%(status_id)s,
	%(status_message)s,
	%(link_name)s,
	%(status_type)s,
	%(status_link)s,
	%(status_published)s,
	%(num_reactions)s,
	%(num_comments)s,
	%(num_shares)s,
	%(num_likes)s,
	%(num_loves)s,
	%(num_wows)s,
	%(num_hahas)s,
	%(num_sads)s,
	%(num_angrys)s
)
"""

INT_COLUMNS = (
	"num_reactions",
	"num_comments",
	"num_shares",
	"num_likes",
	"num_loves",
	"num_wows",
	"num_hahas",
	"num_sads",
	"num_angrys",
)


def _prepare_row(row: dict) -> dict:
	prepared = {}
	for key, value in row.items():
		if value == "":
			prepared[key] = None
		elif key in INT_COLUMNS:
			prepared[key] = int(value)
		else:
			prepared[key] = value
	return prepared


def load_reaction_counts(csv_path: Path = CSV_PATH) -> int:
	conn = connect()
	count = 0
	seen_status_ids: set[str] = set()
	try:
		with conn.cursor() as cur:
			cur.execute(CREATE_TABLE_SQL)
			cur.execute("TRUNCATE reaction_counts")
			with csv_path.open(newline="") as file:
				total_rows = max(sum(1 for _ in file) - 1, 0)
				file.seek(0)
				reader = csv.DictReader(file)
				for row in tqdm(reader, total=total_rows, desc="Loading rows"):
					status_id = row["status_id"]
					if status_id in seen_status_ids:
						continue
					seen_status_ids.add(status_id)
					cur.execute(INSERT_SQL, _prepare_row(row))
					count += 1
		conn.commit()
	except Exception:
		conn.rollback()
		raise
	finally:
		conn.close()

	return count


if __name__ == "__main__":
	n = load_reaction_counts()
	print(f"Loaded {n} rows into reaction_counts")
