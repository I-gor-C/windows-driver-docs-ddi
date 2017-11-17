---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTGETDESCRIPTOR
title: PFN_WDFIORESOURCELISTGETDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 5ac39093-953d-414c-8cc6-1bd1d6ec12c0
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

# PFN_WDFIORESOURCELISTGETDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTGETDESCRIPTOR PfnWdfioresourcelistgetdescriptor; 

// Definition

WDFAPI PfnWdfioresourcelistgetdescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESLIST ResourceList
	ULONG Index
)
{...}

PFN_WDFIORESOURCELISTGETDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param ResourceList: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also