"#Multi-User Chat Application"
## Architecture

This application follows a client–server architecture using TCP sockets.

Multiple clients connect to a central server.
The server is responsible for:

accepting client connections
receiving messages from clients
broadcasting messages to other connected clients
persisting messages to a database

Clients do not communicate directly with each other.
All communication is routed through the server, which acts as the single source of truth for message ordering and delivery.


## Connection Lifecycle
The server starts and listens on a TCP port.

A client initiates a TCP connection to the server.

The server accepts the connection and creates a dedicated handler for that client.

The client sends an initial message containing its username.

The server registers the client in its active user list.

The client can now send chat messages to the server.

The server broadcasts each received message to all connected clients.

When a client disconnects (gracefully or due to failure), the server removes the client from the active user list and releases resources.

## Message Protocol
Although TCP provides reliable byte-stream delivery, it does not define message boundaries.
Therefore, this application defines a simple application-level message protocol using JSON.

Each message is sent as a JSON-formatted string with the following structure:
{
  "type": "chat",
  "sender": "user1",
  "timestamp": 1700000000,
  "content": "Hello everyone"
}
Why JSON is used:
It is human-readable and easy to debug.
It allows the protocol to be extended (e.g., join, leave, typing events).
It clearly separates message metadata from message content

## Concurrency Model 
The server handles multiple clients concurrently using a thread-per-client model.

Each client connection is handled in a separate thread.

Shared resources such as the list of connected clients are accessed by multiple threads.

To prevent race conditions, access to shared data structures is protected using locks (mutexes).

This approach is simple and effective for a limited number of clients.
For larger scale systems, an event-driven or asynchronous I/O model would be more appropriate.
