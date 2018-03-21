# Atari RPC

An RPC server that serves the Arcade Learning Environment over the network.


## Why

This is for people who want to build reinforcement learning algorithms in
languages other than python, or who want to explore alternative network setups
in distributed reinforcement learning models.

Currently, one has the following choices:

- Directly call the C++ source for some environment
- Use an OpenAI gym environment from python

So if you're not using python, C++, or something like lua which interoperates
nicely with C, C++, then this is a pain.

Specifically for me, I'm implementing reinforcement algorithms in Go.


## How

Remote procedure call (RPC) is the standard approach to interoperability between
applications with different runtimes. This project exposes a subset of OpenAI's
python API over the network in a type-safe manner, by funnelling network requests
to and from the environment.

This will be shipped as a pre-built docker image, so that getting up and running
is as easy as:

```bash
docker run -p 8080:8080 cshenton/atari
```

From then, the server will handle a single environment at a time, with the
following API:

- `Start(Environment) returns State` resets the environment to the specified one
- `Step(Action) returns State` steps the environment

Where `Start` wraps both make and reset in the gym python API.


## Roadmap

- Python gRPC server with the atari environments
- Guide on generating client stubs
- (later) remove python client and talk directly to ALE
