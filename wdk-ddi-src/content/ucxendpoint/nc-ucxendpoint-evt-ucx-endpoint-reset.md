---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_RESET
title: EVT_UCX_ENDPOINT_RESET
author: windows-driver-content
description: The client driver's implementation that UCX calls to reset the controller’s programming for an endpoint.
old-location: buses\evt_ucx_endpoint_reset.htm
old-project: usbref
ms.assetid: 927fdd48-416e-4e8f-a29c-c2799952197e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCXUSBDEVICE_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PEVT_UCX_ENDPOINT_RESET
req.alt-loc: ucxendpoint.h
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

# EVT_UCX_ENDPOINT_RESET callback



## -description
<p>The client driver's implementation that UCX calls to reset the controller’s programming for an endpoint.</p>


## -prototype

````
EVT_UCX_ENDPOINT_RESET EvtUcxEndpointReset;

VOID EvtUcxEndpointReset(
  _In_ UCXCONTROLLER UcxController,
  _In_ UCXENDPOINT   Endpoint,
  _In_ WDFREQUEST    Request
)
{ ... }

typedef EVT_UCX_ENDPOINT_RESET PEVT_UCX_ENDPOINT_RESET;
````


## -parameters
<dl>

### -param <i>UcxController</i> [in]

<dd>
<p> A handle to the UCX controller that the client driver received in a previous call to  the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.</p>
</dd>

### -param <i>Endpoint</i> [in]

<dd>
<p>A handle to a UCXENDPOINT object that represents the endpoint.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object that the client driver completes when the reset operation is finished.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="buses._ucxendpointcreate">UcxEndpointCreate</a>
 method.</p>

<p>The client driver returns completion status in the WDFREQUEST, which it might complete
    asynchronously.</p>

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
<dt>Ucxendpoint.h (include Ucxclass.h or Ucxendpoint.h)</dt>
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