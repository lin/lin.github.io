## Docker

1. database and app should be treat separately.
1. app install ruby rails node yarn gems
1. ssh git should be handle differently.
1. ruby rails node yarn

```dockerfile
###=============
# RUBY AND NODE
###=============
ARG RUBY_VERSION=3.3.0
FROM registry.docker.com/library/ruby:$RUBY_VERSION-slim

# Rails app lives here
WORKDIR /rails

# Set production environment
ENV RAILS_ENV="production" \
    BUNDLE_DEPLOYMENT="1" \
    BUNDLE_PATH="/usr/local/bundle" \
    BUNDLE_WITHOUT="development"

# Install packages needed to build gems and node modules
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y build-essential curl git libpq-dev libvips node-gyp pkg-config python

# Install JavaScript dependencies
ARG NODE_VERSION=14.15.1
ARG YARN_VERSION=1.22.17
ENV PATH=/usr/local/node/bin:$PATH
RUN curl -sL https://github.com/nodenv/node-build/archive/master.tar.gz | tar xz -C /tmp/ && \
    /tmp/node-build-master/bin/node-build "${NODE_VERSION}" /usr/local/node && \
    npm install -g yarn@$YARN_VERSION && \
    rm -rf /tmp/node-build-master

# Install node modules
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy application code
COPY . .

# Set the working directory in the container to /myapp
WORKDIR /a23

# Copy the current directory contents into the container at /a23
COPY Gemfile /a23/Gemfile
COPY Gemfile.lock /a23/Gemfile.lock

# Install any needed packages specified in Gemfile
RUN bundle install

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . /a23
```