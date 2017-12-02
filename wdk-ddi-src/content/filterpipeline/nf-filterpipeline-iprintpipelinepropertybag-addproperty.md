---
UID: NF.filterpipeline.IPrintPipelinePropertyBag.AddProperty
title: IPrintPipelinePropertyBag::AddProperty
author: windows-driver-content
description: The AddProperty method adds a property to a property bag.
old-location: print\iprintpipelinepropertybag_addproperty.htm
old-project: print
ms.assetid: ba994342-c203-443e-a9fd-60fd29721dae
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintPipelinePropertyBag, AddProperty, IPrintPipelinePropertyBag::AddProperty
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
req.alt-api: IPrintPipelinePropertyBag.AddProperty
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

# IPrintPipelinePropertyBag::AddProperty method



## -description
<p>The <code>AddProperty</code> method adds a property to a property bag.</p>


## -syntax

````
HRESULT AddProperty(
  [in] const wchar_t *pszName,
  [in] const VARIANT *pVar
);
````


## -parameters
<dl>

### -param pszName [in]

<dd>
<p>The name of the property that you want to add to the property bag. You should uniquely identify this property so that it does not collide with others. For example, use a name like <i>MyCompanyName-MySetting</i>.</p>
</dd>

### -param pVar [in]

<dd>
<p>The <b>VARIANT</b> value to add to the property bag.</p>
</dd>
</dl>

## -returns
<p><code>AddProperty</code> returns an <b>HRESULT</b> value.</p>

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