---
UID: NC.wdfdevice.PFN_WDFDEVICEWDMDISPATCHPREPROCESSEDIRP
title: PFN_WDFDEVICEWDMDISPATCHPREPROCESSEDIRP
author: windows-driver-content
description: 
ms.assetid: 1e4fee95-a10d-4157-bd17-5733b87aa16b
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

# PFN_WDFDEVICEWDMDISPATCHPREPROCESSEDIRP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEWDMDISPATCHPREPROCESSEDIRP PfnWdfdevicewdmdispatchpreprocessedirp; 

// Definition

WDFAPI PfnWdfdevicewdmdispatchpreprocessedirp 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PIRP Irp
)
{...}

PFN_WDFDEVICEWDMDISPATCHPREPROCESSEDIRP 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Irp: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also