---
UID: NF:d3dkmthk.D3DKMTCheckOcclusion
title: D3DKMTCheckOcclusion function
author: windows-driver-content
description: The D3DKMTCheckOcclusion function verifies whether the client area of a window is occluded.
old-location: display\d3dkmtcheckocclusion.htm
old-project: display
ms.assetid: ce889a72-5f42-4bcf-aa15-6ec9b0423781
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DKMTCheckOcclusion, D3DKMTCheckOcclusion callback function [Display Devices], OpenGL_Functions_a73b8485-971d-47a7-bc42-77bd709c5a74.xml, PFND3DKMT_CHECKOCCLUSION, d3dkmthk/D3DKMTCheckOcclusion, display.d3dkmtcheckocclusion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	d3dkmthk.h
api_name:
-	D3DKMTCheckOcclusion
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTCheckOcclusion function
The <b>D3DKMTCheckOcclusion</b> function verifies whether the client area of a window is occluded.

## Syntax

````
NTSTATUS APIENTRY D3DKMTCheckOcclusion(
  _In_ const D3DKMT_CHECKOCCLUSION *pData
);
````

## Parameters

`D3DKMT_CHECKOCCLUSION`

TBD


## Return Value

<b>D3DKMTCheckOcclusion</b> returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The client area of the window is not occluded.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_GRAPHICS_PRESENT_OCCLUDED</b></dt>
</dl>
</td>
<td width="60%">
The client area of the window is occluded.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
Parameters were validated and determined to be incorrect.

</td>
</tr>
</table>
 

This function might also return other <b>NTSTATUS</b> values.

## Remarks

The handle to the window that is checked for occlusion must be valid. A window is not occluded if a part of its client area lies on a unowned video present network (VidPn) source, if its client area is an empty rectangular area (RECT), or if desktop composition is running.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_checkocclusion.md">D3DKMT_CHECKOCCLUSION</a>