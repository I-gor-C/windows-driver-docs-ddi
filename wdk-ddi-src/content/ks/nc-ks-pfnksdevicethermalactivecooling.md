---
UID: NC.ks.PFNKSDEVICETHERMALACTIVECOOLING
title: PFNKSDEVICETHERMALACTIVECOOLING
author: windows-driver-content
description: 
ms.assetid: b9a70e09-67ac-48d5-8034-bd26afc09763
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSDEVICETHERMALACTIVECOOLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICETHERMALACTIVECOOLING Pfnksdevicethermalactivecooling; 

// Definition

void Pfnksdevicethermalactivecooling 
(
	PKSDEVICE KsDevice
	BOOLEAN Engaged
	KSDEVICE_THERMAL_STATE *DeviceThermalState
)
{...}

PFNKSDEVICETHERMALACTIVECOOLING 


```

## -parameters

### -param KsDevice: 
### -param Engaged: 
### -param *DeviceThermalState: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also