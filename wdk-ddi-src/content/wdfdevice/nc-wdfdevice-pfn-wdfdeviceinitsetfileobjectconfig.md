---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETFILEOBJECTCONFIG
title: PFN_WDFDEVICEINITSETFILEOBJECTCONFIG
author: windows-driver-content
description: 
ms.assetid: 9d9d9162-d0e7-422a-84ce-9bdbb71399e9
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

# PFN_WDFDEVICEINITSETFILEOBJECTCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETFILEOBJECTCONFIG PfnWdfdeviceinitsetfileobjectconfig; 

// Definition

WDFAPI PfnWdfdeviceinitsetfileobjectconfig 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_FILEOBJECT_CONFIG FileObjectConfig
	PWDF_OBJECT_ATTRIBUTES FileObjectAttributes
)
{...}

PFN_WDFDEVICEINITSETFILEOBJECTCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param FileObjectConfig: 
### -param FileObjectAttributes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also