---
UID: NF.poscx.PosCxCleanupEvents
title: PosCxCleanupEvents
author: windows-driver-content
description: PosCxCleanupEvents is called to clean up all pending events for a given caller, identified by the open instance.
old-location: pos\poscxcleanupevents.htm
old-project: pos
ms.assetid: AD97BA14-8786-47A2-B551-2DB6FC7F83A8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxCleanupEvents
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxCleanupEvents
req.alt-loc: poscx.h
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
req.iface: 
req.product: Windows 10 or later.
---

# PosCxCleanupEvents function



## -description
<p>      PosCxCleanupEvents is called to clean up all pending events for a given  

      caller, identified by the open instance.</p>


## -syntax

````
VOID PosCxCleanupEvents(
  _In_ WDFDEVICE     device,
  _In_ WDFFILEOBJECT fileObject
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>fileObject</i> [in]

<dd>
<p>A handle to a framework file object for which all pending events should be 

          cleaned up.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>