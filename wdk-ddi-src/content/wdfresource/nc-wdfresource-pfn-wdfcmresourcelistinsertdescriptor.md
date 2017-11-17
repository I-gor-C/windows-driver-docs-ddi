---
UID: NC.wdfresource.PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR
title: PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: d3d3b1eb-4ed9-4ad9-a587-48e174c8121e
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

# PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR PfnWdfcmresourcelistinsertdescriptor; 

// Definition

WDFAPI PfnWdfcmresourcelistinsertdescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCMRESLIST List
	PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor
	ULONG Index
)
{...}

PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param List: 
### -param Descriptor: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also