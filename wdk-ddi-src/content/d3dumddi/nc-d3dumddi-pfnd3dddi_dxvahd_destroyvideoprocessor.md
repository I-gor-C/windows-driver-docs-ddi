---
UID: NC:d3dumddi.PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR
title: PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR
author: windows-driver-content
description: The DestroyVideoProcessor function releases resources for a Microsoft DirectX Video Acceleration (VA) video processor.
old-location: display\destroyvideoprocessor.htm
old-project: display
ms.assetid: ea90fe17-4b79-4011-9e05-d5dbd06c0c6b
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DestroyVideoProcessor, DestroyVideoProcessor callback function [Display Devices], PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR, UserModeDisplayDriver_Functions_e55b46ab-1325-4bb7-bf22-9f3cb19bff71.xml, d3dumddi/DestroyVideoProcessor, display.destroyvideoprocessor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: DestroyVideoProcessor is supported beginning with the Windows 7 operating system.
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
-	d3dumddi.h
api_name:
-	DestroyVideoProcessor
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR callback function
The <b>DestroyVideoProcessor</b> function releases resources for a Microsoft DirectX Video Acceleration (VA) video processor.

## Syntax

```
PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR Pfnd3dddiDxvahdDestroyvideoprocessor;

HRESULT Pfnd3dddiDxvahdDestroyvideoprocessor(
   HANDLE,
   HANDLE
)
{...}
```

## Parameters

`HANDLE`



`HANDLE`




## Return Value

<b>DestroyVideoProcessor</b> should return S_OK or an appropriate error result if it cannot successfully release resources for the DirectX VA video processor.

## Remarks

The <b>DestroyVideoProcessor</b> function notifies the driver to destroy the handle to the DirectX VA video processor that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_createvideoprocessor.md">CreateVideoProcessor</a> function previously created. The driver can then release resources that are associated with the DirectX VA video processor handle.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | DestroyVideoProcessor is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_createvideoprocessor.md">CreateVideoProcessor</a>