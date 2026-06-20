DROP TABLE IF EXISTS dim_customers;

CREATE TABLE dim_customers AS
SELECT
    customer_id,
    customer_name,
    email,
    region
FROM stg_customers;
