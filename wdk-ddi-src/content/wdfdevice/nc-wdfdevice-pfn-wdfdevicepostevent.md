---
UID: NC.wdfdevice.PFN_WDFDEVICEPOSTEVENT
title: PFN_WDFDEVICEPOSTEVENT
author: windows-driver-content
description: 
ms.assetid: bb69159a-d21a-48ff-868a-a1f81189da21
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICEPOSTEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEPOSTEVENT PfnWdfdevicepostevent; 

// Definition

WDFAPI PfnWdfdevicepostevent 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	REFGUID EventGuid
	WDF_EVENT_TYPE WdfEventType
	BYTE *Data
	ULONG DataSizeCb
)
{...}

PFN_WDFDEVICEPOSTEVENT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param EventGuid: 
### -param WdfEventType: 
### -param *Data: 
### -param DataSizeCb: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also