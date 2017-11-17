---
UID: NC.dispmprt.DXGKDDI_NOTIFY_SURPRISE_REMOVAL
title: DXGKDDI_NOTIFY_SURPRISE_REMOVAL
author: windows-driver-content
description: 
ms.assetid: a2778051-d077-45bd-8f70-06e669d175a1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_NOTIFY_SURPRISE_REMOVAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_NOTIFY_SURPRISE_REMOVAL DxgkddiNotifySurpriseRemoval; 

// Definition

NTSTATUS DxgkddiNotifySurpriseRemoval 
(
	PVOID MiniportDeviceContext
	DXGK_SURPRISE_REMOVAL_TYPE RemovalType
)
{...}

DXGKDDI_NOTIFY_SURPRISE_REMOVAL PDXGKDDI_NOTIFY_SURPRISE_REMOVAL


```

## -parameters

### -param MiniportDeviceContext: 
### -param RemovalType: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also