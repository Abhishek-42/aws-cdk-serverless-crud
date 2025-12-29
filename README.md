# Task Management CRUD API

A serverless task management API built with AWS CDK, Lambda, DynamoDB, and API Gateway. This project demonstrates a complete CRUD (Create, Read, Update, Delete) application using AWS services.

## 🚀 Features

- **Create Tasks** - Add new tasks with title and category
- **Read Tasks** - Get all tasks from the database
- **Update Tasks** - Modify task title and status
- **Delete Tasks** - Remove tasks from the database
- **Serverless Architecture** - No server management required
- **RESTful API** - Standard HTTP methods and responses

## 🏗️ Architecture

```
API Gateway → Lambda Function → DynamoDB Table
```

- **API Gateway**: Handles HTTP requests and routing
- **Lambda Function**: Processes business logic for CRUD operations
- **DynamoDB**: NoSQL database for storing task data

## 📋 API Endpoints

### Create Task
```http
POST /tasks
Content-Type: application/json

{
  "title": "Buy groceries",
  "category": "shopping"
}
```

**Response:**
```json
{
  "task_id": "abc-123-def-456",
  "title": "Buy groceries",
  "category": "shopping",
  "status": "pending"
}
```

### Get All Tasks
```http
GET /tasks
```

**Response:**
```json
[
  {
    "task_id": "abc-123-def-456",
    "title": "Buy groceries",
    "category": "shopping",
    "status": "pending"
  }
]
```

### Update Task
```http
PUT /tasks/{id}
Content-Type: application/json

{
  "task_id": "abc-123-def-456",
  "title": "Buy organic groceries",
  "status": "completed"
}
```

**Response:**
```json
{
  "task_id": "abc-123-def-456",
  "title": "Buy organic groceries",
  "status": "completed"
}
```

### Delete Task
```http
DELETE /tasks/{id}
Content-Type: application/json

{
  "task_id": "abc-123-def-456"
}
```

**Response:**
```json
{
  "task_id": "abc-123-def-456"
}
```

## 🧪 Testing the API

### Using curl

**Create a task:**
```bash
curl -X POST https://your-api-url/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn AWS", "category": "education"}'
```

**Get all tasks:**
```bash
curl -X GET https://your-api-url/tasks
```

**Update a task:**
```bash
curl -X PUT https://your-api-url/tasks/123 \
  -H "Content-Type: application/json" \
  -d '{"task_id": "your-task-id", "title": "Master AWS", "status": "completed"}'
```

**Delete a task:**
```bash
curl -X DELETE https://your-api-url/tasks/123 \
  -H "Content-Type: application/json" \
  -d '{"task_id": "your-task-id"}'
```

### Using Postman

1. Import the API endpoints into Postman
2. Set the base URL to your deployed API Gateway URL
3. Add `Content-Type: application/json` header
4. Test each endpoint with the JSON payloads shown above

## 🛠️ Local Development

### Prerequisites
- Python 3.10+
- AWS CDK CLI
- AWS CLI configured with credentials

### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd test_project1

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Deploy to AWS
```bash
# Bootstrap CDK (first time only)
cdk bootstrap

# Deploy the stack
cdk deploy

# Get the API Gateway URL from the output
```

### Local Testing
```bash
# Synthesize CloudFormation template
cdk synth

# Run tests
python -m pytest tests/
```

## 📁 Project Structure

```
test_project1/
├── lambda/
│   └── handler.py          # Lambda function code
├── test_project1/
│   └── test_project1_stack.py  # CDK stack definition
├── tests/                  # Unit tests
├── app.py                  # CDK app entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

The application uses environment variables for configuration:
- `TABLE_NAME`: DynamoDB table name (set automatically by CDK)

## 📊 Data Model

Each task has the following structure:
```json
{
  "task_id": "string (UUID)",
  "title": "string (required)",
  "category": "string (default: 'general')",
  "status": "string (default: 'pending')"
}
```

## 🚀 Deployment

This project uses AWS CDK for infrastructure as code. The stack creates:
- DynamoDB table for task storage
- Lambda function for business logic
- API Gateway for HTTP endpoints
- IAM roles and policies for security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational purposes.

## 🎯 Learning Objectives

This project demonstrates:
- Serverless architecture patterns
- RESTful API design
- AWS service integration
- Infrastructure as Code with CDK
- NoSQL database operations
- HTTP request/response handling