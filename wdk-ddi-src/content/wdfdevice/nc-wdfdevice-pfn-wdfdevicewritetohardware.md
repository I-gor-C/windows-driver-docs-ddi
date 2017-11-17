---
UID: NC.wdfdevice.PFN_WDFDEVICEWRITETOHARDWARE
title: PFN_WDFDEVICEWRITETOHARDWARE
author: windows-driver-content
description: 
ms.assetid: 438f7d0e-dffd-45c1-bf34-fc16eebc771a
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

# PFN_WDFDEVICEWRITETOHARDWARE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEWRITETOHARDWARE PfnWdfdevicewritetohardware; 

// Definition

WDFAPI PfnWdfdevicewritetohardware 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDF_DEVICE_HWACCESS_TARGET_TYPE Type
	WDF_DEVICE_HWACCESS_TARGET_SIZE Size
	PVOID TargetAddress
	SIZE_T Value
	PVOID Buffer
	ULONG Count
)
{...}

PFN_WDFDEVICEWRITETOHARDWARE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Type: 
### -param Size: 
### -param TargetAddress: 
### -param Value: 
### -param Buffer: 
### -param Count: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also