---
UID: NS.ksmedia.PKSWAVE_BUFFER
title: PKSWAVE_BUFFER
author: windows-driver-content
description: The KSWAVE_BUFFER structure is used to describe a sample buffer.
old-location: stream\kswave_buffer.htm
ms.assetid: 1bd19fcd-90da-4e1a-ac9a-692c6fddc7ab
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
req.alt-api: KSWAVE_BUFFER
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
ms.keywords: PKSWAVE_BUFFER, KSWAVE_BUFFER, *PKSWAVE_BUFFER
req.iface: 
---

# PKSWAVE_BUFFER structure



## -description
<p>The KSWAVE_BUFFER structure is used to describe a sample buffer.</p>


## -syntax

````
typedef struct {
  ULONG Attributes;
  ULONG BufferSize;
  PVOID BufferAddress;
} KSWAVE_BUFFER, *PKSWAVE_BUFFER;
````


## -struct-fields
<dl>

### -field <b>Attributes</b>

<dd>
<p>Specifies the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSWAVE_BUFFER_ATTRIBUTEF_LOOPING</p>
</td>
<td>
<p>Indicates that the buffer loops.</p>
</td>
</tr>
<tr>
<td>
<p>KSWAVE_BUFFER_ATTRIBUTEF_STATIC</p>
</td>
<td>
<p>Indicates that the buffer is static.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>BufferSize</b>

<dd>
<p>Specifies the size of the buffer, in bytes.</p>
</dd>

### -field <b>BufferAddress</b>

<dd>
<p>Specifies the starting address of the buffer.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566514">KSPROPERTY_WAVE_BUFFER</a> property.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566514">KSPROPERTY_WAVE_BUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSWAVE_BUFFER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
