---
UID: NC.sercx.PFN_SERCX2SYSTEMDMARECEIVEINITIALIZETRANSACTIONCOMPLETE
title: PFN_SERCX2SYSTEMDMARECEIVEINITIALIZETRANSACTIONCOMPLETE
author: windows-driver-content
description: 
ms.assetid: cfc20d73-d7b2-4384-9316-0a3f42988f16
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

# PFN_SERCX2SYSTEMDMARECEIVEINITIALIZETRANSACTIONCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMARECEIVEINITIALIZETRANSACTIONCOMPLETE PfnSercx2systemdmareceiveinitializetransactioncomplete; 

// Definition

WDFAPI PfnSercx2systemdmareceiveinitializetransactioncomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2SYSTEMDMARECEIVE SystemDmaReceive
	BOOLEAN InitSuccess
)
{...}

PFN_SERCX2SYSTEMDMARECEIVEINITIALIZETRANSACTIONCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param SystemDmaReceive: 
### -param InitSuccess: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also