---
UID: NC.poscx.PFN_POSCXCLEANPENDINGREQUESTS
title: *PFN_POSCXCLEANPENDINGREQUESTS
author: windows-driver-content
description: 
ms.assetid: f58f7f7d-d328-4e82-8304-dfa694cff708
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

# *PFN_POSCXCLEANPENDINGREQUESTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_POSCXCLEANPENDINGREQUESTS *PfnPoscxcleanpendingrequests; 

// Definition

VOID *PfnPoscxcleanpendingrequests 
(
	PPOSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE device
	WDFFILEOBJECT callerFileObj
	NTSTATUS completionStatus
)
{...}

*PFN_POSCXCLEANPENDINGREQUESTS 


```

## -parameters

### -param DriverGlobals: 
### -param device: 
### -param callerFileObj: 
### -param completionStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also