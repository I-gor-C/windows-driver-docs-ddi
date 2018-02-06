---
UID: NC:ucxroothub.EVT_UCX_ROOTHUB_INTERRUPT_TX
title: EVT_UCX_ROOTHUB_INTERRUPT_TX
author: windows-driver-content
description: The client driver's implementation that UCX calls when it receives a request for information about changed ports.
old-location: buses\evt_ucx_roothub_interrupt_tx.htm
old-project: usbref
ms.assetid: e2371b90-2274-459b-9e4a-5c9936d21b9c
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: buses.evt_ucx_roothub_interrupt_tx, EvtUcxInterruptTransferTx callback function [Buses], EvtUcxInterruptTransferTx, EVT_UCX_ROOTHUB_INTERRUPT_TX, EVT_UCX_ROOTHUB_INTERRUPT_TX, ucxroothub/EvtUcxInterruptTransferTx, PEVT_UCX_ROOTHUB_INTERRUPT_TX callback function pointer [Buses], PEVT_UCX_ROOTHUB_INTERRUPT_TX
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	ucxroothub.h
apiname:
-	PEVT_UCX_ROOTHUB_INTERRUPT_TX
product: Windows
targetos: Windows
req.typenames: UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS, *PUCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS
req.product: Windows 10 or later.
---


# EVT_UCX_ROOTHUB_INTERRUPT_TX function
The client driver's implementation that UCX calls when it receives a request for information about changed ports.

## Syntax

```
EVT_UCX_ROOTHUB_INTERRUPT_TX EvtUcxRoothubInterruptTx;

void EvtUcxRoothubInterruptTx(
  UCXROOTHUB UcxRootHub,
  WDFREQUEST Request
)
{...}
```

## Parameters

`UcxRootHub`

A handle to a UCX object that represents the root hub.

`Request`

Contains the <a href="..\usb\ns-usb-_urb.md">URB</a> for the root hub interrupt transfer request.


## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188048">UcxRootHubCreate</a>
 method.

 The <i>Request</i> parameter contains a buffer in which each bit corresponds to a root
    hub port, with the first bit corresponding to the first port.  The
    client driver sets the corresponding bit if any port has changed, and then completes the request.

The client driver returns completion status in <i>Request</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxroothub.h (include Ucxclass.h) |
| **IRQL** | DISPATCH_LEVEL |