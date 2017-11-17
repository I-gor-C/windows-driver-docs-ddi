---
UID: NC.wdfrequest.PFN_WDFREQUESTGETEFFECTIVEIOTYPE
title: PFN_WDFREQUESTGETEFFECTIVEIOTYPE
author: windows-driver-content
description: 
ms.assetid: df389201-8aea-417b-95e5-fea7b9d76741
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTGETEFFECTIVEIOTYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTGETEFFECTIVEIOTYPE PfnWdfrequestgeteffectiveiotype; 

// Definition

WDFAPI PfnWdfrequestgeteffectiveiotype 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
)
{...}

PFN_WDFREQUESTGETEFFECTIVEIOTYPE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also