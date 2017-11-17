---
UID: NC.wdfcommonbuffer.PFN_WDFCOMMONBUFFERCREATEWITHCONFIG
title: PFN_WDFCOMMONBUFFERCREATEWITHCONFIG
author: windows-driver-content
description: 
ms.assetid: 2951a3b3-73f4-43ac-9f0f-e36989e811d5
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

# PFN_WDFCOMMONBUFFERCREATEWITHCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMMONBUFFERCREATEWITHCONFIG PfnWdfcommonbuffercreatewithconfig; 

// Definition

WDFAPI PfnWdfcommonbuffercreatewithconfig 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
	size_t Length
	PWDF_COMMON_BUFFER_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFCOMMONBUFFER *CommonBuffer
)
{...}

PFN_WDFCOMMONBUFFERCREATEWITHCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 
### -param Length: 
### -param Config: 
### -param Attributes: 
### -param *CommonBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also