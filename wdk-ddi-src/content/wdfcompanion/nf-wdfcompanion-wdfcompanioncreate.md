---
UID: NF.wdfcompanion.WdfCompanionCreate
title: WdfCompanionCreate
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompanioncreate.htm
old-project: wdf
ms.assetid: 78b9eccf-34ef-40ae-b7fc-6fa8400f8c2a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfCompanionCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WdfCompanionCreate
req.alt-loc: wdfcompanion.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfCompanionCreate function



## -description
<p>
			For internal use only.</p>


## -syntax

````
NTSTATUS WdfCompanionCreate(
  _Inout_  PWDFDEVICE_INIT        *DeviceInit,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES DeviceAttributes,
  _Out_    WDFCOMPANION           *Companion
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in, out]

<dd></dd>

### -param <i>DeviceAttributes</i> [in, optional]

<dd></dd>

### -param <i>Companion</i> [out]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcompanion.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>