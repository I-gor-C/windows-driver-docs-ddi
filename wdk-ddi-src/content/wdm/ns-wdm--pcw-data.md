---
UID: NS.wdm._PCW_DATA
title: PCW_DATA
author: windows-driver-content
description: The PCW_DATA structure describes the array of data blocks that are associated with an instance.
old-location: devtest\pcw_data.htm
old-project: devtest
ms.assetid: c2da567a-cea6-497a-b50f-848ecac20b30
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PCW_DATA, PCW_DATA, *PPCW_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 or later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCW_DATA
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

# PCW_DATA structure



## -description
<p>The PCW_DATA structure describes the array of data blocks that are associated with an instance.</p>


## -syntax

````
typedef struct _PCW_DATA {
  const VOID *Data;
  ULONG      Size;
} PCW_DATA, *PPCW_DATA;
````


## -struct-fields
<dl>

### -field <b>Data</b>

<dd>
<p>A <b>const</b> pointer to a buffer of <b>Size</b> bytes.</p>
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
<p>Available in Windows 7 or later versions of Windows.</p>
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