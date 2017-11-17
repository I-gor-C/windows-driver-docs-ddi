---
UID: NC.wdfdevice.PFN_WDFDEVICEUNMAPIOSPACE
title: PFN_WDFDEVICEUNMAPIOSPACE
author: windows-driver-content
description: 
ms.assetid: 40012fa0-476d-43ed-ac50-6eaf08f2a75b
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

# PFN_WDFDEVICEUNMAPIOSPACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEUNMAPIOSPACE PfnWdfdeviceunmapiospace; 

// Definition

WDFAPI PfnWdfdeviceunmapiospace 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PVOID PseudoBaseAddress
	SIZE_T NumberOfBytes
)
{...}

PFN_WDFDEVICEUNMAPIOSPACE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PseudoBaseAddress: 
### -param NumberOfBytes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also