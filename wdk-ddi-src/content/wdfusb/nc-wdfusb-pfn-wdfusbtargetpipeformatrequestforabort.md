---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEFORMATREQUESTFORABORT
title: PFN_WDFUSBTARGETPIPEFORMATREQUESTFORABORT
author: windows-driver-content
description: 
ms.assetid: 991b1d50-99f1-4ede-84d5-679fe7ea0f0a
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

# PFN_WDFUSBTARGETPIPEFORMATREQUESTFORABORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORABORT PfnWdfusbtargetpipeformatrequestforabort; 

// Definition

WDFAPI PfnWdfusbtargetpipeformatrequestforabort 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
)
{...}

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORABORT 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also