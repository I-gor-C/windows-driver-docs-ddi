---
UID: NC.wdfdevice.PFN_WDFDEVICECREATEDEVICEINTERFACE
title: PFN_WDFDEVICECREATEDEVICEINTERFACE
author: windows-driver-content
description: 
ms.assetid: 93159329-ffb8-488f-b1d1-1d4700443b15
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICECREATEDEVICEINTERFACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICECREATEDEVICEINTERFACE PfnWdfdevicecreatedeviceinterface; 

// Definition

WDFAPI PfnWdfdevicecreatedeviceinterface 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	CONST GUID
	PCUNICODE_STRING ReferenceString
)
{...}

PFN_WDFDEVICECREATEDEVICEINTERFACE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param GUID: 
### -param ReferenceString: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also