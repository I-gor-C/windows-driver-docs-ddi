---
UID: NF.wdfcompanion.WdfCompanionWdmGetSecureDeviceHandle
title: WdfCompanionWdmGetSecureDeviceHandle
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompanionwdmgetsecuredevicehandle.htm
old-project: wdf
ms.assetid: 8fc3dc6f-8a21-490b-adbf-5f735cb953de
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfCompanionWdmGetSecureDeviceHandle
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
req.alt-api: WdfCompanionWdmGetSecureDeviceHandle
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

# WdfCompanionWdmGetSecureDeviceHandle function



## -description
<p>
			For internal use only.</p>


## -syntax

````
HANDLE WdfCompanionWdmGetSecureDeviceHandle(
  _In_ WDFCOMPANION Companion
);
````


## -parameters
<dl>

### -param <i>Companion</i> [in]

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