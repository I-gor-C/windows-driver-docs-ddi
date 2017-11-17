---
UID: NC.ks.PFNKSDEVICEIRPVOID
title: PFNKSDEVICEIRPVOID
author: windows-driver-content
description: 
ms.assetid: 7f11cebb-f21e-4e82-9fd4-84810eb8d8b6
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

# PFNKSDEVICEIRPVOID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICEIRPVOID Pfnksdeviceirpvoid; 

// Definition

void Pfnksdeviceirpvoid 
(
	PKSDEVICE Device
	PIRP Irp
)
{...}

PFNKSDEVICEIRPVOID 


```

## -parameters

### -param Device: 
### -param Irp: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also