{% macro discount_calculator(price, old_price, decimal_places=2) -%}
ROUND((({{ old_price }} - {{ price }}) / {{ old_price }}) * 100, {{ decimal_places }})
{%- endmacro %}
