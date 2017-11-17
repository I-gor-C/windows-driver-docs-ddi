---
UID: NC.wdm.SET_D3COLD_SUPPORT
title: SET_D3COLD_SUPPORT
author: windows-driver-content
description: 
ms.assetid: 6a458c74-37ae-44ea-aefd-1e3ee9631ef4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# SET_D3COLD_SUPPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SET_D3COLD_SUPPORT SetD3coldSupport; 

// Definition

VOID SetD3coldSupport 
(
	PVOID Context
	BOOLEAN D3ColdSupport
)
{...}

SET_D3COLD_SUPPORT PSET_D3COLD_SUPPORT


```

## -parameters

### -param Context: 
### -param D3ColdSupport: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also