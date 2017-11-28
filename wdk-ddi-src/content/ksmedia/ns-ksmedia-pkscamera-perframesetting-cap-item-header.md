---
UID: NS.ksmedia.PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER
title: PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER
author: windows-driver-content
description: This structure contains the header information for a per-frame settings item.
old-location: stream\kscamera_perframesetting_cap_item_header.htm
old-project: stream
ms.assetid: 6E68CACB-4E0E-41E4-BAB6-0B7ECEFA92F6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER, KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER, *PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER
req.alt-loc: Ksmedia.h
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

# PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER structure



## -description
<p>This structure contains the header information for a per-frame settings item.</p>


## -syntax

````
typedef struct {
  ULONG     Size;
  ULONG     Type;
  ULONGLONG Flags;
} KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER, *PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this header and the item payload that follows.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925212">KSCAMERA_PERFRAMESETTING_ITEM_TYPE</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>This contains the supported capability flags.</p>
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
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>