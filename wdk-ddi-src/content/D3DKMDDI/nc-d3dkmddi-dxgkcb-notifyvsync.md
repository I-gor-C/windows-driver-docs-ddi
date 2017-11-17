---
UID: NC.d3dkmddi.DXGKCB_NOTIFYVSYNC
title: DXGKCB_NOTIFYVSYNC
author: windows-driver-content
description: 
ms.assetid: f1d82a7e-24ec-44f5-b2ef-fd62f0537332
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

# DXGKCB_NOTIFYVSYNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKCB_NOTIFYVSYNC DxgkcbNotifyvsync; 

// Definition

VOID DxgkcbNotifyvsync 
(
	IN_CONST_HANDLE hAdapter
	D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId
)
{...}

DXGKCB_NOTIFYVSYNC PDXGKCB_NOTIFYVSYNC


```

## -parameters

### -param hAdapter: 
### -param VidPnSourceId: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also