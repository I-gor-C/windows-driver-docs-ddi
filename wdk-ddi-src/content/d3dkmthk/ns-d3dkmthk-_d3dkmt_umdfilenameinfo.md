---
UID : NS:d3dkmthk._D3DKMT_UMDFILENAMEINFO
title : "_D3DKMT_UMDFILENAMEINFO"
author : windows-driver-content
description : The D3DKMT_UMDFILENAMEINFO structure contains the name of an OpenGL ICD that is based on the specified version of the DirectX runtime.
old-location : display\d3dkmt_umdfilenameinfo.htm
old-project : display
ms.assetid : 456aef5a-f297-4670-8a83-b468569d23ad
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : OpenGL_Structs_631f8c52-0978-4f26-bd6b-08348676795b.xml, D3DKMT_UMDFILENAMEINFO, D3DKMT_UMDFILENAMEINFO structure [Display Devices], _D3DKMT_UMDFILENAMEINFO, display.d3dkmt_umdfilenameinfo, d3dkmthk/D3DKMT_UMDFILENAMEINFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
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
req.typenames : D3DKMT_UMDFILENAMEINFO
---

# _D3DKMT_UMDFILENAMEINFO structure
The D3DKMT_UMDFILENAMEINFO structure contains the name of an OpenGL ICD that is based on the specified version of the DirectX runtime.

## Syntax
````
typedef struct _D3DKMT_UMDFILENAMEINFO {
  KMTUMDVERSION Version;
  WCHAR         UmdFileName[MAX_PATH];
} D3DKMT_UMDFILENAMEINFO;
````

## Members


`UmdFileName`

[out] A string that contains the name of the OpenGL ICD.

`Version`

[in] A KMTUMDVERSION-typed value that indicates the version of the DirectX runtime to retrieve the name of an OpenGL ICD for. The following table lists the possible values.
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
KMTUMDVERSION_DX9 (0)

</td>
<td>
DirectX version 9.0

</td>
</tr>
<tr>
<td>
KMTUMDVERSION_DX10 (1)

</td>
<td>
DirectX version 10.0

</td>
</tr>
<tr>
<td>
KMTUMDVERSION_DX11 (2)

</td>
<td>
DirectX version 11.0

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |