---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONQUERYBINARY
title: PFN_NETCONFIGURATIONQUERYBINARY
author: windows-driver-content
description: 
ms.assetid: 147a591a-062e-4e0b-91ff-bc4553897d2d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netconfiguration.h
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

# PFN_NETCONFIGURATIONQUERYBINARY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONQUERYBINARY PfnNetconfigurationquerybinary; 

// Definition

WDFAPI PfnNetconfigurationquerybinary 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING ValueName
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES MemoryAttributes
	WDFMEMORY *Memory
)
{...}

PFN_NETCONFIGURATIONQUERYBINARY 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param ValueName: 
### -param POOL_TYPE: 
### -param MemoryAttributes: 
### -param *Memory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also