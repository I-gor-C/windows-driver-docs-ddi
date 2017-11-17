---
UID: NC.wdfdevice.PFN_WDFDEVICEASSIGNMOFRESOURCENAME
title: PFN_WDFDEVICEASSIGNMOFRESOURCENAME
author: windows-driver-content
description: 
ms.assetid: 63e73370-c51d-46ae-8932-e386e5e72b70
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

# PFN_WDFDEVICEASSIGNMOFRESOURCENAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEASSIGNMOFRESOURCENAME PfnWdfdeviceassignmofresourcename; 

// Definition

WDFAPI PfnWdfdeviceassignmofresourcename 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PCUNICODE_STRING MofResourceName
)
{...}

PFN_WDFDEVICEASSIGNMOFRESOURCENAME 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param MofResourceName: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also