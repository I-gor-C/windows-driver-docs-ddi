---
UID: NC.dispmprt.DXGKDDI_GET_CHILD_CONTAINER_ID
title: DXGKDDI_GET_CHILD_CONTAINER_ID
author: windows-driver-content
description: 
ms.assetid: 6b397bdd-facf-4ec5-a68e-505991fe9474
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

# DXGKDDI_GET_CHILD_CONTAINER_ID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GET_CHILD_CONTAINER_ID DxgkddiGetChildContainerId; 

// Definition

NTSTATUS DxgkddiGetChildContainerId 
(
	PVOID MiniportDeviceContext
	ULONG ChildUid
	PDXGK_CHILD_CONTAINER_ID ContainerId
)
{...}

DXGKDDI_GET_CHILD_CONTAINER_ID PDXGKDDI_GET_CHILD_CONTAINER_ID


```

## -parameters

### -param MiniportDeviceContext: 
### -param ChildUid: 
### -param ContainerId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also