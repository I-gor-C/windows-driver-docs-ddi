---
UID : NC:ucxendpoint.EVT_UCX_ENDPOINT_START
title : EVT_UCX_ENDPOINT_START
author : windows-driver-content
description : The client driver's implementation that UCX calls to start the queue associated with the endpoint.
old-location : buses\evt_ucx_endpoint_start.htm
old-project : usbref
ms.assetid : 8b801255-ee6a-413f-8ce3-3a3696283e6b
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.evt_ucx_endpoint_start, EvtUcxEndpointStart callback function [Buses], EvtUcxEndpointStart, EVT_UCX_ENDPOINT_START, EVT_UCX_ENDPOINT_START, ucxendpoint/EvtUcxEndpointStart, PEVT_UCX_ENDPOINT_START callback function pointer [Buses], PEVT_UCX_ENDPOINT_START
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ucxendpoint.h
req.include-header : Ucxclass.h, Ucxendpoint.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS_CHANGE_FLAGS
req.product : Windows 10 or later.
---


# EVT_UCX_ENDPOINT_START function
The client driver's implementation that UCX calls to start the queue associated with the endpoint.

## Syntax

```
EVT_UCX_ENDPOINT_START EvtUcxEndpointStart;

void EvtUcxEndpointStart(
  UCXCONTROLLER UcxController,
  UCXENDPOINT UcxEndpoint
)
{...}
```

## Parameters

`UcxController`

A handle to the UCX controller that the client driver received in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188033">UcxControllerCreate</a> method.

`UcxEndpoint`




## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointcreate.md">UcxEndpointCreate</a>
 method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxendpoint.h (include Ucxclass.h, Ucxendpoint.h) |
| **Library** |  |
| **IRQL** | DISPATCH_LEVEL |
| **DDI compliance rules** |  |