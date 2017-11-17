---
UID: NC.sercx.PFN_SERCX2SYSTEMDMATRANSMITGETDMAENABLER
title: PFN_SERCX2SYSTEMDMATRANSMITGETDMAENABLER
author: windows-driver-content
description: 
ms.assetid: c1a7e088-7a01-4a50-923c-0a2fdf530848
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

# PFN_SERCX2SYSTEMDMATRANSMITGETDMAENABLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMATRANSMITGETDMAENABLER PfnSercx2systemdmatransmitgetdmaenabler; 

// Definition

WDFAPI PfnSercx2systemdmatransmitgetdmaenabler 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2SYSTEMDMATRANSMIT SystemDmaTransmit
)
{...}

PFN_SERCX2SYSTEMDMATRANSMITGETDMAENABLER 


```

## -parameters

### -param DriverGlobals: 
### -param SystemDmaTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also