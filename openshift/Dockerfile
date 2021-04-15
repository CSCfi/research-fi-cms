FROM registry.access.redhat.com/ubi8/python-38

# Add application sources to a directory that the assemble script expects them
# and set permissions so that the container runs without root access

ENV APP_MODULE=cms.wsgi:application
ENV DISABLE_COLLECTSTATIC=true

USER 0

# Install PostgreSQL client
RUN yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
RUN yum install -y postgresql96

ADD django /tmp/src
# RUN rm -f /tmp/src/cms/local_settings.py
RUN chown -R 1001:0 /tmp/src
USER 1001
# Install the dependencies
RUN /usr/libexec/s2i/assemble
# Set the default command for the resulting image
CMD /usr/libexec/s2i/run