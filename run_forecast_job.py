#!/usr/bin/env python
# coding: utf-8

# In[2]:


# run_forecast_job.py

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import CommandJob

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="7db2b459-a548-48f4-a984-f75f5bae5548",  # Replace below
    resource_group_name="venumadhuri.y-rg",
    workspace_name="energy-ml-ws"
)

job = CommandJob(
    code="./",  # directory where energy_forecast_arima.py is located
    command="python energy_forecast_arima.py",
    environment="arima-env@latest",
    compute="arima-instance",  # name of your compute
    experiment_name="energy-forecast-arima"
)

ml_client.jobs.create_or_update(job)


# In[ ]:




