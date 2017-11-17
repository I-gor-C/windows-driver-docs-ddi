---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTINSERTDESCRIPTOR
title: PFN_WDFIORESOURCELISTINSERTDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: c353a3fb-1524-4e4a-9ef0-a7f7c7c098c8
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

# PFN_WDFIORESOURCELISTINSERTDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTINSERTDESCRIPTOR PfnWdfioresourcelistinsertdescriptor; 

// Definition

WDFAPI PfnWdfioresourcelistinsertdescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESLIST ResourceList
	PIO_RESOURCE_DESCRIPTOR Descriptor
	ULONG Index
)
{...}

PFN_WDFIORESOURCELISTINSERTDESCRIPTOR 


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