FROM node:25-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

VOLUME /app

COPY . .

CMD ["npm", "run", "build"]