---
UID: NC.dispmprt.DXGKDDI_SYSTEM_DISPLAY_WRITE
title: DXGKDDI_SYSTEM_DISPLAY_WRITE
author: windows-driver-content
description: 
ms.assetid: 473abb24-e77e-469b-bf5b-6b7379fc2fbd
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

# DXGKDDI_SYSTEM_DISPLAY_WRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SYSTEM_DISPLAY_WRITE DxgkddiSystemDisplayWrite; 

// Definition

VOID DxgkddiSystemDisplayWrite 
(
	PVOID MiniportDeviceContext
	PVOID Source
	UINT SourceWidth
	UINT SourceHeight
	UINT SourceStride
	UINT PositionX
	UINT PositionY
)
{...}

DXGKDDI_SYSTEM_DISPLAY_WRITE PDXGKDDI_SYSTEM_DISPLAY_WRITE


```

## -parameters

### -param MiniportDeviceContext: 
### -param Source: 
### -param SourceWidth: 
### -param SourceHeight: 
### -param SourceStride: 
### -param PositionX: 
### -param PositionY: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also