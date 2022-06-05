FROM node:16.15-alpine

WORKDIR /app

COPY yarn.lock package.json ./

RUN yarn

COPY . .

CMD ["yarn", "start"]
