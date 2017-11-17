---
UID: NC.netrequestqueue.PFN_NETREQUESTQUEUEGETADAPTER
title: PFN_NETREQUESTQUEUEGETADAPTER
author: windows-driver-content
description: 
ms.assetid: 43170a3a-8dbe-4fc6-9a9b-113d9348dc55
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequestqueue.h
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

# PFN_NETREQUESTQUEUEGETADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTQUEUEGETADAPTER PfnNetrequestqueuegetadapter; 

// Definition

WDFAPI PfnNetrequestqueuegetadapter 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUESTQUEUE NetRequestQueue
)
{...}

PFN_NETREQUESTQUEUEGETADAPTER 


```

## -parameters

### -param DriverGlobals: 
### -param NetRequestQueue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also