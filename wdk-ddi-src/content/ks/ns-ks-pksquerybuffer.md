---
UID: NS.ks.PKSQUERYBUFFER
title: PKSQUERYBUFFER
author: windows-driver-content
description: The KSQUERYBUFFER structure is used when querying for outstanding buffers available on an event with KSEVENT_TYPE_QUERYBUFFER.
old-location: stream\ksquerybuffer.htm
ms.assetid: 6827df53-f970-4ceb-961d-b4b95fa56cfe
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
req.alt-api: KSQUERYBUFFER
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
ms.keywords: PKSQUERYBUFFER, KSQUERYBUFFER, *PKSQUERYBUFFER
req.iface: 
---

# PKSQUERYBUFFER structure



## -description
<p>The KSQUERYBUFFER structure is used when querying for outstanding buffers available on an event with KSEVENT_TYPE_QUERYBUFFER<b>.</b></p>


## -syntax

````
typedef struct {
  KSEVENT      Event;
  PKSEVENTDATA EventData;
  PVOID        Reserved;
} KSQUERYBUFFER, *PKSQUERYBUFFER;
````


## -struct-fields
<dl>

### -field <b>Event</b>

<dd>
<p>Specifies the description of the original event, with the KSEVENT_TYPE_QUERYBUFFER flag set instead of the KSEVENT_TYPE_ENABLEBUFFERED flag.</p>
</dd>

### -field <b>EventData</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> structure. This is the same pointer supplied to <a href="https://msdn.microsoft.com/library/windows/hardware/ff554260">AVStrMiniAddEvent</a> at event enable time. This pointer is used as the unique identifier in locating the event, just as it is used when disabling the event.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Not used, and set to zero.</p>
</dd>
</dl>

## -remarks
<p>If KSEVENT_TYPE_ENABLEBUFFERED was used to enable an event that also buffers data, then the data produced by the event can be queried using this method. The description of the event being queried is provided as the first parameter, and any buffer is provided as the second parameter to the query.</p>

<p>The buffer length needed can be queried by providing a zero length output buffer. The size of buffer is returned in the <b>BytesReturned</b> parameter, with a warning status of STATUS_BUFFER_OVERFLOW.</p>

<p>Alternatively, the query returns one of the following status values:</p>

<p>STATUS_NOT_FOUND</p>

<p>event was not found</p>

<p>STATUS_INVALID_PARAMETER</p>

<p>it was not being buffered</p>

<p>STATUS_NO_MORE_ENTRIES</p>

<p>no buffers were available</p>

<p>STATUS_BUFFER_TOO_SMALL</p>

<p>buffer size was insufficient.</p>

<p>STATUS_SUCCESS</p>

<p>life is good.</p>

<p> </p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560992">KSBUFFER_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSQUERYBUFFER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
