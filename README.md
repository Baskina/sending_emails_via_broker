# RabbitMQ and Mongoengine Integration Demo

This Python application demonstrates the basic usage of RabbitMQ and Mongoengine.

## Overview

The application consists of two main components:

1. **Producer**: The `producer.py` file generates fake data for a MongoDB database, inserts it into the database under the collection named "contacts", and sends a message (containing the ID of the contact) via a RabbitMQ broker.

2. **Consumer**: The `consumer.py` file continuously listens for messages from the RabbitMQ broker. Upon receiving a message (containing the client ID), it sends emails to all clients whose data is stored in the MongoDB database. After sending the emails, the `isSent` field in the corresponding documents is updated to `True`.

## Database Structure

The MongoDB database is named "contacts" and contains documents with the following structure:

```json
{
    "name": "",
    "email": "",
    "isSent": false
}
```

## Example Output

Here's an example of the console output from the `consumer.py` file:

```
email was sent to Andrew Gallagher
email was sent to Penny Clark
email was sent to John Frank
email was sent to Lori Jensen
email was sent to Bobby Rivera
email was sent to Frederick Perry
email was sent to Tammy Jacobson
email was sent to Michael Thompson
email was sent to Jonathan Brown
email was sent to Kevin Martin
```