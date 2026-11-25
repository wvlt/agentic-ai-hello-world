# Setup Checklist (5 minutes)

Do this once before Video 01.

## 1. A Databricks workspace
You need a workspace where you can create notebooks. A free or trial workspace works.

## 2. Get the course into your workspace
1. In Databricks, go to **Workspace**, then your home folder.
2. Click **Create**, then **Git folder**.
3. Paste the repository URL: `https://github.com/wvlt/agentic-ai-hello-world` and click **Create Git folder**.
4. Open `videos/01-what-is-an-agent/notebooks/01-hello-llm`.

## 3. Compute
Attach the notebook to **Serverless** (recommended) or any cluster running a recent Databricks Runtime. The libraries used (`databricks-sdk`, `openai`, `mlflow`) come pre-installed.

## 4. Model access
The series uses Databricks-hosted models (Foundation Model APIs). No external API keys are needed.

1. In the left sidebar, click **Serving**.
2. Check that `databricks-meta-llama-3-3-70b-instruct` is listed and shows **Ready**.
3. Optional: also check `databricks-claude-haiku-4-5` - Video 01 compares two models.

If a model is missing, ask your workspace admin to enable Foundation Model APIs, or change the `MODEL` variable in the notebook to any chat model listed under **Serving**.

## 5. Quick test
Run the first two code cells of the Video 01 notebook. If you see a reply from the model, you are ready.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: openai` | Old runtime | Use Serverless, or run `%pip install openai` in the first cell |
| `ENDPOINT_NOT_FOUND` or 404 | Model not available in your workspace | Pick another chat model from **Serving** and update `MODEL` |
| `PERMISSION_DENIED` or 403 | No permission to query the endpoint | Ask your admin for **Can Query** on the endpoint |
| `429 Too Many Requests` | Rate limit | Wait a few seconds and run the cell again |
