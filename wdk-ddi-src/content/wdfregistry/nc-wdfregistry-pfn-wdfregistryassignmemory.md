---
UID: NC.wdfregistry.PFN_WDFREGISTRYASSIGNMEMORY
title: PFN_WDFREGISTRYASSIGNMEMORY
author: windows-driver-content
description: 
ms.assetid: 2d9e4247-fbcb-405d-9bcf-0d08a7dc551d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfregistry.h
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

# PFN_WDFREGISTRYASSIGNMEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYASSIGNMEMORY PfnWdfregistryassignmemory; 

// Definition

WDFAPI PfnWdfregistryassignmemory 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	ULONG ValueType
	WDFMEMORY Memory
	PWDFMEMORY_OFFSET MemoryOffsets
)
{...}

PFN_WDFREGISTRYASSIGNMEMORY 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param ValueType: 
### -param Memory: 
### -param MemoryOffsets: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also