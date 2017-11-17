---
UID: NC.wdfregistry.PFN_WDFREGISTRYQUERYMEMORY
title: PFN_WDFREGISTRYQUERYMEMORY
author: windows-driver-content
description: 
ms.assetid: 44e08de1-a887-4cc4-b16a-16938794b217
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

# PFN_WDFREGISTRYQUERYMEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYQUERYMEMORY PfnWdfregistryquerymemory; 

// Definition

WDFAPI PfnWdfregistryquerymemory 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES MemoryAttributes
	WDFMEMORY *Memory
	PULONG ValueType
)
{...}

PFN_WDFREGISTRYQUERYMEMORY 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param POOL_TYPE: 
### -param MemoryAttributes: 
### -param *Memory: 
### -param ValueType: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also