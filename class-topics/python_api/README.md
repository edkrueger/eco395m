# Reaction counts API

FastAPI service that queries the `reaction_counts` Postgres table. The container listens on port **8000**.

## Local setup

1. Copy credentials into `.env` in this directory:

```env
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
DATABASE_DATABASE=postgres
```

2. Install deps and load the CSV into Postgres:

```bash
pip install -r requirements.txt
python loader.py
```

3. Run the API:

```bash
python main.py
```

## Deploy to Cloud Run

`.env` is not included in the Docker image. Point Cloud Run at your local `.env` with `--env-vars-file` so those values are set on the service.

From this directory:

```bash
gcloud run deploy reaction-counts \
  --source . \
  --region us-central1 \
  --port 8000 \
  --allow-unauthenticated \
  --env-vars-file .env
```

`--env-vars-file` accepts a `.env` or YAML file and replaces the service's existing env vars with the ones in that file. `--source .` builds the Dockerfile with Cloud Build and deploys the image. `--port 8000` matches the port in the Dockerfile. If `gcloud` has no project set, add `--project YOUR_PROJECT_ID`.

Make sure Cloud Run can reach the database:

- Whitelist Cloud Run egress / use `0.0.0.0/0` on Cloud SQL authorized networks for a quick class demo, or
- Prefer a private path (Cloud SQL Auth Proxy / VPC connector) for anything beyond a demo.

Load data before or after deploy by running `python loader.py` against the same database from a machine that can reach it.

## Who can call it

No IP addresses are whitelisted. `--allow-unauthenticated` makes the service public, so any address on the internet can call it. Cloud Run does not filter by client IP unless something like Cloud Armor is added in front of the service.
