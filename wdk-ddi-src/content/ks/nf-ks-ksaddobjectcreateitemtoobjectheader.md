---
UID: NF.ks.KsAddObjectCreateItemToObjectHeader
title: KsAddObjectCreateItemToObjectHeader
author: windows-driver-content
description: The KsAddObjectCreateItemToObjectHeader function adds the specified create-item to an empty item in the previously allocated create item list for this object header.
old-location: stream\ksaddobjectcreateitemtoobjectheader.htm
old-project: stream
ms.assetid: 9946e896-7f1a-4ff2-afa5-9e231047af11
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsAddObjectCreateItemToObjectHeader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsAddObjectCreateItemToObjectHeader
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsAddObjectCreateItemToObjectHeader function



## -description
<p>The <b>KsAddObjectCreateItemToObjectHeader</b> function adds the specified create-item to an empty item in the previously allocated create item list for this object header. An empty item is signified by a <b>NULL</b> create dispatch function in the entry. This function assumes that the caller is serializing multiple changes to the create items list.</p>


## -syntax

````
NTSTATUS KsAddObjectCreateItemToObjectHeader(
  _In_     KSOBJECT_HEADER      Header,
  _In_     PDRIVER_DISPATCH     Create,
  _In_     PVOID                Context,
  _In_     PWSTR                ObjectClass,
  _In_opt_ PSECURITY_DESCRIPTOR SecurityDescriptor
);
````


## -parameters
<dl>

### -param Header [in]

<dd>
<p>Points to the object header that contains the previously allocated child- create table.</p>
</dd>

### -param Create [in]

<dd>
<p>Specifies the create dispatch function to use.</p>
</dd>

### -param Context [in]

<dd>
<p>Specifies the context parameter.</p>
</dd>

### -param ObjectClass [in]

<dd>
<p>Specifies a pointer to a <b>NULL</b>-terminated character string that is used for comparison on create requests. This pointer must remain valid while the object is active.</p>
</dd>

### -param SecurityDescriptor [in, optional]

<dd>
<p>Specifies the security descriptor. This must remain valid while the object is active.</p>
</dd>
</dl>

## -returns
<p>The <b>KsAddObjectCreateItemToObjectHeader</b> function returns STATUS_SUCCESS if an empty create item slot was found and the item was added. If unsuccessful, it returns STATUS_ALLOTTED_SPACE_EXCEEDED.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>