# Instalily Case Study Backend

## Tech Stack

- FastAPI Framework
- Redis Database

The backend uses OpenAI gpt-4o model to generate responses through prompt engineering. Cookies are saved in the extension through chrome and retrieved from the backend in order to save the user's session data (previous chat history) in the Redis database. Redis caches the session data for 10 minutes before expiring the session.
