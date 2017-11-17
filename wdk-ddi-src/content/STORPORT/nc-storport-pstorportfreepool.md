---
UID: NC.storport.PStorPortFreePool
title: PStorPortFreePool
author: windows-driver-content
description: 
ms.assetid: c9048c90-ff59-4b10-a1be-229d5859a1cf
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

# PStorPortFreePool callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortFreePool Pstorportfreepool; 

// Definition

VOID Pstorportfreepool 
(
	__drv_freesMem(Mem)PVOID PMemory
	PVOID HwDeviceExtension
	__drv_freesMem(Mem)PVOID PMdl
)
{...}

PStorPortFreePool 


```

## -parameters

### -param PMemory: 
### -param HwDeviceExtension: 
### -param PMdl: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also