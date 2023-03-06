# dbt-databricks-demo

## Prerequisites

    - pyenv + poetry

## How to use it:
Create virtual environment with dependencies needed for testing dbt in locally.

```sh 
poetry install
```

Only if creating new project, skip otherwise:
```sh
poetry run dbt init
```

Follow the prompts and select required options to build your dbt project.
You'll be required to setup your ~/.dbt/profiles.yml - file contains credentials for your Databricks SQL warehouse connection.

If your project already exists and your ~/.dbt/profiles.yml file has been configured you can execute dbt commands against selected profile.

```sh
cd demo && poetry run dbt debug
```

-----
