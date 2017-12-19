---
UID: NF.udecxusbdevice.UdecxUsbDeviceInitSetEndpointsType
title: UdecxUsbDeviceInitSetEndpointsType function
author: windows-driver-content
description: Indicates the type of endpoint (simple or dynamic) in the initialization parameters that the client driver uses to create the virtual USB device.
old-location: buses\udecxusbdeviceinitsetendpointstype.htm
old-project: UsbRef
ms.assetid: 44760191-77DD-40A9-AA11-AE8AB55AB307
ms.author: windowsdriverdev
ms.date: 12/14/2017
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
req.product: Windows 10 or later.
---

# UdecxUsbDeviceInitSetEndpointsType function



## -description
Indicates the type of endpoint (simple or dynamic) in the initialization parameters that the client driver uses to create the virtual USB device.



## -syntax

````
void UdecxUsbDeviceInitSetEndpointsType(
  _Inout_ PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit,
  _In_    UDECX_ENDPOINT_TYPE  UdecxEndpointType
);
````


## -parameters

### -param UdecxUsbDeviceInit [in, out]

A pointer to a WDF-allocated structure that contains initialization parameters for the virtual USB device.  The client driver retrieved this pointer in the previous call to <a href="buses.udecxusbdeviceinitallocate">UdecxUsbDeviceInitAllocate</a>. 


### -param UdecxEndpointType [in]

A <a href="buses.udecx_endpoint_type">UDECX_ENDPOINT_TYPE</a>-type value that indicates the type of USB endpoint.


## -returns
This function does not return a value.


## -remarks
Before creating the virtual USB device, the client driver must indicate the type of endpoint it supports. It can support one of two types (defined in <a href="buses.udecx_endpoint_type">UDECX_ENDPOINT_TYPE</a>): 

The <i>UdecxUsbDeviceInit</i> is an opaque structure that contains pointers to callback functions related to endpoints. If the client driver supports dynamic endpoints, then these callback functions must be implemented by the driver:

Before calling this method, the client driver must have set those pointers by calling <a href="buses.udecxusbdeviceinitsetstatechangecallbacks">UdecxUsbDeviceInitSetStateChangeCallbacks</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.15

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>UdecxUsbDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Udecxstub.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

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
<a href="..\udecxusbdevice\nc-udecxusbdevice-evt_udecx_usb_device_endpoints_configure.md">EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE</a>
</dt>
<dt>
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20UdecxUsbDeviceInitSetEndpointsType function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

