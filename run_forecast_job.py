from azure.ai.ml import MLClient, command
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="7db2b459-a548-48f4-a984-f75f5bae5548",
    resource_group_name="venumadhuri.y-rg",
    workspace_name="energy-ml-ws"
)

env = Environment(
    name="arima-env",
    conda_file="environment.yml",
    image="mcr.microsoft.com/azureml/base:latest",
    description="ARIMA forecasting environment"
)

env = ml_client.environments.create_or_update(env)

job = command(
    code="./",
    command="python energy_forecast_arima.py > output.log 2>&1",
    environment=f"{env.name}:{env.version}",
    compute="arima-instance",
    display_name="arima_forecast_job"
)

created_job = ml_client.jobs.create_or_update(job)
print(f"Job submitted: {created_job.name}, status: {created_job.status}")
