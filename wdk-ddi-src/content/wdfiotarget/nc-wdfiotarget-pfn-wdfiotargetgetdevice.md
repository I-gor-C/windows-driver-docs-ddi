---
UID: NC.wdfiotarget.PFN_WDFIOTARGETGETDEVICE
title: PFN_WDFIOTARGETGETDEVICE
author: windows-driver-content
description: 
ms.assetid: 1c7f4d85-c093-4e82-8852-dcc8fa3ead90
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETGETDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETGETDEVICE PfnWdfiotargetgetdevice; 

// Definition

WDFAPI PfnWdfiotargetgetdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
)
{...}

PFN_WDFIOTARGETGETDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also