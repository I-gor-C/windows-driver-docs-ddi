---
UID: NF.filterpipeline.IPartDiscardControl.GetDiscardProperties
title: IPartDiscardControl::GetDiscardProperties
author: windows-driver-content
description: The GetDiscardProperties method gets the properties of the discard control.
old-location: print\ipartdiscardcontrol_getdiscardproperties.htm
old-project: print
ms.assetid: 37f624b8-3b15-41ee-9670-84287c3e10e6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartDiscardControl, GetDiscardProperties, IPartDiscardControl::GetDiscardProperties
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
req.alt-api: IPartDiscardControl.GetDiscardProperties
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
req.iface: IPartDiscardControl
---

# IPartDiscardControl::GetDiscardProperties method



## -description
<p>The <b>GetDiscardProperties</b> method gets the properties of the discard control.</p>


## -syntax

````
HRESULT GetDiscardProperties(
  [out] BSTR *uriSentinelPage,
  [out] BSTR *uriPartToDiscard
);
````


## -parameters
<dl>

### -param uriSentinelPage [out]

<dd>
<p>The URI of the first fixed page that no longer needs the identified resource to be processed. </p>
</dd>

### -param uriPartToDiscard [out]

<dd>
<p>The URI of the resource that the consumer can discard.</p>
</dd>
</dl>

## -returns
<p><b>GetDiscardProperties </b>returns an <b>HRESULT</b> value.</p>

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