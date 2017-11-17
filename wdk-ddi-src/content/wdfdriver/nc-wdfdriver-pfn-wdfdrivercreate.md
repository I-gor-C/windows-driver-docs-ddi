---
UID: NC.wdfdriver.PFN_WDFDRIVERCREATE
title: PFN_WDFDRIVERCREATE
author: windows-driver-content
description: 
ms.assetid: 92fb314b-716f-480a-b3d2-2311e16a9b83
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVERCREATE PfnWdfdrivercreate; 

// Definition

WDFAPI PfnWdfdrivercreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PDRIVER_OBJECT DriverObject
	PCUNICODE_STRING RegistryPath
	PWDF_OBJECT_ATTRIBUTES DriverAttributes
	PWDF_DRIVER_CONFIG DriverConfig
	WDFDRIVER *Driver
)
{...}

PFN_WDFDRIVERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param DriverObject: 
### -param RegistryPath: 
### -param DriverAttributes: 
### -param DriverConfig: 
### -param *Driver: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also