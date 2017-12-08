---
UID: NF.filterpipeline.IFixedPage.SetPagePart
title: IFixedPage::SetPagePart
author: windows-driver-content
description: The SetPagePart method associates a new part with the page.
old-location: print\ifixedpage_setpagepart.htm
old-project: print
ms.assetid: 12970111-3d25-4004-9c6d-8582ef7afef3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedPage, SetPagePart, IFixedPage::SetPagePart
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
req.alt-api: IFixedPage.SetPagePart
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

# IFixedPage::SetPagePart method



## -description
<p>The <b>SetPagePart</b> method associates a new part with the page.</p>


## -syntax

````
HRESULT SetPagePart(
  [in] IUnknown *pUnk
);
````


## -parameters
<dl>

### -param pUnk [in]

<dd>
<p>A pointer to the new part.</p>
</dd>
</dl>

## -returns
<p><b>SetPagePart</b> returns an <b>HRESULT</b> value.</p>

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