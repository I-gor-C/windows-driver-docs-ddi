---
UID: NC.trustedruntimeclx.PFN_TRSECUREDEVICEHANDOFFSERVICEDEVICECONTROL
title: PFN_TRSECUREDEVICEHANDOFFSERVICEDEVICECONTROL
author: windows-driver-content
description: 
ms.assetid: 775e8b32-04c4-4dba-8312-db78dc46252a
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

# PFN_TRSECUREDEVICEHANDOFFSERVICEDEVICECONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_TRSECUREDEVICEHANDOFFSERVICEDEVICECONTROL PfnTrsecuredevicehandoffservicedevicecontrol; 

// Definition

WDFAPI PfnTrsecuredevicehandoffservicedevicecontrol 
(
	WDFOBJECT BindContextObject
	PWDFDEVICE_INIT DeviceInit
	LPGUID ServiceGuid
	PTR_SECURE_SERVICE_CALLBACKS Callbacks
	WDFDEVICE *ServiceDevice
)
{...}

PFN_TRSECUREDEVICEHANDOFFSERVICEDEVICECONTROL 


```

## -parameters

### -param BindContextObject: 
### -param DeviceInit: 
### -param ServiceGuid: 
### -param Callbacks: 
### -param *ServiceDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also