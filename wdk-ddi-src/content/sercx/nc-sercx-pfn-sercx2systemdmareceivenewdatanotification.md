---
UID: NC.sercx.PFN_SERCX2SYSTEMDMARECEIVENEWDATANOTIFICATION
title: PFN_SERCX2SYSTEMDMARECEIVENEWDATANOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 1bb5611c-77c6-4a77-91d2-5c05777baa10
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

# PFN_SERCX2SYSTEMDMARECEIVENEWDATANOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMARECEIVENEWDATANOTIFICATION PfnSercx2systemdmareceivenewdatanotification; 

// Definition

WDFAPI PfnSercx2systemdmareceivenewdatanotification 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2SYSTEMDMARECEIVE SystemDmaReceive
)
{...}

PFN_SERCX2SYSTEMDMARECEIVENEWDATANOTIFICATION 


```

## -parameters

### -param DriverGlobals: 
### -param SystemDmaReceive: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also