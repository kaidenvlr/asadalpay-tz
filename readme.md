
# Asadal Pay Test Work

Test work goal: create a frontend view for AsadalPay payment system.

Telegram bot: https://t.me/asadal_pay_tz_bot

## Getting Started

### Make will help you
To build, up, test, create and apply migration use:

```bash
  make help
```
and you receive this
```bash
bot                  Run bot
build                Build project with compose
help                 Show this help
migrate-apply        apply alembic migrations to database/schema
migrate-create       Create new alembic database migration aka database revision.
test                 Run project tests
up                   Run project with compose
```

### Build and Run project
To build and up project use
```bash
make build
make up
```
In another terminal you should use
```bash
make bot
```

### Test API
To test project use
```bash
make test
```

## API Reference

### Documentation
Documentation is available by these endpoints:
```http
/docs
```
```http
/redoc
```

### Items

#### Get item

```http
  GET /api/v1/item/${item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id` | `int`    | **Required**. Id of item to fetch |


#### Create item

```http
  POST /api/v1/item
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | **Required**. Title of item       |
| `price`   | `float`  | **Required**. Price of item       |


#### Update item

```http
  PATCH /api/v1/item/${item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id` | `int`    | **Required**. Id of item to update|
| `title`   | `string` | **Required** New title of item    |
| `price`   | `string` | **Required** New price of item    |


#### Delete item

```http
  DELETE /api/v1/item/${item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id` | `int`    | **Required**. Id of item to delete|


### Orders

#### Get order

```http
  GET /api/v1/order/${order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`| `int`    | **Required**. Id of order to fetch|


#### Create order

```http
  POST /api/v1/order
```

| Parameter    | Type            | Description                         |
| :--------    | :-------        | :--------------------------------   |
| `telegram_id`| `string`        | **Required**. User ID in Telegram   |
|`order_items` |`list<OrderItem>`| **Required**. List of Ordered Items |

##### Order Item Schema

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id` | `int`    | **Required**. Id of item          |
|`quantity` |`int`     | **Required** Quantity of item     |


#### Change order status

```http
  PATCH /api/v1/order/${order_id}
```

| Parameter | Type     | Description                               |
| :-------- | :------- | :--------------------------------         |
| `order_id`| `int`    | **Required**. Id of order to change status|


#### Check payment status

```http
  GET /api/v1/order/check-payment/${order_id}
```

| Parameter | Type     | Description                                      |
| :-------- | :------- | :--------------------------------                |
| `order_id`| `int`    | **Required**. Id of order to check payment status|


#### Get orders by Telegram ID

```http
  GET /api/v1/order/all/${telegram_id}
```

| Parameter    | Type     | Description                               |
| :--------    | :------- | :--------------------------------         |
| `telegram_id`| `str`    | **Required**. Telegram ID to get orders   |
