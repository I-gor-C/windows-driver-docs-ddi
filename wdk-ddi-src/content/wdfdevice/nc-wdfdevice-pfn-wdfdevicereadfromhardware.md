---
UID: NC.wdfdevice.PFN_WDFDEVICEREADFROMHARDWARE
title: PFN_WDFDEVICEREADFROMHARDWARE
author: windows-driver-content
description: 
ms.assetid: feb41404-2b3e-4ece-8a1c-4930b21c3daa
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

# PFN_WDFDEVICEREADFROMHARDWARE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEREADFROMHARDWARE PfnWdfdevicereadfromhardware; 

// Definition

WDFAPI PfnWdfdevicereadfromhardware 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDF_DEVICE_HWACCESS_TARGET_TYPE Type
	WDF_DEVICE_HWACCESS_TARGET_SIZE Size
	PVOID TargetAddress
	PVOID Buffer
	ULONG Count
)
{...}

PFN_WDFDEVICEREADFROMHARDWARE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Type: 
### -param Size: 
### -param TargetAddress: 
### -param Buffer: 
### -param Count: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also