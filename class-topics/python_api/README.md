# Reaction counts API

FastAPI service that serves `reaction_counts.csv`. The container listens on port **8000**.

## Deploy to Cloud Run

From this directory:

```bash
gcloud run deploy reaction-counts \
  --source . \
  --region us-central1 \
  --port 8000 \
  --allow-unauthenticated
```

`--source .` builds the Dockerfile with Cloud Build and deploys the image. `--port 8000` matches the port in the Dockerfile. If `gcloud` has no project set, add `--project YOUR_PROJECT_ID`.

## Who can call it

No IP addresses are whitelisted. `--allow-unauthenticated` makes the service public, so any address on the internet can call it. Cloud Run does not filter by client IP unless something like Cloud Armor is added in front of the service.
