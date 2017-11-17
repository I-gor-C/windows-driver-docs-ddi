---
UID: NC.wdffdo.PFN_WDFFDOUNLOCKSTATICCHILDLISTFROMITERATION
title: PFN_WDFFDOUNLOCKSTATICCHILDLISTFROMITERATION
author: windows-driver-content
description: 
ms.assetid: 44a3bdb1-dffa-415b-bb54-ffd22b8a73b3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDOUNLOCKSTATICCHILDLISTFROMITERATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOUNLOCKSTATICCHILDLISTFROMITERATION PfnWdffdounlockstaticchildlistfromiteration; 

// Definition

WDFAPI PfnWdffdounlockstaticchildlistfromiteration 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Fdo
)
{...}

PFN_WDFFDOUNLOCKSTATICCHILDLISTFROMITERATION 


```

## -parameters

### -param DriverGlobals: 
### -param Fdo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also