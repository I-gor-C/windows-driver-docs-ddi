---
UID: NE.ks.KSPIN_MDL_CACHING_EVENT
title: KSPIN_MDL_CACHING_EVENT
author: windows-driver-content
description: This enumeration is used internally by the operating system.
old-location: stream\kspin_mdl_caching_event.htm
old-project: stream
ms.assetid: 74A7C2C8-F12B-4753-8E1F-C425B0B56788
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
req.alt-api: KSPIN_MDL_CACHING_EVENT
req.alt-loc: ks.h
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

# KSPIN_MDL_CACHING_EVENT enumeration



## -description
<p>This enumeration is used internally by the operating system.</p>


## -syntax

````
typedef enum  { 
  KSPIN_MDL_CACHING_NOTIFY_CLEANUP,
  KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT,
  KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT,
  KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE
} KSPIN_MDL_CACHING_EVENT;
````


## -enum-fields
<dl>

### -field <a id="KSPIN_MDL_CACHING_NOTIFY_CLEANUP"></a><a id="kspin_mdl_caching_notify_cleanup"></a><b>KSPIN_MDL_CACHING_NOTIFY_CLEANUP</b>

<dd>
<p>This value is used internally by the operating system.</p>
</dd>

### -field <a id="KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT"></a><a id="kspin_mdl_caching_notify_cleanall_wait"></a><b>KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT</b>

<dd>
<p>This value is used internally by the operating system.</p>
</dd>

### -field <a id="KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT"></a><a id="kspin_mdl_caching_notify_cleanall_nowait"></a><b>KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT</b>

<dd>
<p>This value is used internally by the operating system.</p>
</dd>

### -field <a id="KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE"></a><a id="kspin_mdl_caching_notify_addsample"></a><b>KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE</b>

<dd>
<p>This value is used internally by the operating system.</p>
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