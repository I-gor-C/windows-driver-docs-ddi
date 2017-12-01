---
UID: NC.ufxclient.EVT_UFX_DEVICE_ENDPOINT_ADD
title: EVT_UFX_DEVICE_ENDPOINT_ADD
author: windows-driver-content
description: The client driver's implementation to create a default endpoint object.
old-location: buses\evt_ufx_device_endpoint_add.htm
old-project: usbref
ms.assetid: F366990E-7FE3-401B-B8BE-E71EAFD3AC58
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_HARDWARE_FAILURE_CONTEXT, UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PFN_UFX_DEVICE_ENDPOINT_ADD
req.alt-loc: Ufxclient.h
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

# EVT_UFX_DEVICE_ENDPOINT_ADD callback



## -description
<p>The client driver's implementation to create a default endpoint object.</p>


## -prototype

````
EVT_UFX_DEVICE_ENDPOINT_ADD EvtUfxDeviceEndpointAdd;

NTSTATUS EvtUfxDeviceEndpointAdd(
  _In_          UFXDEVICE                UfxDevice,
  _In_    const PUSB_ENDPOINT_DESCRIPTOR EndpointDescriptor,
  _Inout_       PUFXENDPOINT_INIT        EndpointInit
)
{ ... }

typedef EVT_UFX_DEVICE_ENDPOINT_ADD PFN_UFX_DEVICE_ENDPOINT_ADD;
````


## -parameters
<dl>

### -param <i>UfxDevice</i> [in]

<dd>
<p>The handle to a  USB device object that the client driver received in a previous call to  the <a href="buses.ufxdevicecreate">UfxDeviceCreate</a>.</p>
</dd>

### -param <i>EndpointDescriptor</i> [in]

<dd>
<p>A pointer to a <a href="..\usbspec\ns-usbspec--usb-endpoint-descriptor.md">USB_ENDPOINT_DESCRIPTOR</a> structure that contains descriptor data.</p>
</dd>

### -param <i>EndpointInit</i> [in, out]

<dd>
<p>A pointer to an  UFXENDPOINT_INIT opaque structure that contains the endpoint descriptor required  to create an endpoint object.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p>The client driver for the function host controller registers its <i>EVT_UFX_DEVICE_ENDPOINT_ADD</i> implementation with the USB function class extension (UFX) by calling the <a href="buses.ufxdevicecreate">UfxDeviceCreate</a> method.</p>

<p>To create the endpoint the client driver is expected to initialize the attributes of the endpoint’s transfer and command queues, and then call <a href="buses.ufxendpointcreate">UfxEndpointCreate</a> to create the endpoint.</p>

<p>The client driver indicates completion of this event by calling the <a href="buses.ufxdeviceeventcomplete">UfxDeviceEventComplete</a> method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
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
<a href="buses.ufxdevicecreate">UfxDeviceCreate</a>
</dt>
<dt>
<a href="buses.ufxdeviceeventcomplete">UfxDeviceEventComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UFX_DEVICE_ENDPOINT_ADD callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
