---
UID: NC.sercx.PFN_SERCX2INITIALIZEDEVICE
title: PFN_SERCX2INITIALIZEDEVICE
author: windows-driver-content
description: 
ms.assetid: 0801638f-181b-41cc-9962-38fa3502a177
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

# PFN_SERCX2INITIALIZEDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2INITIALIZEDEVICE PfnSercx2initializedevice; 

// Definition

WDFAPI PfnSercx2initializedevice 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PSERCX2_CONFIG Config
)
{...}

PFN_SERCX2INITIALIZEDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also