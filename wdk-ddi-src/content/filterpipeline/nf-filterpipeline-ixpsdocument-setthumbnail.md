---
UID: NF.filterpipeline.IXpsDocument.SetThumbnail
title: IXpsDocument::SetThumbnail
author: windows-driver-content
description: The SetThumbnail method removes the current thumbnail object from the document and inserts a new one.
old-location: print\ixpsdocument_setthumbnail.htm
old-project: print
ms.assetid: 47211c8f-e112-47fd-bd9e-57ff7ec586a5
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsDocument, SetThumbnail, IXpsDocument::SetThumbnail
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
req.alt-api: IXpsDocument.SetThumbnail
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

# IXpsDocument::SetThumbnail method



## -description
<p>The <code>SetThumbnail</code> method removes the current thumbnail object from the document and inserts a new one.</p>


## -syntax

````
HRESULT SetThumbnail(
  [in] IPartThumbnail *pThumbnail
);
````


## -parameters
<dl>

### -param pThumbnail [in]

<dd>
<p>A pointer to a new thumbnail.</p>
</dd>
</dl>

## -returns
<p><code>SetThumbnail</code> returns an <b>HRESULT</b> value.</p>

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