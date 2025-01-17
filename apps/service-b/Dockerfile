FROM node:14

WORKDIR /app

COPY package.json ./
RUN npm install
RUN apt-get update && apt-get install curl -y

COPY server.js .

CMD ["node", "server.js"]
