---
UID: NS.udecxusbdevice._UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS
title: UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS
author: windows-driver-content
description: Initializes a UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure with pointers to callback functions that are implemented by a UDE client for a virtual USB device.
old-location: buses\udecx_usb_device_state_change_callbacks.htm
old-project: usbref
ms.assetid: 9847A6E1-9551-4F0A-8B50-BB191B0181EF
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS, UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS, *PUDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS
req.alt-loc: UdecxUsbDevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure



## -description
<p>Initializes a <b>UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS</b> structure with pointers to callback functions that are implemented by a UDE client for a virtual USB device. </p>


## -syntax

````
typedef struct _UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS {
  ULONG                                     Size;
  PFN_UDECX_USB_DEVICE_D0_ENTRY             EvtUsbDeviceLinkPowerEntry;
  PFN_UDECX_USB_DEVICE_D0_EXIT              EvtUsbDeviceLinkPowerExit;
  PFN_UDECX_USB_DEVICE_DEFAULT_ENDPOINT_ADD EvtUsbDeviceDefaultEndpointAdd;
  PFN_UDECX_USB_DEVICE_ENDPOINT_ADD         EvtUsbDeviceEndpointAdd;
  PFN_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE  EvtUsbDeviceEndpointsConfigure;
} UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS, *PUDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size of this structure.</p>
</dd>

### -field EvtUsbDeviceLinkPowerEntry

<dd>
<p>A pointer to an <a href="..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-d0-entry.md">EVT_UDECX_USB_DEVICE_D0_ENTRY</a> callback function implemented by a UDE client driver.</p>
</dd>

### -field EvtUsbDeviceLinkPowerExit

<dd>
<p>A pointer to an <a href="..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-d0-exit.md">EVT_UDECX_USB_DEVICE_D0_EXIT</a> callback function implemented by a UDE client driver.</p>
</dd>

### -field EvtUsbDeviceDefaultEndpointAdd

<dd>
<p>A pointer to an <a href="..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-default-endpoint-add.md">EVT_UDECX_USB_DEVICE_DEFAULT_ENDPOINT_ADD</a> callback function implemented by a UDE client driver.</p>
</dd>

### -field EvtUsbDeviceEndpointAdd

<dd>
<p>A pointer to an E<a href="..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-endpoint-add.md">VT_UDECX_USB_DEVICE_ENDPOINT_ADD</a> callback function implemented by a UDE client driver.</p>
</dd>

### -field EvtUsbDeviceEndpointsConfigure

<dd>
<p>A pointer to an <a href="..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-endpoints-configure.md">EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE</a> callback function implemented by a UDE client driver.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>UdecxUsbDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitsetstatechangecallbacks.md">UdecxUsbDeviceInitSetStateChangeCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
