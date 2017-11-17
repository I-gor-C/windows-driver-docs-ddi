---
UID: NC.unknown.PFNCREATEINSTANCE
title: PFNCREATEINSTANCE
author: windows-driver-content
description: 
ms.assetid: 25a1e652-30cc-41d5-a287-f6953ad8968b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: unknown.h
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

# PFNCREATEINSTANCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNCREATEINSTANCE Pfncreateinstance; 

// Definition

HRESULT Pfncreateinstance 
(
	OUT PUNKNOWN *Unknown
	IN REFCLSID ClassId
	IN PUNKNOWN OuterUnknown
	IN POOL_TYPE PoolType
)
{...}

PFNCREATEINSTANCE 


```

## -parameters

### -param *Unknown: 
### -param ClassId: 
### -param OuterUnknown: 
### -param PoolType: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also