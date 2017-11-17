---
UID: NC.wdfstring.PFN_WDFSTRINGGETUNICODESTRING
title: PFN_WDFSTRINGGETUNICODESTRING
author: windows-driver-content
description: 
ms.assetid: 7ba71b25-78c3-4df3-8c3d-36ae6ad96c9f
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

# PFN_WDFSTRINGGETUNICODESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFSTRINGGETUNICODESTRING PfnWdfstringgetunicodestring; 

// Definition

WDFAPI PfnWdfstringgetunicodestring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFSTRING String
	PUNICODE_STRING UnicodeString
)
{...}

PFN_WDFSTRINGGETUNICODESTRING 


```

## -parameters

### -param DriverGlobals: 
### -param String: 
### -param UnicodeString: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also