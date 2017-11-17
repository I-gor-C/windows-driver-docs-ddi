---
UID: NC.wdfregistry.PFN_WDFREGISTRYASSIGNULONG
title: PFN_WDFREGISTRYASSIGNULONG
author: windows-driver-content
description: 
ms.assetid: 46049756-b875-44aa-a4b9-fff428ecdbea
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

# PFN_WDFREGISTRYASSIGNULONG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYASSIGNULONG PfnWdfregistryassignulong; 

// Definition

WDFAPI PfnWdfregistryassignulong 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	ULONG Value
)
{...}

PFN_WDFREGISTRYASSIGNULONG 


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