FROM node:25-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

VOLUME /app/dist

CMD ["npm", "run", "build"]