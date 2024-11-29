# User Management API

This document describes the user management endpoints for creating, updating, and managing user accounts.

## Overview

The User Management API provides endpoints for managing user accounts, profiles, and permissions. This API works in conjunction with the Authentication API for secure access control.

## Endpoints

### POST /users/create

Creates a new user account.

```python
import requests

response = requests.post('/users/create', json={
    'username': 'new_user@example.com',
    'password': 'secure_password',
    'role': 'user'
})
user = response.json()['user']
```

### PUT /users/{user_id}

Updates user profile information.

## Security

- All endpoints require authentication via JWT
- Admin role required for certain operations
- Password hashing using bcrypt

## Related Topics

- Authentication system
- Role-based access control
- User profile management
