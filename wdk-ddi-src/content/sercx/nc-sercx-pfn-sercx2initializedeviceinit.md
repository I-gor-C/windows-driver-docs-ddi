---
UID: NC.sercx.PFN_SERCX2INITIALIZEDEVICEINIT
title: PFN_SERCX2INITIALIZEDEVICEINIT
author: windows-driver-content
description: 
ms.assetid: c1c55875-8d67-4be5-b471-08a2bab04f18
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

# PFN_SERCX2INITIALIZEDEVICEINIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2INITIALIZEDEVICEINIT PfnSercx2initializedeviceinit; 

// Definition

WDFAPI PfnSercx2initializedeviceinit 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
)
{...}

PFN_SERCX2INITIALIZEDEVICEINIT 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also