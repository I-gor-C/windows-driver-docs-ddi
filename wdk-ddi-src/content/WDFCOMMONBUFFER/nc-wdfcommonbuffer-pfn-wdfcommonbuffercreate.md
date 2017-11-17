---
UID: NC.wdfcommonbuffer.PFN_WDFCOMMONBUFFERCREATE
title: PFN_WDFCOMMONBUFFERCREATE
author: windows-driver-content
description: 
ms.assetid: 991f1da9-29b8-45d9-a1f9-57091bfb7649
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

# PFN_WDFCOMMONBUFFERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMMONBUFFERCREATE PfnWdfcommonbuffercreate; 

// Definition

WDFAPI PfnWdfcommonbuffercreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
	size_t Length
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFCOMMONBUFFER *CommonBuffer
)
{...}

PFN_WDFCOMMONBUFFERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 
### -param Length: 
### -param Attributes: 
### -param *CommonBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also