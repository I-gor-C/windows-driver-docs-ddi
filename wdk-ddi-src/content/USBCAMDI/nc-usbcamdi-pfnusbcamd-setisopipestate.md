---
UID: NC.usbcamdi.PFNUSBCAMD_SetIsoPipeState
title: PFNUSBCAMD_SetIsoPipeState
author: windows-driver-content
description: 
ms.assetid: d656c0af-2d20-44c8-879e-2c24308faff5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbcamdi.h
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

# PFNUSBCAMD_SetIsoPipeState callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNUSBCAMD_SetIsoPipeState PfnusbcamdSetisopipestate; 

// Definition

NTSTATUS PfnusbcamdSetisopipestate 
(
	PVOID DeviceContext
	ULONG PipeStateFlags
)
{...}

PFNUSBCAMD_SetIsoPipeState 


```

## -parameters

### -param DeviceContext: 
### -param PipeStateFlags: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also