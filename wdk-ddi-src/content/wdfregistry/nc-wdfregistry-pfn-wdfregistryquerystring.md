---
UID: NC.wdfregistry.PFN_WDFREGISTRYQUERYSTRING
title: PFN_WDFREGISTRYQUERYSTRING
author: windows-driver-content
description: 
ms.assetid: f26506ae-ffa1-4df2-b342-35f75a742b15
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

# PFN_WDFREGISTRYQUERYSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYQUERYSTRING PfnWdfregistryquerystring; 

// Definition

WDFAPI PfnWdfregistryquerystring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	WDFSTRING String
)
{...}

PFN_WDFREGISTRYQUERYSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param String: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also