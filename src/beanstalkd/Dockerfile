FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
        beanstalkd \
    && rm -rf /var/lib/apt/lists/

VOLUME ["/data"]
EXPOSE 11300
CMD ["/usr/bin/beanstalkd", "-f", "60000", "-l", "0.0.0.0", "-p", "11300", "-b", "/data"]
