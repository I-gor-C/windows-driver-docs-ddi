---
UID: NC.wdfwmi.PFN_WDFWMIINSTANCECREATE
title: PFN_WDFWMIINSTANCECREATE
author: windows-driver-content
description: 
ms.assetid: 9f9ce4c0-1fb9-4850-9577-68a68da76a78
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfwmi.h
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

# PFN_WDFWMIINSTANCECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIINSTANCECREATE PfnWdfwmiinstancecreate; 

// Definition

WDFAPI PfnWdfwmiinstancecreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_WMI_INSTANCE_CONFIG InstanceConfig
	PWDF_OBJECT_ATTRIBUTES InstanceAttributes
	WDFWMIINSTANCE *Instance
)
{...}

PFN_WDFWMIINSTANCECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param InstanceConfig: 
### -param InstanceAttributes: 
### -param *Instance: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also