---
UID: NC:d3d12umddi.PFND3D12DDI_CREATECOMMANDQUEUE_0023
title: PFND3D12DDI_CREATECOMMANDQUEUE_0023
author: windows-driver-content
description: The pfnCreateCommandQueue callback function is used to create command queue.
old-location: display\pfnd3d12ddi_createcommandqueue_0023.htm
old-project: display
ms.assetid: 1DA52354-2338-4214-8489-B6BFCD6060FB
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D12DDI_CREATECOMMANDQUEUE_0023, d3d12umddi/pfnCreateCommandQueue, display.pfnd3d12ddi_createcommandqueue_0023, pfnCreateCommandQueue, pfnCreateCommandQueue callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	D3d12umddi.h
api_name:
-	pfnCreateCommandQueue
product:
- Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CREATECOMMANDQUEUE_0023 callback function
The <i>pfnCreateCommandQueue</i> callback function is used to create command queue.

## Syntax

```
PFND3D12DDI_CREATECOMMANDQUEUE_0023 Pfnd3d12ddiCreatecommandqueue0023;

HRESULT Pfnd3d12ddiCreatecommandqueue0023(
   D3D12DDI_HDEVICE,
  CONST D3D12DDIARG_CREATECOMMANDQUEUE_0023 *,
   D3D12DDI_HCOMMANDQUEUE,
   D3D12DDI_HRTCOMMANDQUEUE
)
{...}
```

## Parameters

`D3D12DDI_HDEVICE`



`*`



`D3D12DDI_HCOMMANDQUEUE`



`D3D12DDI_HRTCOMMANDQUEUE`




## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

Access this callback function by using a device functions core structure, such as the <b>D3D12DDI_DEVICE_FUNCS_CORE_0003</b> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |