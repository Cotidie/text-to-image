FROM node:25-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

VOLUME /app

CMD ["npm", "run", "build"]