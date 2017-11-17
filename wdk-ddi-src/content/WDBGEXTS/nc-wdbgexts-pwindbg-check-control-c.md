---
UID: NC.wdbgexts.PWINDBG_CHECK_CONTROL_C
title: PWINDBG_CHECK_CONTROL_C
author: windows-driver-content
description: 
ms.assetid: 83b07397-1365-48b2-b39d-d9941c0414da
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_CHECK_CONTROL_C callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_CHECK_CONTROL_C PwindbgCheckControlC; 

// Definition

ULONG PwindbgCheckControlC 
(
	VOID 
)
{...}

PWINDBG_CHECK_CONTROL_C 


```

## -parameters

### -param : 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also