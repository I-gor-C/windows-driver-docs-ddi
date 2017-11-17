---
UID: NC.wdfregistry.PFN_WDFREGISTRYASSIGNVALUE
title: PFN_WDFREGISTRYASSIGNVALUE
author: windows-driver-content
description: 
ms.assetid: 476ded70-3ddd-49c9-a95a-b2dc759a42fc
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

# PFN_WDFREGISTRYASSIGNVALUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYASSIGNVALUE PfnWdfregistryassignvalue; 

// Definition

WDFAPI PfnWdfregistryassignvalue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	ULONG ValueType
	ULONG ValueLength
	PVOID Value
)
{...}

PFN_WDFREGISTRYASSIGNVALUE 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param ValueType: 
### -param ValueLength: 
### -param Value: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also