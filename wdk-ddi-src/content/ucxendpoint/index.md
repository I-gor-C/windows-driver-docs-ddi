# Ucxendpoint.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucxendpoint.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT function](nf-ucxendpoint-ucx-default-endpoint-event-callbacks-init.md) | Initializes a UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS structure with client driver's callback functions. The client driver calls this function before calling UcxEndpointCreate method to create an endpoint and register its callback functions with UCX. |
| [UCX_ENDPOINT_EVENT_CALLBACKS_INIT function](nf-ucxendpoint-ucx-endpoint-event-callbacks-init.md) | Initializes a UCX_ENDPOINT_EVENT_CALLBACKS structure with client driver's callback functions. The client driver calls this function before calling UcxEndpointCreate method to create an endpoint and register its callback functions with UCX. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_UCX_DEFAULT_ENDPOINT_UPDATE callback](nc-ucxendpoint-evt-ucx-default-endpoint-update.md) | The client driver's implementation that UCX calls with information about the default endpoint. |
| [EVT_UCX_ENDPOINT_ABORT callback](nc-ucxendpoint-evt-ucx-endpoint-abort.md) | The client driver's implementation that UCX calls to abort the queue associated with the endpoint. |
| [EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS callback](nc-ucxendpoint-evt-ucx-endpoint-get-isoch-transfer-path-delays.md) | UCX invokes this callback function to get information about transfer path delays for an isochronous endpoint. |
| [EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS callback](nc-ucxendpoint-evt-ucx-endpoint-ok-to-cancel-transfers.md) | The client driver's implementation that UCX calls to notify the controller driver that it can complete cancelled transfers on the endpoint. |
| [EVT_UCX_ENDPOINT_PURGE callback](nc-ucxendpoint-evt-ucx-endpoint-purge.md) | The client driver's implementation that completes all outstanding I/O requests on the endpoint. |
| [EVT_UCX_ENDPOINT_RESET callback](nc-ucxendpoint-evt-ucx-endpoint-reset.md) | The client driver's implementation that UCX calls to reset the controller’s programming for an endpoint. |
| [EVT_UCX_ENDPOINT_SET_CHARACTERISTIC callback](nc-ucxendpoint-evt-ucx-endpoint-set-characteristic.md) | UCX invokes this callback function to set the priority on an endpoint. |
| [EVT_UCX_ENDPOINT_START callback](nc-ucxendpoint-evt-ucx-endpoint-start.md) | The client driver's implementation that UCX calls to start the queue associated with the endpoint. |
| [EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD callback](nc-ucxendpoint-evt-ucx-endpoint-static-streams-add.md) | The client driver's implementation that UCX calls to create static streams. |
| [EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE callback](nc-ucxendpoint-evt-ucx-endpoint-static-streams-disable.md) | The client driver's implementation that UCX calls to release controller resources for all streams for an endpoint. |
| [EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE callback](nc-ucxendpoint-evt-ucx-endpoint-static-streams-enable.md) | The client driver's implementation that UCX calls to enable the static streams. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [DEFAULT_ENDPOINT_UPDATE structure](ns-ucxendpoint--default-endpoint-update.md) | Contains the handle to the default endpoint to update in a framework request that is passed by UCX when it invokes EVT_UCX_DEFAULT_ENDPOINT_UPDATE callback function. |
| [ENDPOINTS_CONFIGURE structure](ns-ucxendpoint--endpoints-configure.md) | Describes endpoints to enable or disable endpoints. This structure is passed by UCX in the EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE callback function. |
| [ENDPOINTS_CONFIGURE_FAILURE_FLAGS structure](ns-ucxendpoint--endpoints-configure-failure-flags.md) | This structure provides failure flags to indicate errors, if any, that might have occurred during a request to an EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE callback function. |
| [ENDPOINT_RESET structure](ns-ucxendpoint--endpoint-reset.md) | Describes information required to reset an endpoint. This structure is passed by UCX in the EVT_UCX_ENDPOINT_RESET callback function. |
| [UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS structure](ns-ucxendpoint--ucx-default-endpoint-event-callbacks.md) | This structure provides a list of UCX default endpoint event callback functions. |
| [UCX_ENDPOINT_CHARACTERISTIC structure](ns-ucxendpoint--ucx-endpoint-characteristic.md) | Stores the characteristics of an endpoint. |
| [UCX_ENDPOINT_EVENT_CALLBACKS structure](ns-ucxendpoint--ucx-endpoint-event-callbacks.md) | This structure provides a list of pointers to UCX endpoint event callback functions. |
| [UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS structure](ns-ucxendpoint--ucx-endpoint-isoch-transfer-path-delays.md) | Stores the isochronous transfer path delay values. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [ENDPOINT_RESET_FLAGS enumeration](ne-ucxendpoint--endpoint-reset-flags.md) | Defines parameters for a request to reset an endpoint. |
| [UCX_ENDPOINT_CHARACTERISTIC_TYPE enumeration](ne-ucxendpoint--ucx-endpoint-characteristic-type.md) | Defines values that indicates the type of endpoint characteristic. |
