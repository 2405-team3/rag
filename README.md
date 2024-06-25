# Create environment variable file for API key

`cd server`
`touch .env`
`nano .env`
paste in `OPENAI_API_KEY=<your-api-key>`

# Install dependencies and run dev environment

```
cd client
npm install
npm run dev
```

```
cd server
pipenv install
pipenv shell
fastapi dev main.py
```
