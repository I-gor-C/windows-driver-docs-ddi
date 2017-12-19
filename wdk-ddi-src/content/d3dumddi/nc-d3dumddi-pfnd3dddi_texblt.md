---
UID: NC.d3dumddi.PFND3DDDI_TEXBLT
title: PFND3DDDI_TEXBLT
author: windows-driver-content
description: The TexBlt function performs a bit-block transfer (bitblt) operation from a source texture to a destination texture, including all of the sublevels of the source texture.
old-location: display\texblt.htm
old-project: display
ms.assetid: 1ddfd822-7a43-4976-a153-ba862d6dfd82
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DXGK_PTE, DXGK_PTE
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
req.alt-api: TexBlt
req.alt-loc: d3dumddi.h
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
---

# PFND3DDDI_TEXBLT callback



## -description
The <i>TexBlt</i> function performs a bit-block transfer (bitblt) operation from a source texture to a destination texture, including all of the sublevels of the source texture.



## -prototype

````
PFND3DDDI_TEXBLT TexBlt;

__checkReturn HRESULT APIENTRY TexBlt(
  _In_       HANDLE           hDevice,
  _In_ const D3DDDIARG_TEXBLT *pData
)
{ ... }
````


## -parameters

### -param hDevice [in]

 A handle to the display device (graphics context).


### -param pData [in]

 A pointer to a <a href="display.d3dddiarg_texblt">D3DDDIARG_TEXBLT</a> structure that defines the parameters for the texture bitblt operation.


## -returns
<i>TexBlt</i> returns S_OK or an appropriate error result if the texture bitblt operation is not successfully performed.


## -remarks
The Microsoft Direct3D runtime calls the user-mode display driver's <i>TexBlt</i> function to inform the driver to perform a bitblt operation from a source texture to a destination texture. A texture can also be a cubic environment map. The driver should copy the rectangle that is specified by the <b>SrcRect</b> member of the <a href="display.d3dddiarg_texblt">D3DDDIARG_TEXBLT</a> structure in the source texture to the location that is specified by the <b>DstPoint</b> member of D3DDDIARG_TEXBLT in the destination texture. The destination and source textures are identified by the <b>hDstResource</b> and <b>hSrcResource</b> handles of D3DDDIARG_TEXBLT, respectively. 

For MIP-mapped textures, the driver must also copy all of the MIP-map sublevels that are present in the source texture. The source and destination textures might possibly contain different numbers of MIP-map levels. In this situation, the driver should copy the common levels. For example, if a 256x256 source texture has eight MIP-map levels, and if the destination is a 64x64 texture with six levels, the driver should copy the six corresponding levels from the source. Note that the dimensions of the top MIP level of the destination texture is always less than or equal to the dimensions of the top MIP level of the source texture.

The source and destination handles always refer to the top-level surfaces and never to any MIP-map sublevel. 

To copy an arbitrary level of a MIP-map texture, the runtime calls the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_blt.md">Blt</a> function instead.

The pixel formats of the source and destination textures are identical and, in general, the specified bitblt operation is safe to perform. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_blt.md">Blt</a>
</dt>
<dt>
<a href="display.d3dddiarg_texblt">D3DDDIARG_TEXBLT</a>
</dt>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_TEXBLT callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

