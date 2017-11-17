---
UID: NC.storport.PStorPortReleaseMSISpinLock
title: PStorPortReleaseMSISpinLock
author: windows-driver-content
description: 
ms.assetid: d74e1a41-3e52-416b-9259-8ea1ca5cf4b4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: storport.h
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

# PStorPortReleaseMSISpinLock callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortReleaseMSISpinLock Pstorportreleasemsispinlock; 

// Definition

VOID Pstorportreleasemsispinlock 
(
	PVOID HwDeviceExtension
	ULONG MessageID
	ULONG OldIrql
)
{...}

PStorPortReleaseMSISpinLock 


```

## -parameters

### -param HwDeviceExtension: 
### -param MessageID: 
### -param OldIrql: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also