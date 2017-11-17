---
UID: NC.wdfdriver.PFN_WDFDRIVERISVERSIONAVAILABLE
title: PFN_WDFDRIVERISVERSIONAVAILABLE
author: windows-driver-content
description: 
ms.assetid: dd7f4b92-dea2-42bc-b15c-fae0838269b5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVERISVERSIONAVAILABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVERISVERSIONAVAILABLE PfnWdfdriverisversionavailable; 

// Definition

WDFAPI PfnWdfdriverisversionavailable 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
	PWDF_DRIVER_VERSION_AVAILABLE_PARAMS VersionAvailableParams
)
{...}

PFN_WDFDRIVERISVERSIONAVAILABLE 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 
### -param VersionAvailableParams: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also