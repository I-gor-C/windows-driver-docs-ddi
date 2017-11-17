---
UID: NC.spbcx.PFN_SPBCONTROLLERSETREQUESTATTRIBUTES
title: PFN_SPBCONTROLLERSETREQUESTATTRIBUTES
author: windows-driver-content
description: 
ms.assetid: ecb7d3a4-d196-4ced-9934-0b60e4989b3c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBCONTROLLERSETREQUESTATTRIBUTES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBCONTROLLERSETREQUESTATTRIBUTES PfnSpbcontrollersetrequestattributes; 

// Definition

WDFAPI PfnSpbcontrollersetrequestattributes 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	PWDF_OBJECT_ATTRIBUTES RequestAttributes
)
{...}

PFN_SPBCONTROLLERSETREQUESTATTRIBUTES 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param RequestAttributes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also