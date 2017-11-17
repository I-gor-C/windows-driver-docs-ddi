---
UID: NC.wdfregistry.PFN_WDFREGISTRYQUERYMULTISTRING
title: PFN_WDFREGISTRYQUERYMULTISTRING
author: windows-driver-content
description: 
ms.assetid: 473186ed-05b5-46d5-a67e-eeab239ed1f7
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

# PFN_WDFREGISTRYQUERYMULTISTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYQUERYMULTISTRING PfnWdfregistryquerymultistring; 

// Definition

WDFAPI PfnWdfregistryquerymultistring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	PWDF_OBJECT_ATTRIBUTES StringsAttributes
	WDFCOLLECTION Collection
)
{...}

PFN_WDFREGISTRYQUERYMULTISTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param StringsAttributes: 
### -param Collection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also