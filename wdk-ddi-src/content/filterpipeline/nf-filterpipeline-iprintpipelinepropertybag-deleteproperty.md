---
UID: NF.filterpipeline.IPrintPipelinePropertyBag.DeleteProperty
title: IPrintPipelinePropertyBag::DeleteProperty
author: windows-driver-content
description: The DeleteProperty method deletes a property from a property bag.
old-location: print\iprintpipelinepropertybag_deleteproperty.htm
old-project: print
ms.assetid: f3de5514-9a7f-4e27-9be0-4aec4b84a5a7
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintPipelinePropertyBag, DeleteProperty, IPrintPipelinePropertyBag::DeleteProperty
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
req.alt-api: IPrintPipelinePropertyBag.DeleteProperty
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

# IPrintPipelinePropertyBag::DeleteProperty method



## -description
<p>The <code>DeleteProperty</code> method deletes a property from a property bag.</p>


## -syntax

````
BOOL DeleteProperty(
  [in] const wchar_t *pszName
);
````


## -parameters
<dl>

### -param pszName [in]

<dd>
<p>The name of the property to delete from the property bag.</p>
</dd>
</dl>

## -returns
<p><code>DeleteProperty</code> returns "true" if the property was deleted from the property bag.</p>

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