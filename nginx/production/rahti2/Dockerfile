# Copyright 2020 Ministry of Education and Culture, Finland
#
# :author: CSC - IT Center for Science Ltd., Espoo Finland servicedesk@csc.fi
# :license: MIT

# Use non-root version of nginx
FROM image-registry.openshift-image-registry.svc:5000/researchfi-production/nginx-unprivileged:latest
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080