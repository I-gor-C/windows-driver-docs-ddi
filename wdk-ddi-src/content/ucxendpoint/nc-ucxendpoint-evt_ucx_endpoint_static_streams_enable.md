---
UID: NC:ucxendpoint.EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE
title: EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE
author: windows-driver-content
description: The client driver's implementation that UCX calls to enable the static streams.
old-location: buses\evt_ucx_endpoint_static_streams_enable.htm
old-project: usbref
ms.assetid: eb40623f-b13f-4c3f-b3ac-687cba323ce2
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: buses.evt_ucx_endpoint_static_streams_enable, EvtUcxEndpointStaticStreamsEnable callback function [Buses], EvtUcxEndpointStaticStreamsEnable, EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE, EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE, ucxendpoint/EvtUcxEndpointStaticStreamsEnable, PFN_UCM_CONNECTOR_GET_OPERATING_MODE callback function pointer [Buses], PFN_UCM_CONNECTOR_GET_OPERATING_MODE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	ucxendpoint.h
apiname:
-	PFN_UCM_CONNECTOR_GET_OPERATING_MODE
product: Windows
targetos: Windows
req.typenames: UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS_CHANGE_FLAGS
req.product: Windows 10 or later.
---


# EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE function
The client driver's implementation that UCX calls to enable the static streams.

## Syntax

```
EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE EvtUcxEndpointStaticStreamsEnable;

void EvtUcxEndpointStaticStreamsEnable(
  UCXENDPOINT UcxEndpoint,
  UCXSSTREAMS UcxStaticStreams,
  WDFREQUEST Request
)
{...}
```

## Parameters

`UcxEndpoint`



`UcxStaticStreams`

A handle to a UCX object that represents the static streams.

`Request`

Contains the URB for the <b>URB_FUNCTION_OPEN_STATIC_STREAMS</b>.


## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointcreate.md">UcxEndpointCreate</a>
 method.

The client driver returns completion status in <i>Request</i> and in the USBD_STATUS
    in the URB header.  The driver can complete the WDFREQUEST asynchronously.


#### Examples

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>VOID
Endpoint_EvtUcxEndpointStaticStreamsEnable(
    UCXENDPOINT     UcxEndpoint,
    UCXSSTREAMS     UcxStaticStreams,
    WDFREQUEST      Request
)

{
    UNREFERENCED_PARAMETER(UcxEndpoint);
    UNREFERENCED_PARAMETER(UcxStaticStreams);

    DbgTrace(TL_INFO, Endpoint, "Endpoint_EvtUcxEndpointStaticStreamsEnable");

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