---
UID: NF.wdfcompanion.WdfDeviceInitSetCompanionEventCallbacks
title: WdfDeviceInitSetCompanionEventCallbacks
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfdeviceinitsetcompanioneventcallbacks.htm
old-project: wdf
ms.assetid: 7320238d-0c7f-423c-8de7-2b22d02d77bd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceInitSetCompanionEventCallbacks
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
req.alt-api: WdfDeviceInitSetCompanionEventCallbacks
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

# WdfDeviceInitSetCompanionEventCallbacks function



## -description
<p>
			For internal use only.</p>


## -syntax

````
VOID WdfDeviceInitSetCompanionEventCallbacks(
  _In_ PWDFDEVICE_INIT                DeviceInit,
  _In_ PWDF_COMPANION_EVENT_CALLBACKS CompanionEventCallbacks
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd></dd>

### -param <i>CompanionEventCallbacks</i> [in]

<dd></dd>
</dl>

## -returns
<p>This method does not return a value.</p>

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