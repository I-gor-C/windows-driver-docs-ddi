---
UID: NC.wdfcommonbuffer.PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS
title: PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS
author: windows-driver-content
description: 
ms.assetid: 21fa90ac-240d-471a-94ad-7f014d10a7d0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcommonbuffer.h
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

# PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS PfnWdfcommonbuffergetalignedvirtualaddress; 

// Definition

WDFAPI PfnWdfcommonbuffergetalignedvirtualaddress 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMMONBUFFER CommonBuffer
)
{...}

PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS 


```

## -parameters

### -param DriverGlobals: 
### -param CommonBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also