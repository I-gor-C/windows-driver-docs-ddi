---
UID: NC.trustedruntimeclx.PFN_TRSECUREDEVICEHANDOFFMASTERDEVICECONTROL
title: PFN_TRSECUREDEVICEHANDOFFMASTERDEVICECONTROL
author: windows-driver-content
description: 
ms.assetid: 8b8dd965-3825-479c-82cb-ee6e594bcf36
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: trustedruntimeclx.h
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

# PFN_TRSECUREDEVICEHANDOFFMASTERDEVICECONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_TRSECUREDEVICEHANDOFFMASTERDEVICECONTROL PfnTrsecuredevicehandoffmasterdevicecontrol; 

// Definition

WDFAPI PfnTrsecuredevicehandoffmasterdevicecontrol 
(
	WDFOBJECT BindContextObject
	PWDFDEVICE_INIT DeviceInit
	PTR_SECURE_DEVICE_CALLBACKS Callbacks
	WDFDEVICE *MasterDevice
)
{...}

PFN_TRSECUREDEVICEHANDOFFMASTERDEVICECONTROL 


```

## -parameters

### -param BindContextObject: 
### -param DeviceInit: 
### -param Callbacks: 
### -param *MasterDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also