---
UID: NA:udecxusbendpoint
---

# Udecxusbendpoint.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Udecxusbendpoint.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UDECX_USB_ENDPOINT_CALLBACKS_INIT function](nf-udecxusbendpoint-udecx_usb_endpoint_callbacks_init.md) | Initializes a UDECX_USB_ENDPOINT_CALLBACKS structure before a UdecxUsbEndpointCreate call. |
| [UdecxUsbEndpointCreate function](nf-udecxusbendpoint-udecxusbendpointcreate.md) | Creates a UDE endpoint object. |
| [UdecxUsbEndpointInitFree function](nf-udecxusbendpoint-udecxusbendpointinitfree.md) | Release the resources that were allocated by the UdecxUsbSimpleEndpointInitAllocate call. |
| [UdecxUsbEndpointInitSetCallbacks function](nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks.md) | Sets pointers to UDE client driver-implemented callback functions in the initialization parameters of the simple endpoint to create. |
| [UdecxUsbEndpointInitSetEndpointAddress function](nf-udecxusbendpoint-udecxusbendpointinitsetendpointaddress.md) | Sets the address of the endpoint in the initialization parameters of the simple endpoint to create. |
| [UdecxUsbEndpointPurgeComplete function](nf-udecxusbendpoint-udecxusbendpointpurgecomplete.md) | Completes an asynchronous request for canceling all I/O requests queued to the specified endpoint. |
| [UdecxUsbEndpointSetWdfIoQueue function](nf-udecxusbendpoint-udecxusbendpointsetwdfioqueue.md) | Sets a framework queue object with a UDE endpoint. |
| [UdecxUsbSimpleEndpointInitAllocate function](nf-udecxusbendpoint-udecxusbsimpleendpointinitallocate.md) | Allocates memory for an initialization structure that is used to create a simple endpoint for the specified virtual USB device. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_UDECX_USB_ENDPOINT_CALLBACKS structure](ns-udecxusbendpoint-_udecx_usb_endpoint_callbacks.md) | Contains function pointers to endpoint callback functions implemented by the UDE client driver. Initialize this structure by calling UDECX_USB_ENDPOINT_CALLBACKS_INIT. |
