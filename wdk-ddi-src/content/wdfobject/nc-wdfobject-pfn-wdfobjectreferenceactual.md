---
UID: NC.wdfobject.PFN_WDFOBJECTREFERENCEACTUAL
title: PFN_WDFOBJECTREFERENCEACTUAL
author: windows-driver-content
description: 
ms.assetid: 105ee613-4f22-4d76-b55a-35acfb664e87
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfobject.h
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

# PFN_WDFOBJECTREFERENCEACTUAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTREFERENCEACTUAL PfnWdfobjectreferenceactual; 

// Definition

WDFAPI PfnWdfobjectreferenceactual 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFOBJECT Handle
	PVOID Tag
	LONG Line
	PCCH File
)
{...}

PFN_WDFOBJECTREFERENCEACTUAL 


```

## -parameters

### -param DriverGlobals: 
### -param Handle: 
### -param Tag: 
### -param Line: 
### -param File: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also