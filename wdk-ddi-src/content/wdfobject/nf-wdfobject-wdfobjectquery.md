---
UID: NF.wdfobject.WdfObjectQuery
title: WdfObjectQuery function
author: windows-driver-content
description: The WdfObjectQuery method is not implemented.
old-location: wdf\wdfobjectquery.htm
old-project: wdf
ms.assetid: c9e654cc-7ea5-41dd-8ee5-23a89f61e3c1
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfObjectQuery
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.product: Windows 10 or later.
---

# WdfObjectQuery function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfObjectQuery</b> method is not implemented.



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

### -param Object [in]


### -param Guid [in]


### -param QueryBufferLength [in]


### -param QueryBuffer [out]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Not applicable

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>