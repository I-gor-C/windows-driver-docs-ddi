# Declarations in the udecxusbendpoint header
This header Udecxusbendpoint contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [UdecxUsbEndpointPurgeComplete function](nf-udecxusbendpoint-udecxusbendpointpurgecomplete.md) | TBD |
| [UDECX_USB_ENDPOINT_CALLBACKS_INIT function](nf-udecxusbendpoint-udecx-usb-endpoint-callbacks-init.md) | TBD |
| [UdecxUsbSimpleEndpointInitAllocate function](nf-udecxusbendpoint-udecxusbsimpleendpointinitallocate.md) | TBD |
| [UdecxUsbEndpointInitSetCallbacks function](nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks.md) | TBD |
| [UdecxUsbEndpointInitSetEndpointAddress function](nf-udecxusbendpoint-udecxusbendpointinitsetendpointaddress.md) | TBD |
| [UdecxUsbEndpointSetWdfIoQueue function](nf-udecxusbendpoint-udecxusbendpointsetwdfioqueue.md) | TBD |
| [UdecxUsbEndpointInitFree function](nf-udecxusbendpoint-udecxusbendpointinitfree.md) | TBD |
| [UdecxUsbEndpointCreate function](nf-udecxusbendpoint-udecxusbendpointcreate.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_UDECXUSBENDPOINTCREATE callback function](nc-udecxusbendpoint-pfn-udecxusbendpointcreate.md) | TBD |
| [*PFN_UDECXUSBSIMPLEENDPOINTINITALLOCATE callback function](nc-udecxusbendpoint-pfn-udecxusbsimpleendpointinitallocate.md) | TBD |
| [*PFN_UDECXUSBENDPOINTINITFREE callback function](nc-udecxusbendpoint-pfn-udecxusbendpointinitfree.md) | TBD |
| [*PFN_UDECXUSBENDPOINTINITSETCALLBACKS callback function](nc-udecxusbendpoint-pfn-udecxusbendpointinitsetcallbacks.md) | TBD |
| [EVT_UDECX_USB_ENDPOINT_START callback](nc-udecxusbendpoint-evt-udecx-usb-endpoint-start.md) | The USB device emulation class extension (UdeCx) invokes this callback function to start processing I/O requests on the specified endpoint of the virtual USB device. |
| [EVT_UDECX_USB_ENDPOINT_PURGE callback](nc-udecxusbendpoint-evt-udecx-usb-endpoint-purge.md) | The USB device emulation class extension (UdeCx) invokes this callback function to stop queuing I/O requests to the endpoint's queue and cancel unprocessed requests. |
| [EVT_UDECX_USB_ENDPOINT_RESET callback](nc-udecxusbendpoint-evt-udecx-usb-endpoint-reset.md) | The USB device emulation class extension (UdeCx) invokes this callback function to reset an endpoint of the virtual USB device. |
| [*PFN_UDECXUSBENDPOINTINITSETENDPOINTADDRESS callback function](nc-udecxusbendpoint-pfn-udecxusbendpointinitsetendpointaddress.md) | TBD |
| [*PFN_UDECXUSBENDPOINTPURGECOMPLETE callback function](nc-udecxusbendpoint-pfn-udecxusbendpointpurgecomplete.md) | TBD |
| [*PFN_UDECXUSBENDPOINTSETWDFIOQUEUE callback function](nc-udecxusbendpoint-pfn-udecxusbendpointsetwdfioqueue.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_USB_ENDPOINT_CALLBACKS structure](ns-udecxusbendpoint--udecx-usb-endpoint-callbacks.md) | TBD |

This header is used in these topics:

- [usbref](..content/_usbref)
