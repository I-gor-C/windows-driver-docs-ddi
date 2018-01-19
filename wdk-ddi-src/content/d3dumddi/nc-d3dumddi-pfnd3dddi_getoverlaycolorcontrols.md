---
UID : NC:d3dumddi.PFND3DDDI_GETOVERLAYCOLORCONTROLS
title : PFND3DDDI_GETOVERLAYCOLORCONTROLS
author : windows-driver-content
description : The GetOverlayColorControls function retrieves color-control settings for the given overlay.
old-location : display\getoverlaycolorcontrols.htm
old-project : display
ms.assetid : 23b15bb5-4394-406b-8869-f9d1e4e2b539
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
req.alt-api : GetOverlayColorControls
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


# PFND3DDDI_GETOVERLAYCOLORCONTROLS callback function
The <i>GetOverlayColorControls</i> function retrieves color-control settings for the given overlay.

## Syntax

```
PFND3DDDI_GETOVERLAYCOLORCONTROLS Pfnd3dddiGetoverlaycolorcontrols;

HRESULT Pfnd3dddiGetoverlaycolorcontrols(
  HANDLE hDevice,
  D3DDDIARG_GETOVERLAYCOLORCONTROLS *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<i>GetOverlayColorControls</i> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The color-control settings were successfully retrieved.
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>Parameters were validated and determined to be incorrect.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><i>GetOverlayColorControls</i> could not allocate the required memory for it to complete.

## Remarks

The Microsoft Direct3D runtime calls the <i>GetOverlayColorControls</i> function to return the current brightness, contrast, hue, saturation, sharpness, gamma, and color-enable settings that are associated with a specific overlay. 

The runtime can also call <i>GetOverlayColorControls</i> for an overlay that is not yet visible. In this situation, when the <b>hOverlay</b> member of the <a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_getoverlaycolorcontrols.md">D3DDDIARG_GETOVERLAYCOLORCONTROLS</a> structure pointed to by <i>pData</i> is set to <b>NULL</b>, the driver should return the default color-control settings of the overlay hardware.

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
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_getoverlaycolorcontrols.md">D3DDDIARG_GETOVERLAYCOLORCONTROLS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_GETOVERLAYCOLORCONTROLS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>