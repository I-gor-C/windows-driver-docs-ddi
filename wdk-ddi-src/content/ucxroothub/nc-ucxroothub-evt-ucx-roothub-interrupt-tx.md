---
UID: NC.ucxroothub.EVT_UCX_ROOTHUB_INTERRUPT_TX
title: EVT_UCX_ROOTHUB_INTERRUPT_TX
author: windows-driver-content
description: The client driver's implementation that UCX calls when it receives a request for information about changed ports.
old-location: buses\evt_ucx_roothub_interrupt_tx.htm
old-project: usbref
ms.assetid: e2371b90-2274-459b-9e4a-5c9936d21b9c
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
req.alt-api: PEVT_UCX_ROOTHUB_INTERRUPT_TX
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

# EVT_UCX_ROOTHUB_INTERRUPT_TX callback



## -description
<p>The client driver's implementation that UCX calls when it receives a request for information about changed ports.</p>


## -prototype

````
EVT_UCX_ROOTHUB_INTERRUPT_TX EvtUcxInterruptTransferTx;

VOID EvtUcxInterruptTransferTx(
  _In_ UCXROOTHUB UcxRootHub,
  _In_ WDFREQUEST Request
)
{ ... }

typedef EVT_UCX_ROOTHUB_INTERRUPT_TX PEVT_UCX_ROOTHUB_INTERRUPT_TX;
````


## -parameters
<dl>

### -param <i>UcxRootHub</i> [in]

<dd>
<p>A handle to a UCX object that represents the root hub.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>Contains the <a href="..\usb\ns-usb--urb.md">URB</a> for the root hub interrupt transfer request.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="buses._ucxroothubcreate">UcxRootHubCreate</a>
 method.</p>

<p> The <i>Request</i> parameter contains a buffer in which each bit corresponds to a root
    hub port, with the first bit corresponding to the first port.  The
    client driver sets the corresponding bit if any port has changed, and then completes the request.</p>

<p>The client driver returns completion status in <i>Request</i>.</p>

<p>This snippet shows how the callback extracts the root hub interrupt transfer request.</p>

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