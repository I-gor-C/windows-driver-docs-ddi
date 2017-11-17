---
UID: NC.netrequestqueue.EVT_NET_REQUEST_SET_DATA
title: EVT_NET_REQUEST_SET_DATA
author: windows-driver-content
description: 
ms.assetid: a747761d-c00e-44b6-980c-aa819841c9f8
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

# EVT_NET_REQUEST_SET_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_REQUEST_SET_DATA EvtNetRequestSetData; 

// Definition

VOID EvtNetRequestSetData 
(
	NETREQUESTQUEUE RequestQueue
	NETREQUEST Request
	PVOID InputBuffer
	UINT InputBufferLength
)
{...}

EVT_NET_REQUEST_SET_DATA PFN_NET_REQUEST_SET_DATA


```

## -parameters

### -param RequestQueue: 
### -param Request: 
### -param InputBuffer: 
### -param InputBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also