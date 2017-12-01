---
UID: NF.wdfdevice.WdfDeviceRetrieveCompanionTarget
title: WdfDeviceRetrieveCompanionTarget
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfdeviceretrievecompaniontarget.htm
old-project: wdf
ms.assetid: 2ca34fb7-72c1-4253-ad5b-bc829a1ba540
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceRetrieveCompanionTarget
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.23
req.umdf-ver: 
req.alt-api: WdfDeviceRetrieveCompanionTarget
req.alt-loc: wdfdevice.h
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

# WdfDeviceRetrieveCompanionTarget function



## -description
<p>For internal use only.</p>


## -syntax

````
NTSTATUS WdfDeviceRetrieveCompanionTarget(
  _In_  WDFDEVICE          Device,
  _Out_ WDFCOMPANIONTARGET *CompanionTarget
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd></dd>

### -param <i>CompanionTarget</i> [out]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h</dt>
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