---
UID: NC.d3dkmddi.DXGKDDI_CREATEDEVICE
title: DXGKDDI_CREATEDEVICE
author: windows-driver-content
description: 
ms.assetid: e7324dcc-5df1-4011-b0c3-a3e2dcfe9700
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

# DXGKDDI_CREATEDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CREATEDEVICE DxgkddiCreatedevice; 

// Definition

NTSTATUS DxgkddiCreatedevice 
(
	IN_CONST_HANDLE hAdapter
	INOUT_PDXGKARG_CREATEDEVICE pCreateDevice
)
{...}

DXGKDDI_CREATEDEVICE PDXGKDDI_CREATEDEVICE


```

## -parameters

### -param hAdapter: 
### -param pCreateDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also