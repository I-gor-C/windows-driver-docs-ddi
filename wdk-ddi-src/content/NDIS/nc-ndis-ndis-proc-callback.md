---
UID: NC.ndis.NDIS_PROC_CALLBACK
title: NDIS_PROC_CALLBACK
author: windows-driver-content
description: 
ms.assetid: fe64a4dd-5d77-43c0-8802-40e5cbcc7b19
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

# NDIS_PROC_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_PROC_CALLBACK NdisProcCallback; 

// Definition

_IRQL_requires_same_ VOID NdisProcCallback 
(
	_NDIS_WORK_ITEM * WorkItem
	PVOID Context
)
{...}

NDIS_PROC_CALLBACK NDIS_PROC


```

## -parameters

### -param WorkItem: 
### -param Context: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also