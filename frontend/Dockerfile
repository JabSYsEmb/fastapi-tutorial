FROM node:bullseye-slim as builder

WORKDIR /tmp/node/

COPY package*.json .

RUN npm install -f

FROM node:lts-alpine3.17 

WORKDIR /usr/src/app

COPY --from=builder /tmp/node/node_modules /usr/src/app/node_modules

EXPOSE 3000

CMD ["npm", "start"]
