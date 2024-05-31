# Start with the Alpine base image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Copy the config.txt file to the container
COPY config.txt /app/config.txt

# Specify a default command
CMD echo "Container started. Config file and curl are ready to use."
