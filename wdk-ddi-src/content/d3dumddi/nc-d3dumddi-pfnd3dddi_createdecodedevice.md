---
UID: NC:d3dumddi.PFND3DDDI_CREATEDECODEDEVICE
title: PFND3DDDI_CREATEDECODEDEVICE
author: windows-driver-content
description: The CreateDecodeDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) decode device that is used to decode video.
old-location: display\createdecodedevice.htm
old-project: display
ms.assetid: 4d9a062a-2fdf-4e55-a335-c03c5d5665ff
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateDecodeDevice, CreateDecodeDevice callback function [Display Devices], PFND3DDDI_CREATEDECODEDEVICE, UserModeDisplayDriver_Functions_a6618d5f-ea60-467f-bc0b-e1fe3ee268fe.xml, d3dumddi/CreateDecodeDevice, display.createdecodedevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
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
-	d3dumddi.h
api_name:
-	CreateDecodeDevice
product:
- Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_CREATEDECODEDEVICE callback function
The <b>CreateDecodeDevice</b> function creates a Microsoft DirectX Video Acceleration (DirectX VA) decode device that is used to decode video.

## Syntax

```
PFND3DDDI_CREATEDECODEDEVICE Pfnd3dddiCreatedecodedevice;

HRESULT Pfnd3dddiCreatedecodedevice(
  HANDLE hDevice,
  D3DDDIARG_CREATEDECODEDEVICE *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>CreateDecodeDevice</b> returns one of the following values:

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
The DirectX VA decode device is successfully created.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

<a href="https://msdn.microsoft.com/4d9a062a-2fdf-4e55-a335-c03c5d5665ff">CreateDecodeDevice</a> could not allocate the required memory for it to complete.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542927">D3DDDIARG_CREATEDECODEDEVICE</a>



<a href="https://msdn.microsoft.com/3685e58b-8d67-4b01-a8a0-8a794d653637">DestroyDecodeDevice</a>