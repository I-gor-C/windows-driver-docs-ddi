---
UID: NC.ursdevice.PFN_URSSETHARDWAREEVENTSUPPORT
title: PFN_URSSETHARDWAREEVENTSUPPORT
author: windows-driver-content
description: 
ms.assetid: 287b3a23-3c4e-41c8-b0d1-5b75a4cea8af
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ursdevice.h
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

# PFN_URSSETHARDWAREEVENTSUPPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_URSSETHARDWAREEVENTSUPPORT PfnUrssethardwareeventsupport; 

// Definition

WDFAPI PfnUrssethardwareeventsupport 
(
	PURS_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	BOOLEAN HardwareEventReportingSupported
)
{...}

PFN_URSSETHARDWAREEVENTSUPPORT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param HardwareEventReportingSupported: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also