---
UID: NF.filterpipeline.IPartFont.GetFontProperties
title: IPartFont::GetFontProperties
author: windows-driver-content
description: The GetFontProperties method gets the font properties.
old-location: print\ipartfont_getfontproperties.htm
old-project: print
ms.assetid: 6a19c32c-62f2-4b88-908c-c6b92419e410
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartFont, GetFontProperties, IPartFont::GetFontProperties
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
req.alt-api: IPartFont.GetFontProperties
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

# IPartFont::GetFontProperties method



## -description
<p>The <b>GetFontProperties</b> method gets the font properties.</p>


## -syntax

````
HRESULT GetFontProperties(
  [out] BSTR            *pContentType,
  [out] EXpsFontOptions *pFontOptions
);
````


## -parameters
<dl>

### -param pContentType [out]

<dd>
<p>A pointer to the content type of the font.</p>
</dd>

### -param pFontOptions [out]

<dd>
<p>A pointer to the options of the font.</p>
</dd>
</dl>

## -returns
<p><b>GetFontProperties</b> returns an <b>HRESULT</b> value.</p>

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