---
UID: NS.ks.PKSFRAMETIME
title: PKSFRAMETIME
author: windows-driver-content
description: The KSFRAMETIME structure is supported by rendering pins, and is used to return the duration of the next &#0034;frame&#0034; of data, and flags associated with that frame.
old-location: stream\ksframetime.htm
ms.assetid: 0e3beb72-2b00-41be-a7b4-341bcf065e92
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSFRAMETIME
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
ms.keywords: PKSFRAMETIME, KSFRAMETIME, *PKSFRAMETIME
req.iface: 
---

# PKSFRAMETIME structure



## -description
<p>The KSFRAMETIME structure is supported by rendering pins, and is used to return the duration of the next "frame" of data, and flags associated with that frame.</p>


## -syntax

````
typedef struct {
  LONGLONG Duration;
  ULONG    FrameFlags;
  ULONG    Reserved;
} KSFRAMETIME, *PKSFRAMETIME;
````


## -struct-fields
<dl>

### -field <b>Duration</b>

<dd>
<p>Specifies the duration in presentation time units.</p>
</dd>

### -field <b>FrameFlags</b>

<dd>
<p>Specifies the flags specific to the next frame, or to all frames. Flags are described on the reference page for <a href="https://msdn.microsoft.com/library/windows/hardware/ff560979">KSALLOCATOR_FRAMING</a>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Set to zero.</p>
</dd>
</dl>

## -remarks
<p>Note that this is an optional property, which need only be implemented if the pin instance understands the specifics of the media type it is transporting.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>