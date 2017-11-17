---
UID: NC.wdfcommonbuffer.PFN_WDFCOMMONBUFFERGETALIGNEDLOGICALADDRESS
title: PFN_WDFCOMMONBUFFERGETALIGNEDLOGICALADDRESS
author: windows-driver-content
description: 
ms.assetid: 06e8e588-33b5-4114-9a58-981993aef8d6
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

# PFN_WDFCOMMONBUFFERGETALIGNEDLOGICALADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMMONBUFFERGETALIGNEDLOGICALADDRESS PfnWdfcommonbuffergetalignedlogicaladdress; 

// Definition

WDFAPI PfnWdfcommonbuffergetalignedlogicaladdress 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMMONBUFFER CommonBuffer
)
{...}

PFN_WDFCOMMONBUFFERGETALIGNEDLOGICALADDRESS 


```

## -parameters

### -param DriverGlobals: 
### -param CommonBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also