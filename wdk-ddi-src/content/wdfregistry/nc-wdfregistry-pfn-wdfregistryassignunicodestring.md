---
UID: NC.wdfregistry.PFN_WDFREGISTRYASSIGNUNICODESTRING
title: PFN_WDFREGISTRYASSIGNUNICODESTRING
author: windows-driver-content
description: 
ms.assetid: e9a50436-3bc7-4958-8044-8571ebe727a3
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

# PFN_WDFREGISTRYASSIGNUNICODESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYASSIGNUNICODESTRING PfnWdfregistryassignunicodestring; 

// Definition

WDFAPI PfnWdfregistryassignunicodestring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	PCUNICODE_STRING Value
)
{...}

PFN_WDFREGISTRYASSIGNUNICODESTRING 


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