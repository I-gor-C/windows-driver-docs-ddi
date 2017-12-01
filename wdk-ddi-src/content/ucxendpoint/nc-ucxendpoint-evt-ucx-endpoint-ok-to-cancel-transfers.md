---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
title: EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
author: windows-driver-content
description: The client driver's implementation that UCX calls to notify the controller driver that it can complete cancelled transfers on the endpoint.
old-location: buses\evt_ucx_endpoint_ok_to_cancel_transfers.htm
old-project: usbref
ms.assetid: 3cb30b74-d50d-49dd-ab5d-de1cf71facd4
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
req.alt-api: PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
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

# EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS callback



## -description
<p>The client driver's implementation that UCX calls to notify the controller driver that it can complete cancelled transfers on the
    endpoint.</p>


## -prototype

````
EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS EvtUcxEndpointOkToCancelTransfers;

VOID EvtUcxEndpointOkToCancelTransfers(
  _In_ UCXENDPOINT Endpoint
)
{ ... }

typedef EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS;
````


## -parameters
<dl>

### -param <i>Endpoint</i> [in]

<dd>
<p>A handle to a UCXENDPOINT object that represents the endpoint.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="buses._ucxendpointcreate">UcxEndpointCreate</a>
 method.</p>

<p>Before completing the URB associated with the transfer, the client driver calls <a href="buses._ucxendpointneedtocanceltransfers">UcxEndpointNeedToCancelTransfers</a>
and then waits for UCX to call this function. Then the client driver can complete the URB with <b>STATUS_CANCELLED</b>.</p>

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