---
UID: NS.ksmedia.tagTRANSPORTAUDIOPARMS
title: tagTRANSPORTAUDIOPARMS
author: windows-driver-content
description: The TRANSPORTAUDIOPARMS structure is defined but not used.
old-location: stream\transportaudioparms.htm
ms.assetid: 591ef01a-1a89-454a-ab58-a76813a9d4c2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSPORTAUDIOPARMS
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
ms.keywords: tagTRANSPORTAUDIOPARMS, TRANSPORTAUDIOPARMS, *PTRANSPORTAUDIOPARMS
req.iface: 
---

# tagTRANSPORTAUDIOPARMS structure



## -description
<p>The TRANSPORTAUDIOPARMS structure is defined but not used.</p>


## -syntax

````
typedef struct tagTRANSPORTAUDIOPARMS {
  LONG EnableOutput;
  LONG EnableRecord;
  LONG EnableSelsync;
  LONG Input;
  LONG MonitorSource;
} TRANSPORTAUDIOPARMS, *PTRANSPORTAUDIOPARMS;
````


## -struct-fields
<dl>

### -field <b>EnableOutput</b>

<dd>
<p>Specifies the enable audio output. The default is ED_AUDIO_ALL.</p>
</dd>

### -field <b>EnableRecord</b>

<dd>
<p>Specifies the enable audio record. The default is zero.</p>
</dd>

### -field <b>EnableSelsync</b>

<dd>
<p>Specifies the selsync.</p>
</dd>

### -field <b>Input</b>

<dd>
<p>Specifies the audio input to use. For example, specify zero to use the first (zeroth) audio input.</p>
</dd>

### -field <b>MonitorSource</b>

<dd>
<p>Indicates the monitor source. The default is zero.</p>
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