FROM node:latest

# set environment variable
ENV NODE_ENV development

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package*.json ./
COPY app.js ./

#RUN npm install

EXPOSE 3000

#CMD ["npm", "start"]
