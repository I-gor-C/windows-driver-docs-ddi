---
UID: NC.poscx.PFN_POSCXCLEANUPEVENTS
title: *PFN_POSCXCLEANUPEVENTS
author: windows-driver-content
description: 
ms.assetid: 1dc0176c-4019-493a-b55b-1a45eb95876a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: poscx.h
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

# *PFN_POSCXCLEANUPEVENTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_POSCXCLEANUPEVENTS *PfnPoscxcleanupevents; 

// Definition

VOID *PfnPoscxcleanupevents 
(
	PPOSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE device
	WDFFILEOBJECT fileObject
)
{...}

*PFN_POSCXCLEANUPEVENTS 


```

## -parameters

### -param DriverGlobals: 
### -param device: 
### -param fileObject: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also