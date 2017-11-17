---
UID: NC.wdfdevice.PFN_WDFDEVICERETRIEVEDEVICEINTERFACESTRING
title: PFN_WDFDEVICERETRIEVEDEVICEINTERFACESTRING
author: windows-driver-content
description: 
ms.assetid: cdc1698d-da42-40b2-87af-df91edd9e092
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

# PFN_WDFDEVICERETRIEVEDEVICEINTERFACESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICERETRIEVEDEVICEINTERFACESTRING PfnWdfdeviceretrievedeviceinterfacestring; 

// Definition

WDFAPI PfnWdfdeviceretrievedeviceinterfacestring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	CONST GUID
	PCUNICODE_STRING ReferenceString
	WDFSTRING String
)
{...}

PFN_WDFDEVICERETRIEVEDEVICEINTERFACESTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param GUID: 
### -param ReferenceString: 
### -param String: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also