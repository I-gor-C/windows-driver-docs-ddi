---
UID: NF.engextcpp.ExtRemoteTyped.HasField
title: ExtRemoteTyped::HasField
author: windows-driver-content
description: The HasField method determines if the type of the data represented by this object contains the specified member.
old-location: debugger\extremotetyped_hasfield.htm
ms.assetid: c206d8e7-1a90-4866-868b-20275a52e2dd
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteTyped.HasField
req.alt-loc: engextcpp.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: ExtRemoteTyped, HasField, ExtRemoteTyped::HasField
req.iface: ExtRemoteTyped
---

# ExtRemoteTyped::HasField method



## -description
<p>The <b>HasField</b> method determines if the type of the data represented by this object contains the specified member.</p>


## -syntax

````
bool HasField(
  [in] PCSTR Field
);
````


## -parameters
<dl>

### -param <i>Field</i> [in]

<dd>
<p>The name of the member.  The name of the member is a dot-separated path and can contain sub-members (for example, <b>mymember.mysubmember</b>).  Pointers on this dot-separated path will automatically be dereferenced. However, a dot operator (<b>.</b>) should still be used here instead of the usual C pointer dereference operator (<b>-&gt;</b>).</p>
</dd>
</dl>

## -returns
<p><b>HasField</b> returns <code>true</code> if the typed data contains the member; <code>false</code> otherwise.</p>

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
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>