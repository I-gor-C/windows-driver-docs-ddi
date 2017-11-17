---
UID: NC.wdfresource.PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR
title: PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 716cf85e-4fe2-4f42-8dc3-c4cb48f476d2
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

# PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR PfnWdfcmresourcelistremovebydescriptor; 

// Definition

WDFAPI PfnWdfcmresourcelistremovebydescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCMRESLIST List
	PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor
)
{...}

PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param List: 
### -param Descriptor: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also