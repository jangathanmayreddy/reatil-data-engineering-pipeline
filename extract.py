# Data Model

## Staging Tables

### stg_customers
Raw customer information after basic cleaning.

### stg_products
Raw product information after standardization.

### stg_orders
Order-level transaction data with calculated sales amount.

## Analytics Tables

### dim_customers
Customer dimension containing customer profile and region.

### dim_products
Product dimension containing product category details.

### fact_sales
Sales fact table at order-line grain. Supports reporting by date, customer, product, region, and category.

## Grain

Each row in `fact_sales` represents one order transaction.

## Important Metrics

- Total revenue: SUM(sales_amount)
- Total orders: COUNT(order_id)
- Average order value: SUM(sales_amount) / COUNT(order_id)
- Units sold: SUM(quantity)
