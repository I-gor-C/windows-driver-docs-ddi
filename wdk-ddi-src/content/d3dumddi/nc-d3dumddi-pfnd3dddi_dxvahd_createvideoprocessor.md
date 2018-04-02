---
UID: NC:d3dumddi.PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR
title: PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR
author: windows-driver-content
description: The CreateVideoProcessor function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processor that is used to process high-definition video.
old-location: display\createvideoprocessor.htm
old-project: display
ms.assetid: 68a7c394-4b0f-4446-a54b-5aee6cf8a913
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateVideoProcessor, CreateVideoProcessor callback function [Display Devices], PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR, UserModeDisplayDriver_Functions_ce6a0d51-9da3-43d9-ac23-c2e250ca4cfa.xml, d3dumddi/CreateVideoProcessor, display.createvideoprocessor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateVideoProcessor is supported beginning with the Windows 7 operating system.
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
-	CreateVideoProcessor
product:
- Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR callback function
The <b>CreateVideoProcessor</b> function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processor that is used to process high-definition video.

## Syntax

```
PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR Pfnd3dddiDxvahdCreatevideoprocessor;

HRESULT Pfnd3dddiDxvahdCreatevideoprocessor(
   HANDLE,
  D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR *
)
{...}
```

## Parameters

`HANDLE`



`*`




## Return Value

<b>CreateVideoProcessor</b> returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The video processor is successfully created. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

<a href="https://msdn.microsoft.com/68a7c394-4b0f-4446-a54b-5aee6cf8a913">CreateVideoProcessor</a> could not allocate the required memory for it to complete.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateVideoProcessor is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543077">D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451638">DestroyVideoProcessor</a>