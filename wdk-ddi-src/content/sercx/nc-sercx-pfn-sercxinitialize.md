---
UID: NC.sercx.PFN_SERCXINITIALIZE
title: PFN_SERCXINITIALIZE
author: windows-driver-content
description: 
ms.assetid: c4ed18cd-68b7-4a98-94cc-8a1a5774039a
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

# PFN_SERCXINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXINITIALIZE PfnSercxinitialize; 

// Definition

WDFAPI PfnSercxinitialize 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	PSERCX_CONFIG Config
)
{...}

PFN_SERCXINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param Config: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also