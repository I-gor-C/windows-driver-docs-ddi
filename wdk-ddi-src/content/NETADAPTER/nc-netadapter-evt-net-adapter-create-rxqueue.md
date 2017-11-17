---
UID: NC.netadapter.EVT_NET_ADAPTER_CREATE_RXQUEUE
title: EVT_NET_ADAPTER_CREATE_RXQUEUE
author: windows-driver-content
description: 
ms.assetid: d65115a9-94f5-4bfa-861b-215141f90b65
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netadapter.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# EVT_NET_ADAPTER_CREATE_RXQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_ADAPTER_CREATE_RXQUEUE EvtNetAdapterCreateRxqueue; 

// Definition

NTSTATUS EvtNetAdapterCreateRxqueue 
(
	NETADAPTER Adapter
	PNETRXQUEUE_INIT RxQueueInit
)
{...}

EVT_NET_ADAPTER_CREATE_RXQUEUE PFN_NET_ADAPTER_CREATE_RXQUEUE


```

## -parameters

### -param Adapter: 
### -param RxQueueInit: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also