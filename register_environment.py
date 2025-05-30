#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# register_environment.py

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="7db2b459-a548-48f4-a984-f75f5bae5548",
    resource_group_name="venumadhuri.y-rg",
    workspace_name="energy-ml-ws"
)

arima_env = Environment(
    name="arima-env",
    description="Environment for ARIMA time series forecasting",
    conda_file="environment.yml",  # This should already exist in your project directory
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
)

ml_client.environments.create_or_update(arima_env)

