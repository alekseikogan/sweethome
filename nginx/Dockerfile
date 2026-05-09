FROM nginx:1.27-alpine

RUN apk add --no-cache bash openssl

COPY nginx/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
