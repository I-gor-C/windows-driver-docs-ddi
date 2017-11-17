---
UID: NF.poscx.PosCxCleanPendingRequests
title: PosCxCleanPendingRequests
author: windows-driver-content
description: PosCxCleanPendingRequests is called to cancel all pending requests for a given caller, identified by the open instance.
old-location: pos\poscxcleanpendingrequests.htm
ms.assetid: FD6036D5-C316-43E6-8C37-067F5705BCB6
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxCleanPendingRequests
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
ms.keywords: PosCxCleanPendingRequests
req.iface: 
req.product: Windows 10 or later.
---

# PosCxCleanPendingRequests function



## -description
<p>      PosCxCleanPendingRequests is called to cancel all pending requests for a given  

      caller, identified by the open instance.</p>


## -syntax

````
VOID PosCxCleanPendingRequests(
  _In_     WDFDEVICE     device,
  _In_opt_ WDFFILEOBJECT callerFileObj,
  _In_     NTSTATUS      completionStatus
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>callerFileObj</i> [in, optional]

<dd>
<p>      A handle to a framework file object for which all pending requests should be 

          cancelled, or NULL to cancel all pending requests.</p>
</dd>

### -param <i>completionStatus</i> [in]

<dd>
<p>An appropriate NTSTATUS error code that indicates success or failure.</p>
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