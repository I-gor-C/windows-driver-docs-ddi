---
UID: NF:ucxendpoint.UCX_ENDPOINT_EVENT_CALLBACKS_INIT
title: UCX_ENDPOINT_EVENT_CALLBACKS_INIT function
author: windows-driver-content
description: Initializes a UCX_ENDPOINT_EVENT_CALLBACKS structure with client driver's callback functions. The client driver calls this function before calling UcxEndpointCreate method to create an endpoint and register its callback functions with UCX.
old-location: buses\_ucx_endpoint_event_callbacks_init.htm
old-project: usbref
ms.assetid: 1890052A-EE98-4749-ACF9-8321148F3828
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: UCX_ENDPOINT_EVENT_CALLBACKS_INIT, UCX_ENDPOINT_EVENT_CALLBACKS_INIT function [Buses], buses._ucx_endpoint_event_callbacks_init, ucxendpoint/UCX_ENDPOINT_EVENT_CALLBACKS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxendpoint.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ucxendpoint.h
api_name:
-	UCX_ENDPOINT_EVENT_CALLBACKS_INIT
product: Windows
targetos: Windows
req.typenames: UCX_ENDPOINT_CHARACTERISTIC_TYPE
req.product: Windows 10 or later.
---


# UCX_ENDPOINT_EVENT_CALLBACKS_INIT function
Initializes a <a href="..\ucxendpoint\ns-ucxendpoint-_ucx_endpoint_event_callbacks.md">UCX_ENDPOINT_EVENT_CALLBACKS</a> structure with client driver's callback functions. The client driver calls this function before calling <a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointcreate.md">UcxEndpointCreate</a> method to create an endpoint and register its callback functions with UCX.

## Syntax

````
void UCX_ENDPOINT_EVENT_CALLBACKS_INIT(
  _Out_ PUCX_ENDPOINT_EVENT_CALLBACKS                Callbacks,
  _In_  PEVT_UCX_ENDPOINT_PURGE                      EvtEndpointPurge,
  _In_  PEVT_UCX_ENDPOINT_START                      EvtEndpointStart,
  _In_  PEVT_UCX_ENDPOINT_ABORT                      EvtEndpointAbort,
  _In_  PEVT_UCX_ENDPOINT_RESET                      EvtEndpointReset,
  _In_  PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS     EvtEndpointOkToCancelTransfers,
  _In_  PEVT_UCX_ENDPOINT_STATIC_STREAMS_ADD         EvtEndpointStaticStreamsAdd,
  _In_  PEVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE      EvtEndpointStaticStreamsEnable,
  _In_  PEVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE     EvtEndpointStaticStreamsDisable
);
````

## Parameters

`Callbacks`

A pointer to a <a href="..\ucxendpoint\ns-ucxendpoint-_ucx_endpoint_event_callbacks.md">UCX_ENDPOINT_EVENT_CALLBACKS</a> structure that contains pointers to the client driver's event callback functions.

`EvtEndpointPurge`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_purge.md">EVT_UCX_ENDPOINT_PURGE</a>                     event callback function.

`EvtEndpointStart`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_start.md">EVT_UCX_ENDPOINT_START</a>                     event callback function.

`EvtEndpointAbort`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_abort.md">EVT_UCX_ENDPOINT_ABORT</a>                     event callback function.

`EvtEndpointReset`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_reset.md">EVT_UCX_ENDPOINT_RESET</a>                     event callback function.

`EvtEndpointOkToCancelTransfers`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_ok_to_cancel_transfers.md">EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS</a>    event callback function.

`EvtEndpointStaticStreamsAdd`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_static_streams_add.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</a>        event callback function.

`EvtEndpointStaticStreamsEnable`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_static_streams_enable.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE</a>     event callback function.

`EvtEndpointStaticStreamsDisable`

A pointer to client driver's implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_static_streams_disable.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE</a>    event callback function.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10  |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxendpoint.h (include Ucxclass.h) |

## See Also

<a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointcreate.md">UcxEndpointCreate</a>