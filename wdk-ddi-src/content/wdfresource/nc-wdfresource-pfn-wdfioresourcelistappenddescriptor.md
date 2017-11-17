---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR
title: PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: f5c3a861-1900-493d-aa5c-cdf04bf901b2
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

# PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR PfnWdfioresourcelistappenddescriptor; 

// Definition

WDFAPI PfnWdfioresourcelistappenddescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESLIST ResourceList
	PIO_RESOURCE_DESCRIPTOR Descriptor
)
{...}

PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR 


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