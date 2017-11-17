---
UID: NC.sercx.PFN_SERCX2SYSTEMDMATRANSMITINITIALIZETRANSACTIONCOMPLETE
title: PFN_SERCX2SYSTEMDMATRANSMITINITIALIZETRANSACTIONCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 1837534f-efaf-4a5e-99e3-a009857666b8
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

# PFN_SERCX2SYSTEMDMATRANSMITINITIALIZETRANSACTIONCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMATRANSMITINITIALIZETRANSACTIONCOMPLETE PfnSercx2systemdmatransmitinitializetransactioncomplete; 

// Definition

WDFAPI PfnSercx2systemdmatransmitinitializetransactioncomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2SYSTEMDMATRANSMIT SystemDmaTransmit
	BOOLEAN InitSuccess
)
{...}

PFN_SERCX2SYSTEMDMATRANSMITINITIALIZETRANSACTIONCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param SystemDmaTransmit: 
### -param InitSuccess: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also