---
UID: NC.wdffileobject.PFN_WDFFILEOBJECTWDMGETFILEOBJECT
title: PFN_WDFFILEOBJECTWDMGETFILEOBJECT
author: windows-driver-content
description: 
ms.assetid: a17e4fa4-8f83-4d6a-b4d0-ae1ff3c1a92f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffileobject.h
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

# PFN_WDFFILEOBJECTWDMGETFILEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFILEOBJECTWDMGETFILEOBJECT PfnWdffileobjectwdmgetfileobject; 

// Definition

WDFAPI PfnWdffileobjectwdmgetfileobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFFILEOBJECT FileObject
)
{...}

PFN_WDFFILEOBJECTWDMGETFILEOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param FileObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also