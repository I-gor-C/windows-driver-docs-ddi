---
UID: NC.wdfregistry.PFN_WDFREGISTRYQUERYUNICODESTRING
title: PFN_WDFREGISTRYQUERYUNICODESTRING
author: windows-driver-content
description: 
ms.assetid: 532467f2-bed6-4d12-b48b-9db95a3e2377
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

# PFN_WDFREGISTRYQUERYUNICODESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYQUERYUNICODESTRING PfnWdfregistryqueryunicodestring; 

// Definition

WDFAPI PfnWdfregistryqueryunicodestring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	PUSHORT ValueByteLength
	PUNICODE_STRING Value
)
{...}

PFN_WDFREGISTRYQUERYUNICODESTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param ValueByteLength: 
### -param Value: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also