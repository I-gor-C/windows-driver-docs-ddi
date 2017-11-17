---
UID: NC.wdfregistry.PFN_WDFREGISTRYQUERYULONG
title: PFN_WDFREGISTRYQUERYULONG
author: windows-driver-content
description: 
ms.assetid: 77325e48-27d4-4c1e-ac2b-517063bcb248
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

# PFN_WDFREGISTRYQUERYULONG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYQUERYULONG PfnWdfregistryqueryulong; 

// Definition

WDFAPI PfnWdfregistryqueryulong 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	PULONG Value
)
{...}

PFN_WDFREGISTRYQUERYULONG 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param Value: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also