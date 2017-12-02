---
UID: NF.filterpipeline.IFixedPage.DeleteResource
title: IFixedPage::DeleteResource
author: windows-driver-content
description: The DeleteResource method deletes a resource that is associated with the page.
old-location: print\ifixedpage_deleteresource.htm
old-project: print
ms.assetid: 11aefa65-9f1c-4a6e-aac0-8727c6e00a02
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedPage, DeleteResource, IFixedPage::DeleteResource
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
req.alt-api: IFixedPage.DeleteResource
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
req.iface: IFixedPage
---

# IFixedPage::DeleteResource method



## -description
<p>The <b>DeleteResource</b> method deletes a resource that is associated with the page.</p>


## -syntax

````
HRESULT DeleteResource(
  [in] const wchar_t *uri
);
````


## -parameters
<dl>

### -param uri [in]

<dd>
<p>The URI to the resource that should be unassociated from the page.</p>
</dd>
</dl>

## -returns
<p><b>DeleteResource</b> returns an <b>HRESULT</b> value.</p>

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