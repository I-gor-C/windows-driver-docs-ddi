---
UID: NF.udecxusbdevice.UdecxUsbDeviceInitSetEndpointsType
title: UdecxUsbDeviceInitSetEndpointsType
author: windows-driver-content
description: Indicates the type of endpoint (simple or dynamic) in the initialization parameters that the client driver uses to create the virtual USB device.
old-location: buses\udecxusbdeviceinitsetendpointstype.htm
old-project: usbref
ms.assetid: 44760191-77DD-40A9-AA11-AE8AB55AB307
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UdecxUsbDeviceInitSetEndpointsType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UdecxUsbDeviceInitSetEndpointsType
req.alt-loc: Udecxstub.lib,Udecxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UdecxUsbDeviceInitSetEndpointsType function



## -description
<p>Indicates the type of endpoint (simple or dynamic) in the initialization parameters that the client driver uses to create the virtual USB device.</p>


## -syntax

````
void UdecxUsbDeviceInitSetEndpointsType(
  _Inout_ PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit,
  _In_    UDECX_ENDPOINT_TYPE  UdecxEndpointType
);
````


## -parameters
<dl>

### -param <i>UdecxUsbDeviceInit</i> [in, out]

<dd>
<p>A pointer to a WDF-allocated structure that contains initialization parameters for the virtual USB device.  The client driver retrieved this pointer in the previous call to <a href="buses.udecxusbdeviceinitallocate">UdecxUsbDeviceInitAllocate</a>. </p>
</dd>

### -param <i>UdecxEndpointType</i> [in]

<dd>
<p>A <a href="buses.udecx_endpoint_type">UDECX_ENDPOINT_TYPE</a>-type value that indicates the type of USB endpoint.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>Before creating the virtual USB device, the client driver must indicate the type of endpoint it supports. It can support one of two types (defined in <a href="buses.udecx_endpoint_type">UDECX_ENDPOINT_TYPE</a>): </p>

<p>The <i>UdecxUsbDeviceInit</i> is an opaque structure that contains pointers to callback functions related to endpoints. If the client driver supports dynamic endpoints, then these callback functions must be implemented by the driver:</p>

<p>Before calling this method, the client driver must have set those pointers by calling <a href="buses.udecxusbdeviceinitsetstatechangecallbacks">UdecxUsbDeviceInitSetStateChangeCallbacks</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Udecxstub.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_endpoints_and_their_pipes">USB endpoints</a>
</dt>
<dt>
<a href="buses.udecxusbdeviceinitallocate">UdecxUsbDeviceInitAllocate</a>
</dt>
<dt>
<a href="buses.udecxusbdeviceinitsetstatechangecallbacks">UdecxUsbDeviceInitSetStateChangeCallbacks</a>
</dt>
<dt>
<a href="buses.evt_udecx_usb_device_endpoints_configure">EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE</a>
</dt>
<dt>
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UdecxUsbDeviceInitSetEndpointsType function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
