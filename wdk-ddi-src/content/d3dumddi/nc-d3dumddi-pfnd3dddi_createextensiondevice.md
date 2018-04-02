---
UID: NC:d3dumddi.PFND3DDDI_CREATEEXTENSIONDEVICE
title: PFND3DDDI_CREATEEXTENSIONDEVICE
author: windows-driver-content
description: The CreateExtensionDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) extension device.
old-location: display\createextensiondevice.htm
old-project: display
ms.assetid: 7e6dbb70-2e74-4ddb-a504-2c8145af99d9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateExtensionDevice, CreateExtensionDevice callback function [Display Devices], PFND3DDDI_CREATEEXTENSIONDEVICE, UserModeDisplayDriver_Functions_342ee084-e24a-43a8-99a9-c83c2670e2e4.xml, d3dumddi/CreateExtensionDevice, display.createextensiondevice
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
-	CreateExtensionDevice
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_CREATEEXTENSIONDEVICE callback function
The <b>CreateExtensionDevice</b> function creates a Microsoft DirectX Video Acceleration (DirectX VA) extension device.

## Syntax

```
PFND3DDDI_CREATEEXTENSIONDEVICE Pfnd3dddiCreateextensiondevice;

HRESULT Pfnd3dddiCreateextensiondevice(
  HANDLE hDevice,
  D3DDDIARG_CREATEEXTENSIONDEVICE *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>CreateExtensionDevice</b> returns one of the following values:

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
The extension device is successfully created.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

<a href="https://msdn.microsoft.com/7e6dbb70-2e74-4ddb-a504-2c8145af99d9">CreateExtensionDevice</a> could not allocate the required memory for it to complete.

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

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542938">D3DDDIARG_CREATEEXTENSIONDEVICE</a>



<a href="https://msdn.microsoft.com/8c4bcab3-b903-4f39-aab0-7efb3b18d068">DestroyExtensionDevice</a>