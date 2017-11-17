---
UID: NC.netrxqueue.PFN_NETRXQUEUEQUERYALLOCATORCACHEENABLED
title: PFN_NETRXQUEUEQUERYALLOCATORCACHEENABLED
author: windows-driver-content
description: 
ms.assetid: bc060ff5-7162-4f9e-b95f-2b3c0c71bb34
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrxqueue.h
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

# PFN_NETRXQUEUEQUERYALLOCATORCACHEENABLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUEQUERYALLOCATORCACHEENABLED PfnNetrxqueuequeryallocatorcacheenabled; 

// Definition

WDFAPI PfnNetrxqueuequeryallocatorcacheenabled 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETRXQUEUE RxQueue
	PBOOLEAN CacheEnabled
)
{...}

PFN_NETRXQUEUEQUERYALLOCATORCACHEENABLED 


```

## -parameters

### -param DriverGlobals: 
### -param RxQueue: 
### -param CacheEnabled: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also