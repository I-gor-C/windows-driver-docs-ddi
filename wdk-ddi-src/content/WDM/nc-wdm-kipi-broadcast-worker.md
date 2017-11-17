---
UID: NC.wdm.KIPI_BROADCAST_WORKER
title: KIPI_BROADCAST_WORKER
author: windows-driver-content
description: 
ms.assetid: 9997bfcb-345b-4586-ba5f-9b3d400918ff
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# KIPI_BROADCAST_WORKER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KIPI_BROADCAST_WORKER KipiBroadcastWorker; 

// Definition

ULONG_PTR KipiBroadcastWorker 
(
	ULONG_PTR Argument
)
{...}

KIPI_BROADCAST_WORKER PKIPI_BROADCAST_WORKER


```

## -parameters

### -param Argument: 



## -returns

Returns ULONG_PTR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also