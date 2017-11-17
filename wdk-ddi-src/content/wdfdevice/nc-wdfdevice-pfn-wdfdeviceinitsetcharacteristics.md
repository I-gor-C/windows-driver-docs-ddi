---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETCHARACTERISTICS
title: PFN_WDFDEVICEINITSETCHARACTERISTICS
author: windows-driver-content
description: 
ms.assetid: 5c5afdad-2029-4780-b738-c879307d64f7
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

# PFN_WDFDEVICEINITSETCHARACTERISTICS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETCHARACTERISTICS PfnWdfdeviceinitsetcharacteristics; 

// Definition

WDFAPI PfnWdfdeviceinitsetcharacteristics 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	ULONG DeviceCharacteristics
	BOOLEAN OrInValues
)
{...}

PFN_WDFDEVICEINITSETCHARACTERISTICS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceCharacteristics: 
### -param OrInValues: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also