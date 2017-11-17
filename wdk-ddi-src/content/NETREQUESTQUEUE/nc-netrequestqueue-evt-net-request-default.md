---
UID: NC.netrequestqueue.EVT_NET_REQUEST_DEFAULT
title: EVT_NET_REQUEST_DEFAULT
author: windows-driver-content
description: 
ms.assetid: ffe726cc-c9db-4748-8c2d-6fd77ad5f297
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

# EVT_NET_REQUEST_DEFAULT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_REQUEST_DEFAULT EvtNetRequestDefault; 

// Definition

VOID EvtNetRequestDefault 
(
	NETREQUESTQUEUE RequestQueue
	NETREQUEST Request
	NDIS_REQUEST_TYPE RequestType
	NDIS_OID Oid
	PVOID InputOutputBuffer
	UINT InputBufferLength
	UINT OutputBufferLength
)
{...}

EVT_NET_REQUEST_DEFAULT PFN_NET_REQUEST_DEFAULT


```

## -parameters

### -param RequestQueue: 
### -param Request: 
### -param RequestType: 
### -param Oid: 
### -param InputOutputBuffer: 
### -param InputBufferLength: 
### -param OutputBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also