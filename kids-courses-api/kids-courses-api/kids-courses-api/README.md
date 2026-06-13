# Kids Courses API

This project is a GraphQL API for managing kids' courses and user accounts, built using Python with the Strawberry GraphQL library and MongoDB as the database.

## Features

- **Courses Management**: 
  - Query to list courses
  - Mutation to create and update courses

- **User Account Management**: 
  - Create, update, and delete user accounts
  - User types include students, teachers, and admins

## Project Structure

```
kids-courses-api
├── src
│   ├── app.py            # Entry point of the application
│   ├── database.py       # MongoDB database connection handling
│   ├── models.py         # Data models for courses and users
│   ├── schema.py         # GraphQL schema definition
│   ├── types.py          # GraphQL types for courses and users
│   └── resolvers
│       ├── courses.py    # Resolvers for course-related queries and mutations
│       └── users.py      # Resolvers for user account-related queries and mutations
├── tests
│   ├── test_courses.py    # Unit tests for course functionality
│   └── test_users.py      # Unit tests for user account functionality
├── pyproject.toml         # Project configuration and dependencies
├── .gitignore             # Files and directories to ignore in version control
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kids-courses-api
   ```

2. Install dependencies:
   ```
   uvicorn src/app:app --reload
   ```

3. Start the server:
   ```
   uvicorn src/app:app --host 0.0.0.0 --port 8000
   ```

## API Endpoints

- **Courses**
  - `GET /graphql`: Query to list courses
  - `POST /graphql`: Mutation to create or update courses

- **User Accounts**
  - `POST /graphql`: Mutation to create, update, or delete user accounts

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.