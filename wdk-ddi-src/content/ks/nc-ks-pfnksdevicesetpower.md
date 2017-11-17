---
UID: NC.ks.PFNKSDEVICESETPOWER
title: PFNKSDEVICESETPOWER
author: windows-driver-content
description: 
ms.assetid: 67eee238-dbcc-4c1b-afe4-972577d04a8c
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

# PFNKSDEVICESETPOWER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICESETPOWER Pfnksdevicesetpower; 

// Definition

void Pfnksdevicesetpower 
(
	PKSDEVICE Device
	PIRP Irp
	DEVICE_POWER_STATE To
	DEVICE_POWER_STATE From
)
{...}

PFNKSDEVICESETPOWER 


```

## -parameters

### -param Device: 
### -param Irp: 
### -param To: 
### -param From: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also