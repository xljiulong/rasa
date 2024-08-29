# FROM harbor.spdiotdev.tech/docker/ubuntu:20.04
FROM rasa-dev:0.0.1


# env http_proxy "http://192.168.200.26:51837"
# env https_proxy "http://192.168.200.26:51837"

# ENV HOME=/workspace
ENV DEBIAN_FRONTEND=noninteractive


# # update permissions & change user to not run as root
WORKDIR /workspace

# # copy files
# COPY . /build/

# # change working directory
# WORKDIR /build


# install dependencies
# RUN python -m venv /opt/venv && \
#   . /opt/venv/bin/activate && \
#   pip install --no-cache-dir -U "pip==22.*" -U "wheel>0.38.0" && \
#   poetry config installer.max-workers 10 && \
#   poetry install --no-dev --no-root --no-interaction && \
#   poetry build -f wheel -n && \
#   pip install --no-deps dist/*.whl && \
#   rm -rf dist *.egg-info

# # start a new build stage
# FROM ${IMAGE_BASE_NAME}:base-${BASE_IMAGE_HASH} as runner

# # copy everything from /opt
# COPY --from=builder /opt/venv /opt/venv

# # make sure we use the virtualenv
# ENV PATH="/opt/venv/bin:$PATH"

# # set HOME environment variable
# ENV HOME=/app

# # update permissions & change user to not run as root
# WORKDIR /app
# RUN chgrp -R 0 /app && chmod -R g=u /app && chmod o+wr /app
# USER 1001

# # create a volume for temporary data
# VOLUME /tmp

# # change shell
# SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# # the entry point
# EXPOSE 5005
# ENTRYPOINT ["rasa"]
# CMD ["--help"]
