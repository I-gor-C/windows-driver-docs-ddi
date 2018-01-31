---
UID : NS:d3dkmthk._D3DKMT_ADDSURFACETOSWAPCHAIN
title : "_D3DKMT_ADDSURFACETOSWAPCHAIN"
author : windows-driver-content
description : Used to add a surface to the swapchain.
old-location : display\d3dkmt-addsurfacetoswapchain.htm
old-project : display
ms.assetid : f1a2390c-0154-4bd7-954f-ca8725710d61
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3dkmt-addsurfacetoswapchain, _D3DKMT_ADDSURFACETOSWAPCHAIN, D3DKMT_ADDSURFACETOSWAPCHAIN, D3DKMT_ADDSURFACETOSWAPCHAIN structure [Display Devices], d3dkmthk/D3DKMT_ADDSURFACETOSWAPCHAIN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DKMT_ADDSURFACETOSWAPCHAIN
---

# _D3DKMT_ADDSURFACETOSWAPCHAIN structure
Used to add a surface to the swapchain.

## Syntax
````
typedef struct _D3DKMT_ADDSURFACETOSWAPCHAIN {
  HANDLE hNtSwapChain;
  BOOL   bProducer;
  HANDLE hNtSurfaceHandle;
  UINT   BufferIdx;
} D3DKMT_ADDSURFACETOSWAPCHAIN;
````

## Members


`bProducer`

Indicates if the surface is a producer or consumer.

`BufferIdx`

Index of were the texture was placed on the surface table.

`hNtSurfaceHandle`

An NT handle for the surface to be added.

`hNtSwapChain`

An NT handle for the swapchain in this process.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |