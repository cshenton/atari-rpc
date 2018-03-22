# Atari RPC :space_invader:

An RPC server that serves the Arcade Learning Environment over the network.


## What Is This?

This is an RPC server that exposes the "arcade learning environment" over the network.
It uses OpenAI's gym and Google's gRPC under the hood. It is intended to enable
language agnostic access to this reinforcement learning environment.


## Installation & Usage

To install the server, just pull the prebuilt docker image:
```bash
docker run -p 8080:8080 cshenton/atari
```

To communicate with the server, use the included `atari.proto` file in `proto/`
to generate a client to communicate with the library. For example, to generate
Golang stubs from a neighbouring repo, run:
```
protoc -I ../atari-rpc/proto/ atari.proto --go_out=plugins=grpc:path/to/your/proto
```

Then use the generated client and structs to communicate with the server. If you've
never used gRPC before, check out the [docs for your language](https://grpc.io/docs/).


## Technical Notes

This is a single thread server, it does not handle multiple active environments at
once, if you want that, just spin up more containers.


## Contributing

#### Environment
```bash
virtualenv -p python3.5 venv
pip install -r requirements.txt
source venv/bin/activate
```

#### Running tests
```bash
python -m pytest tests/
```

#### Generating stubs
```
python -m grpc_tools.protoc -I . proto/atari.proto --python_out=. --grpc_python_out=.
```
