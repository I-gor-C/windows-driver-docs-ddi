---
UID: NF.filterpipeline.IPartFont.SetFontOptions
title: IPartFont::SetFontOptions
author: windows-driver-content
description: The SetFontOptions method sets the options for the font.
old-location: print\ipartfont_setfontoptions.htm
old-project: print
ms.assetid: 28c708b7-82bb-4246-bde8-88d471c8120c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartFont, SetFontOptions, IPartFont::SetFontOptions
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
req.alt-api: IPartFont.SetFontOptions
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

# IPartFont::SetFontOptions method



## -description
<p>The <b>SetFontOptions</b> method sets the options for the font.</p>


## -syntax

````
HRESULT SetFontOptions(
  [in] EXpsFontOptions options
);
````


## -parameters
<dl>

### -param <i>options</i> [in]

<dd>
<p>An <a href="print.expsfontoptions">ExpsFontOptions</a>-typed value that describes the options for the font.</p>
</dd>
</dl>

## -returns
<p><b>SetFontOptions</b> returns an <b>HRESULT</b> value.</p>

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