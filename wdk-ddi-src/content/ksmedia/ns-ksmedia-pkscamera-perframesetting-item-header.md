---
UID: NS.ksmedia.PKSCAMERA_PERFRAMESETTING_ITEM_HEADER
title: PKSCAMERA_PERFRAMESETTING_ITEM_HEADER
author: windows-driver-content
description: This structure contains the header information for a per-frame settings item.
old-location: stream\kscamera_perframesetting_item_header.htm
ms.assetid: A550E674-50CA-4956-8422-16875E29D04B
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_PERFRAMESETTING_ITEM_HEADER
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
ms.keywords: PKSCAMERA_PERFRAMESETTING_ITEM_HEADER, KSCAMERA_PERFRAMESETTING_ITEM_HEADER, *PKSCAMERA_PERFRAMESETTING_ITEM_HEADER
req.iface: 
---

# PKSCAMERA_PERFRAMESETTING_ITEM_HEADER structure



## -description
<p>This structure contains the header information for a per-frame settings item.</p>


## -syntax

````
typedef struct {
  ULONG     Size;
  ULONG     Type;
  ULONGLONG Flags;
} KSCAMERA_PERFRAMESETTING_ITEM_HEADER, *PKSCAMERA_PERFRAMESETTING_ITEM_HEADER;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this header and the item payload that follows.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>This contains a <a href="https://msdn.microsoft.com/library/windows/hardware/dn925212">KSCAMERA_PERFRAMESETTING_ITEM_TYPE</a> structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>This is any one of the capability flags reported in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925193">KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER</a> Flags field.</p>
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