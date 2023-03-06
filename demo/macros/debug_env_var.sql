{%macro debug_env_var(variable_name) %}
    {{ log("Variable Name: " ~ variable_name, True) }}
    {{ log("Variable Value: ") ~ env_var(variable_name), True }}
{% endmacro %}