---
UID: NC.dispmprt.DXGKDDI_OPM_GET_SRM_LIST_VERSION
title: DXGKDDI_OPM_GET_SRM_LIST_VERSION
author: windows-driver-content
description: 
ms.assetid: 7ec7d27a-b077-43a9-be05-72a678afbc4b
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

# DXGKDDI_OPM_GET_SRM_LIST_VERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_OPM_GET_SRM_LIST_VERSION DxgkddiOpmGetSrmListVersion; 

// Definition

NTSTATUS DxgkddiOpmGetSrmListVersion 
(
	PVOID MiniportDeviceContext
	PULONG SrmListVersionSize
	PVOID SrmListVersionBuffer
)
{...}

DXGKDDI_OPM_GET_SRM_LIST_VERSION 


```

## -parameters

### -param MiniportDeviceContext: 
### -param SrmListVersionSize: 
### -param SrmListVersionBuffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also