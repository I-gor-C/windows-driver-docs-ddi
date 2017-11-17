---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYVIDEODECODER_0021
title: PFND3D12DDI_DESTROYVIDEODECODER_0021
author: windows-driver-content
description: 
ms.assetid: 35148de3-616f-42ce-a932-db553e8e1112
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_DESTROYVIDEODECODER_0021 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYVIDEODECODER_0021 Pfnd3d12ddiDestroyvideodecoder0021; 

// Definition

VOID Pfnd3d12ddiDestroyvideodecoder0021 
(
	D3D12DDI_HDEVICE hDrvDevice
	D3D12DDI_HVIDEODECODER_0020 hDrvVideoDecoder
)
{...}

PFND3D12DDI_DESTROYVIDEODECODER_0021 


```

## -parameters

### -param hDrvDevice: 
### -param hDrvVideoDecoder: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also