---
UID : NC:ucxendpoint.EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
title : EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
author : windows-driver-content
description : The client driver's implementation that UCX calls to notify the controller driver that it can complete cancelled transfers on the endpoint.
old-location : buses\evt_ucx_endpoint_ok_to_cancel_transfers.htm
old-project : usbref
ms.assetid : 3cb30b74-d50d-49dd-ab5d-de1cf71facd4
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.evt_ucx_endpoint_ok_to_cancel_transfers, EvtUcxEndpointOkToCancelTransfers callback function [Buses], EvtUcxEndpointOkToCancelTransfers, EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS, EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS, ucxendpoint/EvtUcxEndpointOkToCancelTransfers, PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS callback function pointer [Buses], PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS
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


# EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS function
The client driver's implementation that UCX calls to notify the controller driver that it can complete cancelled transfers on the
    endpoint.

## Syntax

```
EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS EvtUcxEndpointOkToCancelTransfers;

void EvtUcxEndpointOkToCancelTransfers(
  UCXENDPOINT UcxEndpoint
)
{...}
```

## Parameters

`UcxEndpoint`




## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointcreate.md">UcxEndpointCreate</a>
 method.

Before completing the URB associated with the transfer, the client driver calls <a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointneedtocanceltransfers.md">UcxEndpointNeedToCancelTransfers</a>
and then waits for UCX to call this function. Then the client driver can complete the URB with <b>STATUS_CANCELLED</b>.
<div class="alert"><b>Note</b>  If GUID_USB_CAPABILITY_CLEAR_TT_BUFFER_ON_ASYNC_TRANSFER_CANCEL capability
    is supported, the hub driver may send a control transfer to
    clear the TT (Transaction Translator) buffer before UCX calls this function.</div><div> </div>

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