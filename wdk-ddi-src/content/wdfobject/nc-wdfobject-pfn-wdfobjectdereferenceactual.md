---
UID: NC.wdfobject.PFN_WDFOBJECTDEREFERENCEACTUAL
title: PFN_WDFOBJECTDEREFERENCEACTUAL
author: windows-driver-content
description: 
ms.assetid: 17814cb1-14be-422c-9e1f-c262d43c4b90
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

# PFN_WDFOBJECTDEREFERENCEACTUAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTDEREFERENCEACTUAL PfnWdfobjectdereferenceactual; 

// Definition

WDFAPI PfnWdfobjectdereferenceactual 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFOBJECT Handle
	PVOID Tag
	LONG Line
	PCCH File
)
{...}

PFN_WDFOBJECTDEREFERENCEACTUAL 


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