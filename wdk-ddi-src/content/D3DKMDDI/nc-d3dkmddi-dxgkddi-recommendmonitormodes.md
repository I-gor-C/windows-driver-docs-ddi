---
UID: NC.d3dkmddi.DXGKDDI_RECOMMENDMONITORMODES
title: DXGKDDI_RECOMMENDMONITORMODES
author: windows-driver-content
description: 
ms.assetid: a998e2d6-0e9b-492d-8374-6d08b31f80f8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_RECOMMENDMONITORMODES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_RECOMMENDMONITORMODES DxgkddiRecommendmonitormodes; 

// Definition

NTSTATUS DxgkddiRecommendmonitormodes 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_RECOMMENDMONITORMODES_CONST pRecommendMonitorModes
)
{...}

DXGKDDI_RECOMMENDMONITORMODES PDXGKDDI_RECOMMENDMONITORMODES


```

## -parameters

### -param hAdapter: 
### -param pRecommendMonitorModes: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also