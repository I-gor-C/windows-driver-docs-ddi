---
UID: NF.ks.KsHandleSizedListQuery
title: KsHandleSizedListQuery
author: windows-driver-content
description: The KsHandleSizedListQuery function, depending on the length of the system buffer, returns either the size of the buffer needed, number of entries in the specified data list, or copies the entries themselves.
old-location: stream\kshandlesizedlistquery.htm
old-project: stream
ms.assetid: 014ca1bd-6e18-4110-aefb-ec36e816f013
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsHandleSizedListQuery
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
req.alt-api: KsHandleSizedListQuery
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

# KsHandleSizedListQuery function



## -description
<p>The <b>KsHandleSizedListQuery</b> function, depending on the length of the system buffer, returns either the size of the buffer needed, number of entries in the specified data list, or copies the entries themselves. This assumes the structure of KSMULTIPLE_ITEM to be a Size followed by a Count.</p>


## -syntax

````
NTSTATUS KsHandleSizedListQuery(
  _In_       PIRP  Irp ,
  _In_       ULONG DataItemsCount ,
  _In_       ULONG DataItemSize ,
  _In_ const VOID  *DataItems 
);
````


## -parameters
<dl>

### -param <i>Irp </i> [in]

<dd>
<p>Specifies the IRP with the identifier list request.</p>
</dd>

### -param <i>DataItemsCount </i> [in]

<dd>
<p>Specifies the number of items in the identifier list.</p>
</dd>

### -param <i>DataItemSize </i> [in]

<dd>
<p>Specifies the size of a data item.</p>
</dd>

### -param <i>DataItems </i> [in]

<dd>
<p>Specifies the list of data items.</p>
</dd>
</dl>

## -returns
<p>The <b>KsHandleSizedListQuery</b> function returns STATUS_SUCCESS if the number of entries and the data can be copied. If the buffer is larger than the size to store just the size and the count of entries but too small to contain all the entries, the function returns status STATUS_BUFFER_TOO_SMALL.</p>

## -remarks
<p>Use the <b>KsHandleSizedListQuery</b> function when implementing properties that are to return information in the multiple item format.</p>

<p>Use the <b>KsHandleSizedListQuery</b> function when implementing properties that are to return information in the multiple item format.</p>

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