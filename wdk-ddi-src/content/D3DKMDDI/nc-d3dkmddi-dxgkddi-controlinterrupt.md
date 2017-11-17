---
UID: NC.d3dkmddi.DXGKDDI_CONTROLINTERRUPT
title: DXGKDDI_CONTROLINTERRUPT
author: windows-driver-content
description: 
ms.assetid: a36f4b76-dfe1-41d6-b7be-3c4a9a744b06
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

# DXGKDDI_CONTROLINTERRUPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CONTROLINTERRUPT DxgkddiControlinterrupt; 

// Definition

NTSTATUS DxgkddiControlinterrupt 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_DXGK_INTERRUPT_TYPE InterruptType
	IN_BOOLEAN EnableInterrupt
)
{...}

DXGKDDI_CONTROLINTERRUPT PDXGKDDI_CONTROLINTERRUPT


```

## -parameters

### -param hAdapter: 
### -param InterruptType: 
### -param EnableInterrupt: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also