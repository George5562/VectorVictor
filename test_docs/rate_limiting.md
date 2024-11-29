# Rate Limiting Implementation

Technical documentation for the API rate limiting system.

## Overview

This document details the implementation of our rate limiting system that protects API endpoints from abuse.

## Implementation

The rate limiter uses Redis to track request counts with a sliding window algorithm:

```python
import redis
from datetime import datetime

class RateLimiter:
    def __init__(self):
        self.redis = redis.Redis()
        
    def check_limit(self, user_id: str, window_seconds: int = 3600) -> bool:
        key = f"rate_limit:{user_id}"
        current_time = datetime.now().timestamp()
        
        # Clean old requests
        self.redis.zremrangebyscore(key, 0, current_time - window_seconds)
        
        # Check current count
        count = self.redis.zcard(key)
        if count >= MAX_REQUESTS:
            return False
            
        # Add new request
        self.redis.zadd(key, {str(current_time): current_time})
        return True
```

## Configuration

Rate limits are applied differently based on endpoint and user role:
- Authentication endpoints: 5 requests per minute
- User management endpoints: 30 requests per minute
- Regular API endpoints: 100 requests per minute

## Dependencies

- Redis for request tracking
- Authentication system for user identification
- Middleware system for request interception

## Related Documentation

- Authentication API (for user identification)
- User Management API (for role-based limits)
- Redis Configuration Guide
