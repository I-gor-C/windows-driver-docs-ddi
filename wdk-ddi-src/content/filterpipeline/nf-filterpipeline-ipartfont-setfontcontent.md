---
UID: NF.filterpipeline.IPartFont.SetFontContent
title: IPartFont::SetFontContent
author: windows-driver-content
description: The SetFontContent method sets the content of the font.
old-location: print\ipartfont_setfontcontent.htm
old-project: print
ms.assetid: bd77d32f-97fd-4f80-945d-9fff7553fcc5
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartFont, SetFontContent, IPartFont::SetFontContent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPartFont.SetFontContent
req.alt-loc: filterpipeline.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IPartFont
---

# IPartFont::SetFontContent method



## -description
<p>The <b>SetFontContent</b> method sets the content of the font.</p>


## -syntax

````
HRESULT SetFontContent(
  [in] const wchar_t *contentType
);
````


## -parameters
<dl>

### -param <i>contentType</i> [in]

<dd>
<p>The type of the content for the font to be set.</p>
</dd>
</dl>

## -returns
<p><b>SetFontContent</b> returns an <b>HRESULT</b> value.</p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IDL</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>