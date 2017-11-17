---
UID: NC.wdfregistry.PFN_WDFREGISTRYQUERYVALUE
title: PFN_WDFREGISTRYQUERYVALUE
author: windows-driver-content
description: 
ms.assetid: ecfda3fc-3071-4216-8379-8dcc84f0f6f4
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

# PFN_WDFREGISTRYQUERYVALUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYQUERYVALUE PfnWdfregistryqueryvalue; 

// Definition

WDFAPI PfnWdfregistryqueryvalue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	ULONG ValueLength
	PVOID Value
	PULONG ValueLengthQueried
	PULONG ValueType
)
{...}

PFN_WDFREGISTRYQUERYVALUE 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param ValueLength: 
### -param Value: 
### -param ValueLengthQueried: 
### -param ValueType: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also