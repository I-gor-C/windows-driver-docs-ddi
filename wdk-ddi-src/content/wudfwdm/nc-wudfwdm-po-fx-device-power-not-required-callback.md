---
UID: NC.wudfwdm.PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK
title: PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 1d1d8bfe-8f05-4bc2-a179-ec5b370adc41
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wudfwdm.h
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

# PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK PoFxDevicePowerNotRequiredCallback; 

// Definition

VOID PoFxDevicePowerNotRequiredCallback 
(
	PVOID Context
)
{...}

PO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK PPO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also