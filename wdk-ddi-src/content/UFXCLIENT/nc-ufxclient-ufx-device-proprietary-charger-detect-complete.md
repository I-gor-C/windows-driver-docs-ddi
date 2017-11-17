---
UID: NC.ufxclient.UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE
title: UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE
author: windows-driver-content
description: 
ms.assetid: 8d8acde7-c41b-4bf7-aca2-a4594e1f08cd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxclient.h
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

# UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE UfxDeviceProprietaryChargerDetectComplete; 

// Definition

VOID UfxDeviceProprietaryChargerDetectComplete 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	PUFX_PROPRIETARY_CHARGER 
)
{...}

UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE PFN_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE


```

## -parameters

### -param : 
### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also