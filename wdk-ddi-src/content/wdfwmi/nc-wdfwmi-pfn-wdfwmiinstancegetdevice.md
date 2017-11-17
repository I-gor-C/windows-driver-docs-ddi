---
UID: NC.wdfwmi.PFN_WDFWMIINSTANCEGETDEVICE
title: PFN_WDFWMIINSTANCEGETDEVICE
author: windows-driver-content
description: 
ms.assetid: a3bd0236-0c93-4e1e-aba1-1afb1bceb22c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfwmi.h
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

# PFN_WDFWMIINSTANCEGETDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIINSTANCEGETDEVICE PfnWdfwmiinstancegetdevice; 

// Definition

WDFAPI PfnWdfwmiinstancegetdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWMIINSTANCE WmiInstance
)
{...}

PFN_WDFWMIINSTANCEGETDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param WmiInstance: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also