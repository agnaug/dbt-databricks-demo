# Databricks notebook source
import os

env_vars = ["DBT_ACCESS_TOKEN", "PAT_TOKEN", "DBT_WAREHOUSE_ID", "DBT_HOST"]
for env_var in env_vars:
    print(env_var, os.environ.get(env_var))

# The "DBT_WAREHOUSE_ID", "DBT_HOST", "DBT_ACCESS_TOKEN" get revoked as soon as dbt task finishes
# However it does not try to overwrite it with any other value