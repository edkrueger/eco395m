from collections.abc import Iterator
from typing import Annotated

import psycopg2
from fastapi import Depends
from psycopg2.extensions import connection as Connection

from config import (
	DATABASE_DATABASE,
	DATABASE_HOST,
	DATABASE_PASSWORD,
	DATABASE_PORT,
	DATABASE_USERNAME,
)


def connect() -> Connection:
	return psycopg2.connect(
		user=DATABASE_USERNAME,
		password=DATABASE_PASSWORD,
		host=DATABASE_HOST,
		port=DATABASE_PORT,
		dbname=DATABASE_DATABASE,
	)


def get_connection() -> Iterator[Connection]:
	conn = connect()
	try:
		yield conn
	except Exception:
		conn.rollback()
		raise
	else:
		conn.commit()
	finally:
		conn.close()


ConnectionDep = Annotated[Connection, Depends(get_connection)]
