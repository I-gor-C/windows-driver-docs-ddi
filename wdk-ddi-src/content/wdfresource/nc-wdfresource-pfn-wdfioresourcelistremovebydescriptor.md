---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR
title: PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 380a3796-85e2-4e75-9393-769a01ffb112
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

# PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR PfnWdfioresourcelistremovebydescriptor; 

// Definition

WDFAPI PfnWdfioresourcelistremovebydescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESLIST ResourceList
	PIO_RESOURCE_DESCRIPTOR Descriptor
)
{...}

PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param ResourceList: 
### -param Descriptor: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also