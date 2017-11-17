---
UID: NS.ksmedia.PKSCAMERA_PERFRAMESETTING_CAP_HEADER
title: PKSCAMERA_PERFRAMESETTING_CAP_HEADER
author: windows-driver-content
description: This structure contains the header information for the per frame settings capabilities.
old-location: stream\kscamera_perframesetting_cap_header.htm
ms.assetid: 7478E83E-0657-4547-993A-84AECBB2562D
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
req.alt-api: KSCAMERA_PERFRAMESETTING_CAP_HEADER
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
ms.keywords: PKSCAMERA_PERFRAMESETTING_CAP_HEADER, KSCAMERA_PERFRAMESETTING_CAP_HEADER, *PKSCAMERA_PERFRAMESETTING_CAP_HEADER
req.iface: 
---

# PKSCAMERA_PERFRAMESETTING_CAP_HEADER structure



## -description
<p>This structure contains the header information for the per frame settings capabilities.</p>


## -syntax

````
typedef struct {
  ULONG     Size;
  ULONG     ItemCount;
  ULONGLONG Flags;
} KSCAMERA_PERFRAMESETTING_CAP_HEADER, *PKSCAMERA_PERFRAMESETTING_CAP_HEADER;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of the entire capability payload, including this header, all the item headers, and the item payloads that follow.</p>
</dd>

### -field <b>ItemCount</b>

<dd>
<p>The number of capability items.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Not used.</p>
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