---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR
title: PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 4365329d-0622-440e-81cf-67eef48c6ece
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfresource.h
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

# PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR PfnWdfioresourcelistupdatedescriptor; 

// Definition

WDFAPI PfnWdfioresourcelistupdatedescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESLIST ResourceList
	PIO_RESOURCE_DESCRIPTOR Descriptor
	ULONG Index
)
{...}

PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param ResourceList: 
### -param Descriptor: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also