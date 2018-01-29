---
UID : NS:iddcx.IDARG_IN_SETSWAPCHAIN
title : IDARG_IN_SETSWAPCHAIN
author : windows-driver-content
description : Gives information used to set the indirect swapchain.
old-location : display\idarg_in_setswapchain.htm
old-project : display
ms.assetid : 5b3a4a43-e8d4-4edf-87f3-dd3e6bb7e9dc
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : IDARG_IN_SETSWAPCHAIN structure [Display Devices], display.idarg_in_setswapchain, iddcx/IDARG_IN_SETSWAPCHAIN, IDARG_IN_SETSWAPCHAIN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : iddcx.h
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
req.typenames : 
---

# IDARG_IN_SETSWAPCHAIN structure
Gives information used to set the indirect swapchain.

## Syntax
````
typedef struct IDARG_IN_SETSWAPCHAIN {
  IDDCX_SWAPCHAIN hSwapChain;
  HANDLE          hNextSurfaceAvailable;
  LUID            RenderAdapterLuid;
} IDARG_IN_SETSWAPCHAIN, *IDARG_IN_SETSWAPCHAIN;
````

## Members


`hNextSurfaceAvailable`

[in] Handle to auto reset event that is signaled when the new image to encode is ready.

`hSwapChain`

[in] Handle to indirect swapchain that will be used to pass the desktop image to the driver for processing, transmission and display.

`RenderAdapterLuid`

[In] LUID of the adapter where the desktop image was rendered.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iddcx.h |