---
UID: NS.d3dumddi._D3DDDIARG_UPDATEPALETTE
title: D3DDDIARG_UPDATEPALETTE
author: windows-driver-content
description: The D3DDDIARG_UPDATEPALETTE structure describes parameters that are used to update a texture palette.
old-location: display\d3dddiarg_updatepalette.htm
ms.assetid: 6637c102-4e77-4030-9bb5-ab9fb4bac2c7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_UPDATEPALETTE
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
ms.keywords: D3DDDIARG_UPDATEPALETTE, D3DDDIARG_UPDATEPALETTE
req.iface: 
---

# D3DDDIARG_UPDATEPALETTE structure



## -description
<p>The D3DDDIARG_UPDATEPALETTE structure describes parameters that are used to update a texture palette. </p>


## -syntax

````
typedef struct _D3DDDIARG_UPDATEPALETTE {
  UINT PaletteHandle;
  UINT StartIndex;
  UINT NumEntries;
} D3DDDIARG_UPDATEPALETTE;
````


## -struct-fields
<dl>

### -field <b>PaletteHandle</b>

<dd>
<p>[in] A handle to the palette to be altered.</p>
</dd>

### -field <b>StartIndex</b>

<dd>
<p>[in] The index in the palette beyond which data is updated. </p>
</dd>

### -field <b>NumEntries</b>

<dd>
<p>[in] The number of PALETTEENTRY structures that are being updated. For more information about PALETTEENTRY, see the Microsoft Windows SDK documentation.</p>
</dd>
</dl>

## -remarks
<p>The Microsoft Direct3D runtime passes palette data for updating to the <i>pPaletteData</i> parameter in a call to the user-mode display driver's <a href="https://msdn.microsoft.com/7c22e0c9-cc24-4398-88b7-c91855cbc731">UpdatePalette</a> function. This palette data is an array of PALETTEENTRY structures.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/7c22e0c9-cc24-4398-88b7-c91855cbc731">UpdatePalette</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_UPDATEPALETTE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
