---
UID: NC.d3dumddi.PFND3DDDI_UPDATEPALETTE
title: PFND3DDDI_UPDATEPALETTE
author: windows-driver-content
description: The UpdatePalette function updates a texture palette.
old-location: display\updatepalette.htm
ms.assetid: 7c22e0c9-cc24-4398-88b7-c91855cbc731
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UpdatePalette
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_UPDATEPALETTE callback



## -description
<p>The <i>UpdatePalette</i> function updates a texture palette.</p>


## -prototype

````
PFND3DDDI_UPDATEPALETTE UpdatePalette;

__checkReturn HRESULT APIENTRY UpdatePalette(
  _In_       HANDLE                  hDevice,
  _In_ const D3DDDIARG_UPDATEPALETTE *pData,
  _In_ const PALETTEENTRY            *pPaletteData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544093">D3DDDIARG_UPDATEPALETTE</a> structure that describes parameters for the palette-update operation.</p>
</dd>

### -param <i>pPaletteData</i> [in]

<dd>
<p> An array of PALETTEENTRY structures to update. For more information about PALETTEENTRY, see the Microsoft Windows SDK documentation.</p>
</dd>
</dl>

## -returns
<p><i>UpdatePalette</i> returns S_OK or an appropriate error result if the texture palette is not successfully updated.</p>

## -remarks
<p>The palette data in the array that is specified by <i>pPaletteData</i> consists of one UINT value for each palette entry (PALETTEENTRY structure). The palette entry is in ARGB format, with 8 bits for each of the four channels.</p>

<p>The user-mode display driver uses the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544093">D3DDDIARG_UPDATEPALETTE</a> structure that is pointed to by <i>pData</i> to update the texture palette: </p>

<p>The <b>PaletteHandle</b> member specifies the handle to the palette that is associated with the surface.</p>

<p>The <b>StartIndex</b> member specifies the index of the entry in the array at <i>pPaletteData</i> where the update should start.</p>

<p>The <b>NumEntries</b> member specifies the number of entries in the array at <i>pPaletteData</i> to update.</p>

<p>The palette data in the array that is specified by <i>pPaletteData</i> consists of one UINT value for each palette entry (PALETTEENTRY structure). The palette entry is in ARGB format, with 8 bits for each of the four channels.</p>

<p>The user-mode display driver uses the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544093">D3DDDIARG_UPDATEPALETTE</a> structure that is pointed to by <i>pData</i> to update the texture palette: </p>

<p>The <b>PaletteHandle</b> member specifies the handle to the palette that is associated with the surface.</p>

<p>The <b>StartIndex</b> member specifies the index of the entry in the array at <i>pPaletteData</i> where the update should start.</p>

<p>The <b>NumEntries</b> member specifies the number of entries in the array at <i>pPaletteData</i> to update.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544093">D3DDDIARG_UPDATEPALETTE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_UPDATEPALETTE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
