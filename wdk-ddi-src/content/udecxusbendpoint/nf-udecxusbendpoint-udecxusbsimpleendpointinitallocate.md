---
UID: NF.udecxusbendpoint.UdecxUsbSimpleEndpointInitAllocate
title: UdecxUsbSimpleEndpointInitAllocate
author: windows-driver-content
description: Allocates memory for an initialization structure that is used to create a simple endpoint for the specified virtual USB device.
old-location: buses\udecxusbsimpleendpointinitallocate.htm
old-project: usbref
ms.assetid: 1BF79756-F55D-4F13-A03C-35F7880C5B21
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UdecxUsbSimpleEndpointInitAllocate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbendpoint.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UdecxUsbSimpleEndpointInitAllocate
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

# UdecxUsbSimpleEndpointInitAllocate function



## -description
<p>Allocates memory for an initialization  structure that is used to create a simple endpoint for the specified virtual USB device.  </p>


## -syntax

````
PUDECXUSBENDPOINT_INIT UdecxUsbSimpleEndpointInitAllocate(
  _In_ UDECXUSBDEVICE UdecxUsbDevice
);
````


## -parameters
<dl>

### -param UdecxUsbDevice [in]

<dd>
<p>A handle to UDE device object. The client driver retrieved this pointer in the previous call to <a href="..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicecreate.md">UdecxUsbDeviceCreate</a>.</p>
</dd>
</dl>

## -returns
<p>This method returns a pointer to an opaque <b>UDECXUSBENDPOINT_INIT</b> structure that contains the initialization parameters. The structure is allocated by the USB device emulation  class extension (UdeCx).</p>

## -remarks
<p>The UDE client driver calls this method to allocate parameters for a simple endpoint that is created by a subsequent call to <a href="..\udecxusbendpoint\nf-udecxusbendpoint-udecxusbendpointcreate.md">UdecxUsbEndpointCreate</a>. If the device is not created or the driver is finished using the resources, the driver must free the resources by calling <a href="..\udecxusbendpoint\nf-udecxusbendpoint-udecxusbendpointinitfree.md">UdecxUsbEndpointInitFree</a>.</p>

<p>The only valid time to create simple endpoints is after creating a the UDE device object and before calling <a href="..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceplugin.md">UdecxUsbDevicePlugIn</a> on the device.
</p>

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
<dt>Udecxusbendpoint.h (include Udecx.h)</dt>
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
<a href="..\udecxusbendpoint\nf-udecxusbendpoint-udecxusbendpointcreate.md">UdecxUsbEndpointCreate</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UdecxUsbSimpleEndpointInitAllocate function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
