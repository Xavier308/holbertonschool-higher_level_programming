# Use an Alpine Linux as the base image
FROM alpine:latest

# Create a mount point for the volume
VOLUME /data

# The default command keeps the container running
CMD ["sh", "-c", "echo Hello, Docker Volumes! && exec tail -f /dev/null"]
