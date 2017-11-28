---
UID: NS.ksmedia.tagTRANSPORTVIDEOPARMS
title: tagTRANSPORTVIDEOPARMS
author: windows-driver-content
description: The TRANSPORTVIDEOPARMS structure is defined but not presently used. It may be used in the future.
old-location: stream\transportvideoparms.htm
old-project: stream
ms.assetid: 14bc6133-78f1-4f25-8638-9348245180fa
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagTRANSPORTVIDEOPARMS, TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSPORTVIDEOPARMS
req.alt-loc: ksmedia.h
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

# tagTRANSPORTVIDEOPARMS structure



## -description
<p>The TRANSPORTVIDEOPARMS structure is defined but not presently used. It may be used in the future.</p>


## -syntax

````
typedef struct tagTRANSPORTVIDEOPARMS {
  LONG OutputMode;
  LONG Input;
} TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS;
````


## -struct-fields
<dl>

### -field <b>OutputMode</b>

<dd>
<p>Specifies the video output mode. For example ED_PLAYBACK.</p>
</dd>

### -field <b>Input</b>

<dd>
<p>Specifies the video input to use. For example, specify zero to use the first (zeroth) video input.</p>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>