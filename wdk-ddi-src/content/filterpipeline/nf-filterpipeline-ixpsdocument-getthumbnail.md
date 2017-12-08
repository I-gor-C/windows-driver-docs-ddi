---
UID: NF.filterpipeline.IXpsDocument.GetThumbnail
title: IXpsDocument::GetThumbnail
author: windows-driver-content
description: The GetThumbnail method gets the document thumbnail object.
old-location: print\ixpsdocument_getthumbnail.htm
old-project: print
ms.assetid: 74466609-4408-4065-a607-cd338902335d
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsDocument, GetThumbnail, IXpsDocument::GetThumbnail
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
req.alt-api: IXpsDocument.GetThumbnail
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
req.iface: IXpsDocument
---

# IXpsDocument::GetThumbnail method



## -description
<p>The <code>GetThumbnail</code> method gets the document thumbnail object. </p>


## -syntax

````
HRESULT GetThumbnail(
  [out] IPartThumbnail **ppThumbnail
);
````


## -parameters
<dl>

### -param ppThumbnail [out]

<dd>
<p>The thumbnail object in the document.</p>
</dd>
</dl>

## -returns
<p><code>GetThumbnail</code> returns an <b>HRESULT</b> value. This method might return E_ELEMENT_NOT_FOUND if a thumbnail cannot be found.</p>

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