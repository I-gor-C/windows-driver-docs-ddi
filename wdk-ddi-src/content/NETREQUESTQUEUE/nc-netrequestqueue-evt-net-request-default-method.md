---
UID: NC.netrequestqueue.EVT_NET_REQUEST_DEFAULT_METHOD
title: EVT_NET_REQUEST_DEFAULT_METHOD
author: windows-driver-content
description: 
ms.assetid: f8e9add5-a7d7-4943-bab8-d28ecb73a3e9
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

# EVT_NET_REQUEST_DEFAULT_METHOD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_REQUEST_DEFAULT_METHOD EvtNetRequestDefaultMethod; 

// Definition

VOID EvtNetRequestDefaultMethod 
(
	NETREQUESTQUEUE RequestQueue
	NETREQUEST Request
	NDIS_OID Oid
	PVOID InputOutputBuffer
	UINT InputBufferLength
	UINT OutputBufferLength
)
{...}

EVT_NET_REQUEST_DEFAULT_METHOD PFN_NET_REQUEST_DEFAULT_METHOD


```

## -parameters

### -param RequestQueue: 
### -param Request: 
### -param Oid: 
### -param InputOutputBuffer: 
### -param InputBufferLength: 
### -param OutputBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also