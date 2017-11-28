---
UID: NF.filterpipeline.IPartThumbnail.GetThumbnailProperties
title: IPartThumbnail::GetThumbnailProperties
author: windows-driver-content
description: The GetThumbnailProperties method gets the thumbnail properties.
old-location: print\ipartthumbnail_getthumbnailproperties.htm
old-project: print
ms.assetid: 4255bdea-4d6e-4e69-ae76-6562a3f07678
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartThumbnail, GetThumbnailProperties, IPartThumbnail::GetThumbnailProperties
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
req.alt-api: IPartThumbnail.GetThumbnailProperties
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
req.iface: IPartThumbnail
---

# IPartThumbnail::GetThumbnailProperties method



## -description
<p>The <b>GetThumbnailProperties</b> method gets the thumbnail properties.</p>


## -syntax

````
HRESULT GetThumbnailProperties(
  [out] BSTR *pContentType
);
````


## -parameters
<dl>

### -param <i>pContentType</i> [out]

<dd>
<p>A pointer to the content type of the thumbnail.</p>
</dd>
</dl>

## -returns
<p><b>GetThumbnailProperties</b> returns an <b>HRESULT</b> value.</p>

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