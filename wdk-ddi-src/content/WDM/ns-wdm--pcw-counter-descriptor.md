---
UID: NS.wdm._PCW_COUNTER_DESCRIPTOR
title: PCW_COUNTER_DESCRIPTOR
author: windows-driver-content
description: The PCW_COUNTER_DESCRIPTOR structure supplies details about the notification to send.
old-location: devtest\pcw_counter_descriptor.htm
ms.assetid: 0b099aec-f254-4cfb-87cb-2f8965d5faae
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
req.alt-api: PCW_COUNTER_DESCRIPTOR
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
ms.keywords: PCW_COUNTER_DESCRIPTOR, PCW_COUNTER_DESCRIPTOR, *PPCW_COUNTER_DESCRIPTOR
req.iface: 
req.product: Windows 10 or later.
---

# PCW_COUNTER_DESCRIPTOR structure



## -description
<p>The PCW_COUNTER_DESCRIPTOR structure supplies details about the notification to send.</p>


## -syntax

````
typedef struct _PCW_COUNTER_DESCRIPTOR {
  USHORT Id;
  USHORT StructIndex;
  USHORT Offset;
  USHORT Size;
} PCW_COUNTER_DESCRIPTOR, *PPCW_COUNTER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Id</b>

<dd>
<p>A numeric value that specifies the <b>Id</b> (identifier) associated with the instance of the counter set.</p>
</dd>

### -field <b>StructIndex</b>

<dd>
<p>A numeric value that specifies the index into the array of structures that describe the counter set. </p>
</dd>

### -field <b>Offset</b>

<dd>
<p>A numeric value that indicates the end of the instance list for the counter set. The value is used to ensure that a new instance will always be added to the end of the list. </p>
</dd>

### -field <b>Size</b>

<dd>
<p>A numeric value that specifies the size, in bytes, associated with the instance of the counter set.</p>
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