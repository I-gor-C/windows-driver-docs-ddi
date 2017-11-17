---
UID: NC.ntifs.PRELEASE_FROM_LAZY_WRITE
title: PRELEASE_FROM_LAZY_WRITE
author: windows-driver-content
description: 
ms.assetid: 039fdf3b-0f95-4e0b-80c5-1d8d3ba8e176
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PRELEASE_FROM_LAZY_WRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRELEASE_FROM_LAZY_WRITE PreleaseFromLazyWrite; 

// Definition

VOID PreleaseFromLazyWrite 
(
	PVOID Context
)
{...}

PRELEASE_FROM_LAZY_WRITE 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also