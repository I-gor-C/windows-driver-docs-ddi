---
UID: NC.dsm.DSM_GET_CONTROLLER_INFO
title: DSM_GET_CONTROLLER_INFO
author: windows-driver-content
description: 
ms.assetid: 215e3d77-f185-4ca2-8934-3558a2db579d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_GET_CONTROLLER_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_GET_CONTROLLER_INFO DsmGetControllerInfo; 

// Definition

NTSTATUS DsmGetControllerInfo 
(
	IN PVOID DsmContext
	IN PVOID DsmId
	IN ULONG Flags
	IN OUT PCONTROLLER_INFO *ControllerInfo
)
{...}

DSM_GET_CONTROLLER_INFO 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 
### -param Flags: 
### -param *ControllerInfo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also