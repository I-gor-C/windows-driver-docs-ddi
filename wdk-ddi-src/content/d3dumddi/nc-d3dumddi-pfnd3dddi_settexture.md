---
UID : NC:d3dumddi.PFND3DDDI_SETTEXTURE
title : PFND3DDDI_SETTEXTURE
author : windows-driver-content
description : The SetTexture function inserts a texture at a particular stage in a multiple-texture group.
old-location : display\settexture.htm
old-project : display
ms.assetid : b2ed86c5-cd4f-4aaa-a062-4c7ae4e088df
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PTE, DXGK_PTE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SetTexture
req.alt-loc : d3dumddi.h
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
req.typenames : DXGK_PTE
---


# PFND3DDDI_SETTEXTURE callback function
The <i>SetTexture</i> function inserts a texture at a particular stage in a multiple-texture group.

## Syntax

```
PFND3DDDI_SETTEXTURE Pfnd3dddiSettexture;

HRESULT Pfnd3dddiSettexture(
  HANDLE hDevice,
   UINT,
   HANDLE
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`UINT`



`HANDLE`




## Return Value

<i>SetTexture</i> returns S_OK or an appropriate error result if the texture is not successfully inserted.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETTEXTURE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>