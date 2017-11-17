---
UID: NC.netrxqueue.PFN_NETRXQUEUEINITGETQUEUEID
title: PFN_NETRXQUEUEINITGETQUEUEID
author: windows-driver-content
description: 
ms.assetid: 2bede344-b155-4b16-98d9-7fe8dbd73607
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

# PFN_NETRXQUEUEINITGETQUEUEID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETRXQUEUEINITGETQUEUEID PfnNetrxqueueinitgetqueueid; 

// Definition

WDFAPI PfnNetrxqueueinitgetqueueid 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PNETRXQUEUE_INIT NetRxQueueInit
)
{...}

PFN_NETRXQUEUEINITGETQUEUEID 


```

## -parameters

### -param DriverGlobals: 
### -param NetRxQueueInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also