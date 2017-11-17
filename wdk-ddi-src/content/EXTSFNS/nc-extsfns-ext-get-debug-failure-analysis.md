---
UID: NC.extsfns.EXT_GET_DEBUG_FAILURE_ANALYSIS
title: EXT_GET_DEBUG_FAILURE_ANALYSIS
author: windows-driver-content
description: 
ms.assetid: 0e484f39-b4a3-4783-be30-77e05bf08983
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

# EXT_GET_DEBUG_FAILURE_ANALYSIS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_GET_DEBUG_FAILURE_ANALYSIS ExtGetDebugFailureAnalysis; 

// Definition

HRESULT ExtGetDebugFailureAnalysis 
(
	PDEBUG_CLIENT4 Client
	ULONG Flags
	CLSID pIIdFailureAnalysis
	PDEBUG_FAILURE_ANALYSIS2 *Analysis
)
{...}

EXT_GET_DEBUG_FAILURE_ANALYSIS 


```

## -parameters

### -param Client: 
### -param Flags: 
### -param pIIdFailureAnalysis: 
### -param *Analysis: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also