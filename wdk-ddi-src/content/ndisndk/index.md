# Ndisndk.h header


This header is used by Networking drivers for Windows Vista and later. For more information, see
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Ndisndk.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [CLOSE_NDK_ADAPTER_HANDLER callback](nc-ndisndk-close-ndk-adapter-handler.md) | The CloseNDKAdapterHandler (CLOSE_NDK_ADAPTER_HANDLER) function closes an NDK adapter instance on an NDK-capable NDIS miniport adapter. |
| [OPEN_NDK_ADAPTER_HANDLER callback](nc-ndisndk-open-ndk-adapter-handler.md) | The OpenNDKAdapterHandler (OPEN_NDK_ADAPTER_HANDLER) function opens an NDK adapter instance on an NDK-capable NDIS miniport adapter. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [NDIS_NDK_PROVIDER_CHARACTERISTICS structure](ns-ndisndk--ndis-ndk-provider-characteristics.md) | The NDIS_NDK_PROVIDER_CHARACTERISTICS structure specifies NDK provider characteristics. |
| [NDIS_OPEN_NDK_ADAPTER_PARAMETERS structure](ns-ndisndk--ndis-open-ndk-adapter-parameters.md) | The NDIS_OPEN_NDK_ADAPTER_PARAMETERS structure specifies parameters to open an NDK adapter instance on the NDK-capable miniport adapter. |
