---
UID: NC.ucxroothub.EVT_UCX_ROOTHUB_GET_INFO
title: EVT_UCX_ROOTHUB_GET_INFO
author: windows-driver-content
description: The client driver's implementation that UCX calls when it receives a request for information about the root hub.
old-location: buses\evt_ucx_roothub_get_info.htm
old-project: usbref
ms.assetid: b882b401-f806-4334-a8c5-fa65382fb9d3
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS, UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS, *PUCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PEVT_UCX_ROOTHUB_GET_INFO
req.alt-loc: ucxroothub.h
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

# EVT_UCX_ROOTHUB_GET_INFO callback



## -description
<p>The client driver's implementation that UCX calls when it receives a request for information about the root hub.</p>


## -prototype

````
EVT_UCX_ROOTHUB_GET_INFO EvtUcxRootHubGetInfo;

VOID EvtUcxRootHubGetInfo(
  _In_ UCXROOTHUB UcxRootHub,
  _In_ WDFREQUEST Request
)
{ ... }

typedef EVT_UCX_ROOTHUB_GET_INFO PEVT_UCX_ROOTHUB_GET_INFO;
````


## -parameters
<dl>

### -param <i>UcxRootHub</i> [in]

<dd>
<p>A handle to a UCX object that represents the root hub.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>A structure of type <a href="buses._roothub_info">ROOTHUB_INFO</a>.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="buses._ucxroothubcreate">UcxRootHubCreate</a>
 method.</p>

<p>The <a href="buses._roothub_info">_ROOTHUB_INFO</a> structure contains the number of USB 2.0 and USB 3.0 ports supported by the root hub.</p>

<p>After UCX calls  the <i>EVT_UCX_ROOTHUB_GET_INFO</i> function, the number of ports exposed by the root hub is guaranteed to remain the same. Note that these are virtual ports, not physical ports.  Each physical USB connector is represented by one or more 
ports of different speed on the root hub.</p>

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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
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
<a href="buses._roothub_info">_ROOTHUB_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_ROOTHUB_GET_INFO callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
