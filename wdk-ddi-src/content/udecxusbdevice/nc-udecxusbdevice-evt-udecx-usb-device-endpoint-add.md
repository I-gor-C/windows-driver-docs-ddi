---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_ENDPOINT_ADD
title: EVT_UDECX_USB_DEVICE_ENDPOINT_ADD
author: windows-driver-content
description: The USB device emulation class extension (UdeCx) invokes this callback function to request the client driver to create a dynamic endpoint on the virtual USB device.
old-location: buses\evt_udecx_usb_device_endpoint_add.htm
old-project: usbref
ms.assetid: 82E17C75-BE81-4263-AC04-D3C93505917D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UdecxUrbSetBytesCompleted
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: EvtUsbDeviceEndpointAdd
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

# EVT_UDECX_USB_DEVICE_ENDPOINT_ADD callback



## -description
<p>The USB device emulation class extension (UdeCx) invokes this callback function to request the client driver to create a dynamic endpoint on the virtual USB device.</p>


## -prototype

````
EVT_UDECX_USB_DEVICE_ENDPOINT_ADD EvtUsbDeviceEndpointAdd;

NTSTATUS EvtUsbDeviceEndpointAdd(
  _In_ UDECXUSBDEVICE                                     UdecxUsbDevice,
  _In_ PUDECX_USB_ENDPOINT_INIT_AND_METADATA              EndpointToCreate
)
{ ... }
````


## -parameters
<dl>

### -param <i>UdecxUsbDevice</i> [in]

<dd>
<p>A handle to the UDE device object for which the client driver creates an endpoint. The driver created this object in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt595959">UdecxUsbDeviceCreate</a>.</p>
</dd>

### -param <i>EndpointToCreate</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt628007">UDECX_USB_ENDPOINT_INIT_AND_METADATA</a>             structure that contains the endpoint descriptor.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.</p>

## -remarks
<p>The client driver registered this callback function in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627972">UdecxUsbDeviceInitSetStateChangeCallbacks</a> by supplying a function pointer to its implementation.</p>

<p>In the implementation, the client driver is expected to create the endpoint by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt627983">UdecxUsbEndpointCreate</a> by using the initialization parameters (<b>UDECXUSBENDPOINT_INIT</b>) passed by the class extension in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt628007">UDECX_USB_ENDPOINT_INIT_AND_METADATA</a> structure.</p>

<p>The client driver registered this callback function in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627972">UdecxUsbDeviceInitSetStateChangeCallbacks</a> by supplying a function pointer to its implementation.</p>

<p>In the implementation, the client driver is expected to create the endpoint by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt627983">UdecxUsbEndpointCreate</a> by using the initialization parameters (<b>UDECXUSBENDPOINT_INIT</b>) passed by the class extension in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt628007">UDECX_USB_ENDPOINT_INIT_AND_METADATA</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627983">UdecxUsbEndpointCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595932">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UDECX_USB_DEVICE_ENDPOINT_ADD callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
