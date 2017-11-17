---
UID: NS.wdm._PCW_COUNTER_INFORMATION
title: PCW_COUNTER_INFORMATION
author: windows-driver-content
description: The PCW_COUNTER_INFORMATION structure describes attributes that identify a specific instance of a counter set.
old-location: devtest\pcw_counter_information.htm
ms.assetid: fe4d8df4-0e15-49fb-a5ec-40aa8acf3675
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: devtest
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCW_COUNTER_INFORMATION
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: PCW_COUNTER_INFORMATION, PCW_COUNTER_INFORMATION, *PPCW_COUNTER_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# PCW_COUNTER_INFORMATION structure



## -description
<p>The PCW_COUNTER_INFORMATION structure describes attributes that identify a specific instance of a counter set. </p>


## -syntax

````
typedef struct _PCW_COUNTER_INFORMATION {
  ULONG64          CounterMask;
  PCUNICODE_STRING InstanceMask;
} PCW_COUNTER_INFORMATION, *PPCW_COUNTER_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>CounterMask</b>

<dd>
<p>A bitmask. If the <i>x</i>-th bit is set, counter <i>x</i>^2 is included in the query. The value assigned to identify the counters exposed in a registration.</p>
</dd>

### -field <b>InstanceMask</b>

<dd>
<p>A Unicode string that contains a wildcard specification of the instance. That is, "*" and "?" have the usual meaning of zero-or-more-characters and any-character respectively. The <b>InstanceMask</b> identifies and maps the counter set to a specific instance. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>