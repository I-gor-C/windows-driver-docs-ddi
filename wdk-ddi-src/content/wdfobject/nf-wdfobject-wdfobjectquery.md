---
UID: NF.wdfobject.WdfObjectQuery
title: WdfObjectQuery
author: windows-driver-content
description: The WdfObjectQuery method is not implemented.
old-location: wdf\wdfobjectquery.htm
ms.assetid: c9e654cc-7ea5-41dd-8ee5-23a89f61e3c1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WdfObjectQuery
req.alt-loc: Wdfobject.h
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Not applicable
ms.keywords: WdfObjectQuery
req.iface: 
req.product: Windows 10 or later.
---

# WdfObjectQuery function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfObjectQuery</b> method is not implemented.</p>


## -syntax

````
NTSTATUS WdfObjectQuery(
  _In_  WDFOBJECT  Object,
  _In_  CONST GUID *Guid,
  _In_  ULONG      QueryBufferLength,
  _Out_ PVOID      QueryBuffer
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd></dd>

### -param <i>Guid</i> [in]

<dd></dd>

### -param <i>QueryBufferLength</i> [in]

<dd></dd>

### -param <i>QueryBuffer</i> [out]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Not applicable</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>