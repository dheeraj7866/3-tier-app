FROM node:14

WORKDIR /app

COPY package.json ./
RUN npm install
RUN apt-get update && apt-get install curl -y
RUN npm install prom-client  

COPY server.js .

CMD ["node", "server.js"]
