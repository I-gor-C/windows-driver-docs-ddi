---
UID: NC.wdfminiport.PFN_WDFDEVICEMINIPORTCREATE
title: PFN_WDFDEVICEMINIPORTCREATE
author: windows-driver-content
description: 
ms.assetid: d3910d58-42f5-4c7c-a44f-bfe30849180b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfminiport.h
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

# PFN_WDFDEVICEMINIPORTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEMINIPORTCREATE PfnWdfdeviceminiportcreate; 

// Definition

WDFAPI PfnWdfdeviceminiportcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
	PWDF_OBJECT_ATTRIBUTES Attributes
	PDEVICE_OBJECT DeviceObject
	PDEVICE_OBJECT AttachedDeviceObject
	PDEVICE_OBJECT Pdo
	WDFDEVICE *Device
)
{...}

PFN_WDFDEVICEMINIPORTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 
### -param Attributes: 
### -param DeviceObject: 
### -param AttachedDeviceObject: 
### -param Pdo: 
### -param *Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also