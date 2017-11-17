# Declarations in the ucxendpoint header
This header Ucxendpoint contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UCX_ENDPOINT_RESET callback function](nc-ucxendpoint-evt-ucx-endpoint-reset.md) | TBD |
| [PFN_UCXENDPOINTNOPINGRESPONSEERROR callback function](nc-ucxendpoint-pfn-ucxendpointnopingresponseerror.md) | TBD |
| [PFN_UCXENDPOINTPURGECOMPLETE callback function](nc-ucxendpoint-pfn-ucxendpointpurgecomplete.md) | TBD |
| [EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS callback](nc-ucxendpoint-evt-ucx-endpoint-get-isoch-transfer-path-delays.md) | UCX invokes this callback function to get information about transfer path delays for an isochronous endpoint. |
| [EVT_UCX_DEFAULT_ENDPOINT_UPDATE callback function](nc-ucxendpoint-evt-ucx-default-endpoint-update.md) | TBD |
| [*PFN_UCXDEFAULTENDPOINTINITSETEVENTCALLBACKS callback function](nc-ucxendpoint-pfn-ucxdefaultendpointinitseteventcallbacks.md) | TBD |
| [*PFN_UCXENDPOINTINITSETEVENTCALLBACKS callback function](nc-ucxendpoint-pfn-ucxendpointinitseteventcallbacks.md) | TBD |
| [EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD callback function](nc-ucxendpoint-evt-ucx-endpoint-static-streams-add.md) | TBD |
| [EVT_UCX_ENDPOINT_START callback function](nc-ucxendpoint-evt-ucx-endpoint-start.md) | TBD |
| [EVT_UCX_ENDPOINT_ABORT callback function](nc-ucxendpoint-evt-ucx-endpoint-abort.md) | TBD |
| [PFN_UCXENDPOINTCREATE callback function](nc-ucxendpoint-pfn-ucxendpointcreate.md) | TBD |
| [EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS callback function](nc-ucxendpoint-evt-ucx-endpoint-ok-to-cancel-transfers.md) | TBD |
| [EVT_UCX_ENDPOINT_SET_CHARACTERISTIC callback](nc-ucxendpoint-evt-ucx-endpoint-set-characteristic.md) | UCX invokes this callback function to set the priority on an endpoint. |
| [EVT_UCX_ENDPOINT_PURGE callback function](nc-ucxendpoint-evt-ucx-endpoint-purge.md) | TBD |
| [*PFN_UCXENDPOINTSETWDFIOQUEUE callback function](nc-ucxendpoint-pfn-ucxendpointsetwdfioqueue.md) | TBD |
| [EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE callback function](nc-ucxendpoint-evt-ucx-endpoint-static-streams-disable.md) | TBD |
| [EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE callback function](nc-ucxendpoint-evt-ucx-endpoint-static-streams-enable.md) | TBD |
| [PFN_UCXENDPOINTGETSTATICSTREAMSREFERENCED callback function](nc-ucxendpoint-pfn-ucxendpointgetstaticstreamsreferenced.md) | TBD |
| [PFN_UCXENDPOINTNEEDTOCANCELTRANSFERS callback function](nc-ucxendpoint-pfn-ucxendpointneedtocanceltransfers.md) | TBD |
| [PFN_UCXENDPOINTABORTCOMPLETE callback function](nc-ucxendpoint-pfn-ucxendpointabortcomplete.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_ENDPOINT_CHARACTERISTIC structure](ns-ucxendpoint--ucx-endpoint-characteristic.md) | Stores the characteristics of an endpoint. |
| [DEFAULT_ENDPOINT_UPDATE structure](ns-ucxendpoint--default-endpoint-update.md) | TBD |
| [ENDPOINTS_CONFIGURE_FAILURE_FLAGS structure](ns-ucxendpoint--endpoints-configure-failure-flags.md) | TBD |
| [UCX_ENDPOINT_EVENT_CALLBACKS structure](ns-ucxendpoint--ucx-endpoint-event-callbacks.md) | TBD |
| [UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS structure](ns-ucxendpoint--ucx-endpoint-isoch-transfer-path-delays.md) | Stores the isochronous transfer path delay values. |
| [ENDPOINTS_CONFIGURE structure](ns-ucxendpoint--endpoints-configure.md) | TBD |
| [UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS structure](ns-ucxendpoint--ucx-default-endpoint-event-callbacks.md) | TBD |
| [ENDPOINT_RESET structure](ns-ucxendpoint--endpoint-reset.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_ENDPOINT_CHARACTERISTIC_PRIORITY enumeration](ne-ucxendpoint--ucx-endpoint-characteristic-priority.md) | TBD |
| [UCX_ENDPOINT_CHARACTERISTIC_TYPE enumeration](ne-ucxendpoint--ucx-endpoint-characteristic-type.md) | Defines values that indicates the type of endpoint characteristic. |
| [ENDPOINT_RESET_FLAGS enumeration](ne-ucxendpoint--endpoint-reset-flags.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UcxEndpointGetStaticStreamsReferenced function](nf-ucxendpoint-ucxendpointgetstaticstreamsreferenced.md) | TBD |
| [UcxEndpointCreate function](nf-ucxendpoint-ucxendpointcreate.md) | TBD |
| [UcxEndpointAbortComplete function](nf-ucxendpoint-ucxendpointabortcomplete.md) | TBD |
| [UcxEndpointInitSetEventCallbacks function](nf-ucxendpoint-ucxendpointinitseteventcallbacks.md) | TBD |
| [UcxEndpointNoPingResponseError function](nf-ucxendpoint-ucxendpointnopingresponseerror.md) | TBD |
| [UcxEndpointNeedToCancelTransfers function](nf-ucxendpoint-ucxendpointneedtocanceltransfers.md) | TBD |
| [UcxDefaultEndpointInitSetEventCallbacks function](nf-ucxendpoint-ucxdefaultendpointinitseteventcallbacks.md) | TBD |
| [UCX_ENDPOINT_EVENT_CALLBACKS_INIT function](nf-ucxendpoint-ucx-endpoint-event-callbacks-init.md) | TBD |
| [UcxEndpointSetWdfIoQueue function](nf-ucxendpoint-ucxendpointsetwdfioqueue.md) | TBD |
| [UcxEndpointPurgeComplete function](nf-ucxendpoint-ucxendpointpurgecomplete.md) | TBD |
| [UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT function](nf-ucxendpoint-ucx-default-endpoint-event-callbacks-init.md) | TBD |

This header is used in these topics:

- [usbref](..content/_usbref)
