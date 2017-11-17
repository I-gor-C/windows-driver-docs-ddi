---
UID: NC.wdfdevice.PFN_WDFDEVICESETDEVICEINTERFACESTATE
title: PFN_WDFDEVICESETDEVICEINTERFACESTATE
author: windows-driver-content
description: 
ms.assetid: 2d00512e-1037-447e-a337-19160dc2fa50
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

# PFN_WDFDEVICESETDEVICEINTERFACESTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETDEVICEINTERFACESTATE PfnWdfdevicesetdeviceinterfacestate; 

// Definition

WDFAPI PfnWdfdevicesetdeviceinterfacestate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	CONST GUID
	PCUNICODE_STRING ReferenceString
	BOOLEAN IsInterfaceEnabled
)
{...}

PFN_WDFDEVICESETDEVICEINTERFACESTATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param GUID: 
### -param ReferenceString: 
### -param IsInterfaceEnabled: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also