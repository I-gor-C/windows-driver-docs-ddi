---
UID: NC.ntddk.RTL_RUN_ONCE_INIT_FN
title: RTL_RUN_ONCE_INIT_FN
author: windows-driver-content
description: 
ms.assetid: 8144cbbf-b243-4fe0-a2c5-24908974bbe2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# RTL_RUN_ONCE_INIT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_RUN_ONCE_INIT_FN RtlRunOnceInitFn; 

// Definition

_IRQL_requires_same_ ULONG RtlRunOnceInitFn 
(
	PRTL_RUN_ONCE RunOnce
	PVOID Context
	PVOID * Parameter
)
{...}

RTL_RUN_ONCE_INIT_FN PRTL_RUN_ONCE_INIT_FN


```

## -parameters

### -param RunOnce: 
### -param Context: 
### -param Parameter: 



## -returns

Returns _IRQL_requires_same_ ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also