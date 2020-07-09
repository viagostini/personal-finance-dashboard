# Finance Dashboard

Each user can have many accounts (credit cards, cash, etc) and
transactions can be registered in accounts.

Transactions can be expenses (online purchases, bills, wire transfers, etc)
or earnings (salary, wire transfers, etc).

Each user has a dashboard to visualize his spendings/earnings for a
certain time period (annualy, monthly, weekly) with filtering options
for accounts and/or types of transactions.



## Models

### User
  - ID (unique)
  - Email (unique)
  - Password (hashed)
  - Accounts
  - Transactions (that also belong to Accounts)

### Account
  - ID (unique)
  - Name (unique between same User)
  - Transactions
  - User ID (Account owner)

### Transaction
  - ID (unique)
  - Date
  - Name (required)
  - Description (optional)
  - Type (earning/expense) (required)
  - Category (default: 'Other')
  - Value (required)