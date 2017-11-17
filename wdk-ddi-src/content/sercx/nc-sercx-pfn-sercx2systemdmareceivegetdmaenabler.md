---
UID: NC.sercx.PFN_SERCX2SYSTEMDMARECEIVEGETDMAENABLER
title: PFN_SERCX2SYSTEMDMARECEIVEGETDMAENABLER
author: windows-driver-content
description: 
ms.assetid: 0c639da3-779f-4594-ba6f-652451a7a581
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

# PFN_SERCX2SYSTEMDMARECEIVEGETDMAENABLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMARECEIVEGETDMAENABLER PfnSercx2systemdmareceivegetdmaenabler; 

// Definition

WDFAPI PfnSercx2systemdmareceivegetdmaenabler 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2SYSTEMDMARECEIVE SystemDmaReceive
)
{...}

PFN_SERCX2SYSTEMDMARECEIVEGETDMAENABLER 


```

## -parameters

### -param DriverGlobals: 
### -param SystemDmaReceive: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also