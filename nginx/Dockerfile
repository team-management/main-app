# Use the Nginx image
FROM nginx

# Nginx will listen on this port
EXPOSE 80

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/