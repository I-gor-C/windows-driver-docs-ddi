---
UID: NC.extsfns.PGET_POOL_DATA
title: PGET_POOL_DATA
author: windows-driver-content
description: 
ms.assetid: 680d0a04-ccc1-4391-a9ee-594dc702a952
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

# PGET_POOL_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_POOL_DATA PgetPoolData; 

// Definition

HRESULT PgetPoolData 
(
	PDEBUG_CLIENT Client
	ULONG64 Pool
	PDEBUG_POOL_DATA PoolData
)
{...}

PGET_POOL_DATA 


```

## -parameters

### -param Client: 
### -param Pool: 
### -param PoolData: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also