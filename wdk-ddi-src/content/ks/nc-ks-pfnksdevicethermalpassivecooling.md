---
UID: NC.ks.PFNKSDEVICETHERMALPASSIVECOOLING
title: PFNKSDEVICETHERMALPASSIVECOOLING
author: windows-driver-content
description: 
ms.assetid: 85cbb840-7732-4438-abd7-0b4a8db3f51f
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

# PFNKSDEVICETHERMALPASSIVECOOLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICETHERMALPASSIVECOOLING Pfnksdevicethermalpassivecooling; 

// Definition

void Pfnksdevicethermalpassivecooling 
(
	PKSDEVICE KsDevice
	ULONG Percentage
	KSDEVICE_THERMAL_STATE *DeviceThermalState
)
{...}

PFNKSDEVICETHERMALPASSIVECOOLING 


```

## -parameters

### -param KsDevice: 
### -param Percentage: 
### -param *DeviceThermalState: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also