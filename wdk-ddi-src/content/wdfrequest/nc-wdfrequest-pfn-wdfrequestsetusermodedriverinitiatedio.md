---
UID: NC.wdfrequest.PFN_WDFREQUESTSETUSERMODEDRIVERINITIATEDIO
title: PFN_WDFREQUESTSETUSERMODEDRIVERINITIATEDIO
author: windows-driver-content
description: 
ms.assetid: 4715626a-91bd-4a70-88ec-a1d19e63e446
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

# PFN_WDFREQUESTSETUSERMODEDRIVERINITIATEDIO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTSETUSERMODEDRIVERINITIATEDIO PfnWdfrequestsetusermodedriverinitiatedio; 

// Definition

WDFAPI PfnWdfrequestsetusermodedriverinitiatedio 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	BOOLEAN IsUserModeDriverInitiated
)
{...}

PFN_WDFREQUESTSETUSERMODEDRIVERINITIATEDIO 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param IsUserModeDriverInitiated: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also