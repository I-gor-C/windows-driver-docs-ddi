---
UID: NC.ufxclient.EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT
title: EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT
author: windows-driver-content
description: 
ms.assetid: 6e1bead8-a1cd-4a1e-9906-3fbf53bf506b
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

# EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT EvtUfxDeviceProprietaryChargerDetect; 

// Definition

VOID EvtUfxDeviceProprietaryChargerDetect 
(
)
{...}

EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT PFN_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT


```

## -parameters




## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also