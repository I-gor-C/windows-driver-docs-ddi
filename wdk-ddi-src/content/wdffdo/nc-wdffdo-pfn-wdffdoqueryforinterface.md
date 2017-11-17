---
UID: NC.wdffdo.PFN_WDFFDOQUERYFORINTERFACE
title: PFN_WDFFDOQUERYFORINTERFACE
author: windows-driver-content
description: 
ms.assetid: 6edd2328-6cb2-499a-9cc8-9217b71c01be
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDOQUERYFORINTERFACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOQUERYFORINTERFACE PfnWdffdoqueryforinterface; 

// Definition

WDFAPI PfnWdffdoqueryforinterface 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Fdo
	LPCGUID InterfaceType
	PINTERFACE Interface
	USHORT Size
	USHORT Version
	PVOID InterfaceSpecificData
)
{...}

PFN_WDFFDOQUERYFORINTERFACE 


```

## -parameters

### -param DriverGlobals: 
### -param Fdo: 
### -param InterfaceType: 
### -param Interface: 
### -param Size: 
### -param Version: 
### -param InterfaceSpecificData: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also