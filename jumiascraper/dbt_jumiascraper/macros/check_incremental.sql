{% macro check_incremental(column_name) -%}
{% if is_incremental() %}
-- this filter will only be applied on an incremental run
WHERE {{ column_name }} NOT IN (SELECT {{ column_name }} FROM {{ this }}) 
{% endif %}
{%- endmacro %}
