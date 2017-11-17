---
UID: NC.wdfstring.PFN_WDFSTRINGCREATE
title: PFN_WDFSTRINGCREATE
author: windows-driver-content
description: 
ms.assetid: 3a177436-16a7-483f-9908-3831c5f3f3f7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfstring.h
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

# PFN_WDFSTRINGCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFSTRINGCREATE PfnWdfstringcreate; 

// Definition

WDFAPI PfnWdfstringcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PCUNICODE_STRING UnicodeString
	PWDF_OBJECT_ATTRIBUTES StringAttributes
	WDFSTRING *String
)
{...}

PFN_WDFSTRINGCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param UnicodeString: 
### -param StringAttributes: 
### -param *String: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also