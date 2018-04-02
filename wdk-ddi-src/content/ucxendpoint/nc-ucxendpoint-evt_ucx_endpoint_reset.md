---
UID: NC:ucxendpoint.EVT_UCX_ENDPOINT_RESET
title: EVT_UCX_ENDPOINT_RESET
author: windows-driver-content
description: The client driver's implementation that UCX calls to reset the controller’s programming for an endpoint.
old-location: buses\evt_ucx_endpoint_reset.htm
old-project: usbref
ms.assetid: 927fdd48-416e-4e8f-a29c-c2799952197e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: EVT_UCX_ENDPOINT_RESET, EvtUcxEndpointReset, EvtUcxEndpointReset callback function [Buses], PEVT_UCX_ENDPOINT_RESET, PEVT_UCX_ENDPOINT_RESET callback function pointer [Buses], buses.evt_ucx_endpoint_reset, ucxendpoint/EvtUcxEndpointReset
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ucxendpoint.h
api_name:
-	PEVT_UCX_ENDPOINT_RESET
product: Windows
targetos: Windows
req.typenames: UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS_CHANGE_FLAGS
req.product: Windows 10 or later.
---


# EVT_UCX_ENDPOINT_RESET callback function
The client driver's implementation that UCX calls to reset the controller’s programming for an endpoint.

## Syntax

```
EVT_UCX_ENDPOINT_RESET EvtUcxEndpointReset;

void EvtUcxEndpointReset(
  UCXCONTROLLER UcxController,
  UCXENDPOINT UcxEndpoint,
  WDFREQUEST Request
)
{...}
```

## Parameters

`UcxController`

A handle to the UCX controller that the client driver received in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188033">UcxControllerCreate</a> method.

`UcxEndpoint`



`Request`

A handle to a framework request object that the client driver completes when the reset operation is finished.


## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>
 method.

The client driver returns completion status in the WDFREQUEST, which it might complete
    asynchronously.


#### Examples

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>VOID
Endpoint_EvtUcxEndpointReset(
    UCXCONTROLLER   UcxController,
    UCXENDPOINT     UcxEndpoint,
    WDFREQUEST      Request
)

{
    UNREFERENCED_PARAMETER(UcxController);
    UNREFERENCED_PARAMETER(UcxEndpoint);

    DbgTrace(TL_INFO, Endpoint, "Endpoint_EvtUcxEndpointReset");

    WdfRequestComplete(Request, STATUS_SUCCESS);
}</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxendpoint.h (include Ucxclass.h, Ucxendpoint.h) |
| **IRQL** | DISPATCH_LEVEL |