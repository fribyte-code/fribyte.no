FROM alpine as build-stage

WORKDIR /home/site
COPY . .

RUN apk add zola --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
  && zola build


FROM lipanski/docker-static-website:latest
EXPOSE 3000
COPY --from=build-stage /home/site/public/ /home/static/
CMD ["/thttpd", "-D", "-h", "0.0.0.0", "-p", "3000", "-d", "/home/static", "-u", "static", "-l", "-", "-M", "60"]
