
# DeutschlandAPI SDK

This SDK helps to access the [DeutschlandAPI](https://deutschland-api.dev)

## Usage

The following example shows how you initialize the client:

```python
from sdk.client import Client

client = Client.buildAnonymous()

for city in client.city().getAll():
    print(city.state)

```

More information about the complete API at:
https://app.typehub.cloud/d/deutschland-api/sdk
