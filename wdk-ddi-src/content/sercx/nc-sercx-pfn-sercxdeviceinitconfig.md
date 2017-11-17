---
UID: NC.sercx.PFN_SERCXDEVICEINITCONFIG
title: PFN_SERCXDEVICEINITCONFIG
author: windows-driver-content
description: 
ms.assetid: d713b772-3936-456d-b963-15b53081052b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCXDEVICEINITCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXDEVICEINITCONFIG PfnSercxdeviceinitconfig; 

// Definition

WDFAPI PfnSercxdeviceinitconfig 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
)
{...}

PFN_SERCXDEVICEINITCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also