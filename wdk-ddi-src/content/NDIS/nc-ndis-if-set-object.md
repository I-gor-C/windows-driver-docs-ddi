---
UID: NC.ndis.IF_SET_OBJECT
title: IF_SET_OBJECT
author: windows-driver-content
description: 
ms.assetid: 200d90b7-754d-4d0c-aced-a50f24bb6b3c
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

# IF_SET_OBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IF_SET_OBJECT IfSetObject; 

// Definition

NDIS_STATUS() IfSetObject 
(
	NDIS_HANDLE ProviderIfContext
	NET_IF_OBJECT_ID ObjectId
	ULONG InputBufferLength
	PVOID pInputBuffer
)
{...}

IF_SET_OBJECT IFP_SET_OBJECT


```

## -parameters

### -param ProviderIfContext: 
### -param ObjectId: 
### -param InputBufferLength: 
### -param pInputBuffer: 



## -returns

Returns NDIS_STATUS() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also