---
UID: NC.extsfns.PGET_POOL_TAG_DESCRIPTION
title: PGET_POOL_TAG_DESCRIPTION
author: windows-driver-content
description: 
ms.assetid: af0a5314-cf31-4638-b544-a113188035b0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PGET_POOL_TAG_DESCRIPTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_POOL_TAG_DESCRIPTION PgetPoolTagDescription; 

// Definition

HRESULT PgetPoolTagDescription 
(
	ULONG PoolTag
	PDEBUG_POOLTAG_DESCRIPTION pDescription
)
{...}

PGET_POOL_TAG_DESCRIPTION 


```

## -parameters

### -param PoolTag: 
### -param pDescription: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also