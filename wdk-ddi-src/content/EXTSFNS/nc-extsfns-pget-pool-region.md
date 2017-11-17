---
UID: NC.extsfns.PGET_POOL_REGION
title: PGET_POOL_REGION
author: windows-driver-content
description: 
ms.assetid: e29265d3-529e-4056-9c4f-67d9104ae89a
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

# PGET_POOL_REGION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_POOL_REGION PgetPoolRegion; 

// Definition

HRESULT PgetPoolRegion 
(
	PDEBUG_CLIENT Client
	ULONG64 Pool
	DEBUG_POOL_REGION *PoolRegion
)
{...}

PGET_POOL_REGION 


```

## -parameters

### -param Client: 
### -param Pool: 
### -param *PoolRegion: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also