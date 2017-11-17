---
UID: NS.ksmedia.PLOOPEDSTREAMING_POSITION_EVENT_DATA
title: PLOOPEDSTREAMING_POSITION_EVENT_DATA
author: windows-driver-content
description: The LOOPEDSTREAMING_POSITION_EVENT_DATA structure describes a position event in a looped buffer.
old-location: audio\loopedstreaming_position_event_data.htm
ms.assetid: c9ce4ff9-1c69-40c4-8d82-d1ec4e134f34
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LOOPEDSTREAMING_POSITION_EVENT_DATA
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
ms.keywords: PLOOPEDSTREAMING_POSITION_EVENT_DATA, LOOPEDSTREAMING_POSITION_EVENT_DATA, *PLOOPEDSTREAMING_POSITION_EVENT_DATA
req.iface: 
---

# PLOOPEDSTREAMING_POSITION_EVENT_DATA structure



## -description
<p>The LOOPEDSTREAMING_POSITION_EVENT_DATA structure describes a position event in a looped buffer.</p>


## -syntax

````
typedef struct {
  KSEVENTDATA KsEventData;
  ULONGLONG   Position;
  DWORDLONG   Position;
} LOOPEDSTREAMING_POSITION_EVENT_DATA, *PLOOPEDSTREAMING_POSITION_EVENT_DATA;
````


## -struct-fields
<dl>

### -field <b>KsEventData</b>

<dd>
<p>Specifies the type of notification that the system will send to the client when the event occurs. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a>.</p>
</dd>

### -field <b>Position</b>

<dd>
<p>Specifies the buffer position as a byte offset from the beginning of the looped buffer. If the size of the buffer is <i>n</i> bytes, the <b>Position</b> member must contain a value in the range 0 to <i>n</i>-1.</p>
</dd>

### -field <b>Position</b>

<dd>
<p>Specifies the buffer position as a byte offset from the beginning of the looped buffer. If the size of the buffer is <i>n</i> bytes, the <b>Position</b> member must contain a value in the range 0 to <i>n</i>-1.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537131">KSEVENT_LOOPEDSTREAMING_POSITION</a> event uses the LOOPEDSTREAMING_POSITION_EVENT_DATA structure. This type of event occurs only in looped buffers. A looped buffer is a data buffer for an audio stream of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff563381">KSINTERFACE_STANDARD_LOOPED_STREAMING</a>.</p>

<p>The driver (typically a system component) that generates the event compares the byte offset in the <b>Position</b> member to the play cursor (in a rendering stream) or the record cursor (in a capture stream). The position event occurs when the play or record cursor passes through the specified position.</p>

<p>When the play or record cursor reaches the end of a looped buffer, the cursor wraps around to the beginning of the buffer, which corresponds to a byte offset of 0.</p>

<p>For more information about looped buffers, buffer positions, and play and record cursors, see <a href="NULL">Audio Position Property</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537131">KSEVENT_LOOPEDSTREAMING_POSITION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/88baf1f0-d18f-4601-9ba3-fea957712cd6">KSEVENTSET_LoopedStreaming</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563381">KSINTERFACE_STANDARD_LOOPED_STREAMING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20LOOPEDSTREAMING_POSITION_EVENT_DATA structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
