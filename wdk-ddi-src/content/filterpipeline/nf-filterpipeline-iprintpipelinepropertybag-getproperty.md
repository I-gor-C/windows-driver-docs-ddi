---
UID: NF.filterpipeline.IPrintPipelinePropertyBag.GetProperty
title: IPrintPipelinePropertyBag::GetProperty
author: windows-driver-content
description: The GetProperty method gets a property from a property bag.
old-location: print\iprintpipelinepropertybag_getproperty.htm
old-project: print
ms.assetid: 10a5ada8-98ab-4e1c-a4b5-2f6d60674952
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintPipelinePropertyBag, GetProperty, IPrintPipelinePropertyBag::GetProperty
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
req.alt-api: IPrintPipelinePropertyBag.GetProperty
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
req.iface: IPrintPipelinePropertyBag
---

# IPrintPipelinePropertyBag::GetProperty method



## -description
<p>The <code>GetProperty</code> method gets a property from a property bag.</p>


## -syntax

````
HRESULT GetProperty(
  [in]  const wchar_t *pszName,
  [out]       VARIANT *pVar
);
````


## -parameters
<dl>

### -param pszName [in]

<dd>
<p>The name of the property that you want to get from the property bag.</p>
</dd>

### -param pVar [out]

<dd>
<p>The <b>VARIANT</b> value to get from the property bag.</p>
</dd>
</dl>

## -returns
<p><code>GetProperty</code> returns an <b>HRESULT</b> value.</p>

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