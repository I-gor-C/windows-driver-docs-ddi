---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_UPDATE
title: EVT_UCX_USBDEVICE_UPDATE
author: windows-driver-content
description: The client driver's implementation that UCX calls to update device properties.
old-location: buses\evt_ucx_usbdevice_update.htm
old-project: usbref
ms.assetid: 5dbf3560-9968-4996-8bce-fb43e3918d72
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: STREAM_INFO, STREAM_INFO, *PSTREAM_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PEVT_UCX_USBDEVICE_UPDATE
req.alt-loc: ucxusbdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UCX_USBDEVICE_UPDATE callback



## -description
<p>The client driver's implementation that UCX calls to
    update device properties.</p>


## -prototype

````
EVT_UCX_USBDEVICE_UPDATE EvtUcxUsbDeviceUpdate;

VOID EvtUcxUsbDeviceUpdate(
  _In_ UCXCONTROLLER UcxController,
  _In_ WDFREQUEST    Request
)
{ ... }

typedef EVT_UCX_USBDEVICE_UPDATE PEVT_UCX_USBDEVICE_UPDATE;
````


## -parameters
<dl>

### -param <i>UcxController</i> [in]

<dd>
<p> A handle to the UCX controller that the client driver received in a previous call to  the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>Contains the <a href="buses._usbdevice_update">USBDEVICE_UPDATE</a> structure.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="buses._ucxusbdevicecreate">UcxUsbDeviceCreate</a> method.</p>

<p>The host controller driver communicates with the hardware to update descriptors, LPM parameters, whether device is a hub, and
    maximum exit latency, as needed.</p>

<p>The client driver returns completion status in <i>Request</i>.  The driver can complete the WDFREQUEST asynchronously.</p>

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
<dt>Ucxusbdevice.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucx_usbdevice_event_callbacks_init">UCX_USBDEVICE_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="buses._ucxusbdeviceinitseteventcallbacks">UcxUsbDeviceInitSetEventCallbacks</a>
</dt>
<dt>
<a href="buses._usbdevice_update">USBDEVICE_UPDATE</a>
</dt>
<dt>
<a href="buses._ucxusbdevicecreate">UcxUsbDeviceCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_USBDEVICE_UPDATE callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
