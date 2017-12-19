---
UID: NF.filterpipeline.IPartFont.GetFontProperties
title: IPartFont::GetFontProperties method
author: windows-driver-content
description: The GetFontProperties method gets the font properties.
old-location: print\ipartfont_getfontproperties.htm
old-project: print
ms.assetid: 6a19c32c-62f2-4b88-908c-c6b92419e410
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IPartFont, IPartFont::GetFontProperties, GetFontProperties
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
---

# IPartFont::GetFontProperties method



## -description
The <b>GetFontProperties</b> method gets the font properties.



## -syntax

````
HRESULT GetFontProperties(
  [out] BSTR            *pContentType,
  [out] EXpsFontOptions *pFontOptions
);
````


## -parameters

### -param pContentType [out]

A pointer to the content type of the font.


### -param pFontOptions [out]

A pointer to the options of the font.


## -returns
<b>GetFontProperties</b> returns an <b>HRESULT</b> value.


## -remarks


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
Header

</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IDL

</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>