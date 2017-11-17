---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPECONFIGCONTINUOUSREADER
title: PFN_WDFUSBTARGETPIPECONFIGCONTINUOUSREADER
author: windows-driver-content
description: 
ms.assetid: 91ebb4a8-95be-4723-9146-55fdd3a8876a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETPIPECONFIGCONTINUOUSREADER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPECONFIGCONTINUOUSREADER PfnWdfusbtargetpipeconfigcontinuousreader; 

// Definition

WDFAPI PfnWdfusbtargetpipeconfigcontinuousreader 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	PWDF_USB_CONTINUOUS_READER_CONFIG Config
)
{...}

PFN_WDFUSBTARGETPIPECONFIGCONTINUOUSREADER 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Config: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also