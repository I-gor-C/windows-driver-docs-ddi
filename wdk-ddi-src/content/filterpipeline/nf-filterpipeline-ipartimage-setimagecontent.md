---
UID: NF.filterpipeline.IPartImage.SetImageContent
title: IPartImage::SetImageContent
author: windows-driver-content
description: The SetImageContent method sets an image property that is based on the content type.
old-location: print\ipartimage_setimagecontent.htm
old-project: print
ms.assetid: 5d7a59ac-93de-4a41-9313-df189e1f6e36
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartImage, SetImageContent, IPartImage::SetImageContent
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
req.alt-api: IPartImage.SetImageContent
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
req.iface: IPartImage
---

# IPartImage::SetImageContent method



## -description
<p>The <b>SetImageContent</b> method sets an image property that is based on the content type.</p>


## -syntax

````
HRESULT SetImageContent(
  [in] const wchar_t *contentType
);
````


## -parameters
<dl>

### -param contentType [in]

<dd>
<p>The type of content of the image.</p>
</dd>
</dl>

## -returns
<p><b>SetImageContent</b> returns an <b>HRESULT</b> value.</p>

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