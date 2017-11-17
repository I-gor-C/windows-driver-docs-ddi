---
UID: NC.ndis.IF_QUERY_OBJECT
title: IF_QUERY_OBJECT
author: windows-driver-content
description: 
ms.assetid: 536629d6-ecee-42b6-8719-43c86cef7cf0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# IF_QUERY_OBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IF_QUERY_OBJECT IfQueryObject; 

// Definition

NDIS_STATUS() IfQueryObject 
(
	NDIS_HANDLE ProviderIfContext
	NET_IF_OBJECT_ID ObjectId
	PULONG pOutputBufferLength
	PVOID pOutputBuffer
)
{...}

IF_QUERY_OBJECT IFP_QUERY_OBJECT


```

## -parameters

### -param ProviderIfContext: 
### -param ObjectId: 
### -param pOutputBufferLength: 
### -param pOutputBuffer: 



## -returns

Returns NDIS_STATUS() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also