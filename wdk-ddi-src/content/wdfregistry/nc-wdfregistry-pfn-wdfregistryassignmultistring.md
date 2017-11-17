---
UID: NC.wdfregistry.PFN_WDFREGISTRYASSIGNMULTISTRING
title: PFN_WDFREGISTRYASSIGNMULTISTRING
author: windows-driver-content
description: 
ms.assetid: 3381d513-45a7-4094-b407-192ec72dd6bf
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

# PFN_WDFREGISTRYASSIGNMULTISTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYASSIGNMULTISTRING PfnWdfregistryassignmultistring; 

// Definition

WDFAPI PfnWdfregistryassignmultistring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
	WDFCOLLECTION StringsCollection
)
{...}

PFN_WDFREGISTRYASSIGNMULTISTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 
### -param StringsCollection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also