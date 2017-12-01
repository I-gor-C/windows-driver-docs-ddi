---
UID: NE.ks.KSCOMPLETION_INVOCATION
title: KSCOMPLETION_INVOCATION
author: windows-driver-content
description: .
old-location: stream\kscompletion_invocation.htm
old-project: stream
ms.assetid: 2BD1A2F8-BAA2-40A3-9C97-667780A6F395
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCOMPLETION_INVOCATION
req.alt-loc: Ks.h
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
---

# KSCOMPLETION_INVOCATION enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KsInvokeOnSuccess  = 1,
  KsInvokeOnError    = 2,
  KsInvokeOnCancel   = 4
} KSCOMPLETION_INVOCATION;
````


## -enum-fields
<dl>

### -field <a id="KsInvokeOnSuccess"></a><a id="ksinvokeonsuccess"></a><a id="KSINVOKEONSUCCESS"></a><b>KsInvokeOnSuccess</b>

<dd>
<p>Invokes the completion routine on success.</p>
</dd>

### -field <a id="KsInvokeOnError"></a><a id="ksinvokeonerror"></a><a id="KSINVOKEONERROR"></a><b>KsInvokeOnError</b>

<dd>
<p>Invokes the completion routine on error.</p>
</dd>

### -field <a id="KsInvokeOnCancel"></a><a id="ksinvokeoncancel"></a><a id="KSINVOKEONCANCEL"></a><b>KsInvokeOnCancel</b>

<dd>
<p>Invokes the completion routine on cancellation.</p>
</dd>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>