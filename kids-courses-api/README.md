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
   ```bash
   git clone <repository-url>
   cd kids-courses-api
   ```

2. Install dependencies with `uv`:
   ```bash
   uv sync
   ```

3. Start the server with `uv`:
   ```bash
   uv run uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```

## GraphQL Endpoint

- `POST /graphql`

The GraphQL schema exposes:

- `listCourses` query
- `createCourse` mutation
- `updateCourse` mutation
- `users` query
- `createUser` mutation
- `updateUser` mutation
- `deleteUser` mutation

## Example Queries

List courses:
```graphql
query {
  listCourses {
    id
    title
    description
    teacherId
  }
}
```

Create a course:
```graphql
mutation {
  createCourse(title: "Math Basics", description: "Introductory math course", teacherId: "000000000000000000000000") {
    id
    title
    description
    teacherId
  }
}
```

Create a user:
```graphql
mutation {
  createUser(username: "student1", email: "student1@example.com", role: "student") {
    id
    username
    email
    role
  }
}
```

Update a user:
```graphql
mutation {
  updateUser(id: "000000000000000000000000", username: "student2", email: "student2@example.com") {
    id
    username
    email
    role
  }
}
```

Delete a user:
```graphql
mutation {
  deleteUser(id: "000000000000000000000000") {
    id
    username
    email
    role
  }
}
```

Track course progress:
```graphql
mutation {
  createCourseProgress(userId: "000000000000000000000000", courseId: "000000000000000000000000", currentCourseContentId: "000000000000000000000001") {
    id
    userId
    courseId
    currentCourseContentId
  }
}
```

Update course progress:
```graphql
mutation {
  updateCourseProgress(id: "000000000000000000000001", currentCourseContentId: "000000000000000000000002") {
    id
    userId
    courseId
    currentCourseContentId
  }
}
```

Course ratings:
```graphql
mutation {
  createCourseRating(courseId: "000000000000000000000000", authorId: "000000000000000000000000", rating: 5) {
    id
    courseId
    authorId
    rating
  }
}
```

List ratings for a course:
```graphql
query {
  courseRatings(courseId: "000000000000000000000000") {
    id
    courseId
    authorId
    rating
  }
}
```

## Testing

Install test dependencies and run:
```bash
uv sync --dev
pytest
```

## License

This project is licensed under the MIT License.