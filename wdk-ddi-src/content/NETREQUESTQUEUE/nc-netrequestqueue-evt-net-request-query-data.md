---
UID: NC.netrequestqueue.EVT_NET_REQUEST_QUERY_DATA
title: EVT_NET_REQUEST_QUERY_DATA
author: windows-driver-content
description: 
ms.assetid: 57b81168-3631-4b76-bd38-3759fdc41e88
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequestqueue.h
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

# EVT_NET_REQUEST_QUERY_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_REQUEST_QUERY_DATA EvtNetRequestQueryData; 

// Definition

VOID EvtNetRequestQueryData 
(
	NETREQUESTQUEUE RequestQueue
	NETREQUEST Request
	PVOID OutputBuffer
	UINT OutputBufferLength
)
{...}

EVT_NET_REQUEST_QUERY_DATA PFN_NET_REQUEST_QUERY_DATA


```

## -parameters

### -param RequestQueue: 
### -param Request: 
### -param OutputBuffer: 
### -param OutputBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also