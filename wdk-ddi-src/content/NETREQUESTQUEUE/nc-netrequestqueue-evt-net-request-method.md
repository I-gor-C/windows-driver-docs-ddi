---
UID: NC.netrequestqueue.EVT_NET_REQUEST_METHOD
title: EVT_NET_REQUEST_METHOD
author: windows-driver-content
description: 
ms.assetid: f83264cf-deb3-42c7-af27-205b1c12a8f9
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

# EVT_NET_REQUEST_METHOD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_REQUEST_METHOD EvtNetRequestMethod; 

// Definition

VOID EvtNetRequestMethod 
(
	NETREQUESTQUEUE RequestQueue
	NETREQUEST Request
	PVOID InputOutputBuffer
	UINT InputBufferLength
	UINT OutputBufferLength
)
{...}

EVT_NET_REQUEST_METHOD PFN_NET_REQUEST_METHOD


```

## -parameters

### -param RequestQueue: 
### -param Request: 
### -param InputOutputBuffer: 
### -param InputBufferLength: 
### -param OutputBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also