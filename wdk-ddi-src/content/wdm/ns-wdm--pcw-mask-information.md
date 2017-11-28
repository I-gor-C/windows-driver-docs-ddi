---
UID: NS.wdm._PCW_MASK_INFORMATION
title: PCW_MASK_INFORMATION
author: windows-driver-content
description: The PCW_MASK_INFORMATION structure supplies details about the notification to send to the provider. This information is passed as part of the Info parameter to the PcwCallback function. This mask information is included in PCW_CALLBACK_INFORMATION.
old-location: devtest\pcw_mask_information.htm
old-project: devtest
ms.assetid: 5519aec9-9a02-4571-8809-fa8273269ea5
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PCW_MASK_INFORMATION, PCW_MASK_INFORMATION, *PPCW_MASK_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCW_MASK_INFORMATION
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
req.iface: 
req.product: Windows 10 or later.
---

# PCW_MASK_INFORMATION structure



## -description
<p>The PCW_MASK_INFORMATION structure supplies details about the notification to send to the provider. This information is passed as part of the <i>Info</i> parameter to the <a href="..\wdm\nc-wdm-pcw-callback.md">PcwCallback</a> function. This mask information is included in PCW_CALLBACK_INFORMATION.</p>


## -syntax

````
typedef struct _PCW_MASK_INFORMATION {
  ULONG64          CounterMask;
  PCUNICODE_STRING InstanceMask;
  ULONG            InstanceId;
  BOOLEAN          CollectMultiple;
  PPCW_BUFFER      Buffer;
  PKEVENT          CancelEvent;
} PCW_MASK_INFORMATION, *PPCW_MASK_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>CounterMask</b>

<dd>
<p>A bitmask. If the <i>x</i>-th bit is set, counter <i>x</i>^2 is included in the query. The <b>CounterMask</b> is assigned to identify the counters that are exposed in a registration.</p>
</dd>

### -field <b>InstanceMask</b>

<dd>
<p>A Unicode string that contains a wildcard specification of the instance. That is, "*" and "?" have the usual meaning of zero-or-more-characters and any-character respectively. The <b>InstanceMask</b> identifies the name of the instance (or wildcard) that is used to filter the instances that will be collected.</p>
</dd>

### -field <b>InstanceId</b>

<dd>
<p>The numeric value that identifies the instance(s) to be collected. If the value is PCW_ANY_INSTANCE_ID, no specific instance identifier is required.</p>
</dd>

### -field <b>CollectMultiple</b>

<dd>
<p>The BOOLEAN value that indicates whether multiple instances should be collected or just one. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>A pointer to the consumer buffer to which the instance of the counter set will be added. Depending on the purpose of the buffer, the function either adds an instance or collects data.</p>
</dd>

### -field <b>CancelEvent</b>

<dd>
<p>A pointer to an initialized event object that indicates whether the request (either to collect data or enumerate instances) was canceled. </p>
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