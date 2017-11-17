---
UID: NS.ntdd8042._OUTPUT_PACKET
title: OUTPUT_PACKET
author: windows-driver-content
description: OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt.
old-location: hid\output_packet.htm
ms.assetid: 1d8d723f-aae5-499e-94cf-c7ccdb24c45f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: hid
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OUTPUT_PACKET
req.alt-loc: ntdd8042.h
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
ms.keywords: OUTPUT_PACKET, OUTPUT_PACKET, *POUTPUT_PACKET
req.iface: 
---

# OUTPUT_PACKET structure



## -description
<p>OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt.</p>


## -syntax

````
typedef struct _OUTPUT_PACKET {
  PUCHAR         Bytes;
  ULONG          CurrentByte;
  ULONG          ByteCount;
  TRANSMIT_STATE State;
} OUTPUT_PACKET, *POUTPUT_PACKET;
````


## -struct-fields
<dl>

### -field <b>Bytes</b>

<dd>
<p>Pointer to an array of bytes being written to an i8042 port device.</p>
</dd>

### -field <b>CurrentByte</b>

<dd>
<p>Specifies the index of the next byte to write.</p>
</dd>

### -field <b>ByteCount</b>

<dd>
<p>Specifies the number of bytes in the array of bytes located at <b>Bytes</b>.</p>
</dd>

### -field <b>State</b>

<dd>
<p>Specifies one of the following write states:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef enum _TRANSMIT_STATE {
    Idle = 0,
    SendingBytes
} TRANSMIT_STATE;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="Idle"></a><a id="idle"></a><a id="IDLE"></a>Idle

<dd>
<p>Identifies that a write is not in progress.</p>
</dd>

### -field <a id="SendingBytes"></a><a id="sendingbytes"></a><a id="SENDINGBYTES"></a>SendingBytes

<dd>
<p>Identifies that a write is in progress.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>This structure is used with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543248">PI8042_KEYBOARD_ISR</a> callback routine and a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543252">PI8042_MOUSE_ISR</a> callback routine.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdd8042.h (include Ntdd8042.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/0feca7de-aa80-4d1e-a5fc-901c18169649">KbFilter_IsrHook</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/34d0a7e9-4a1e-43ba-a643-800ebaadc360">MouFilter_IsrHook</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543248">PI8042_KEYBOARD_ISR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543252">PI8042_MOUSE_ISR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20OUTPUT_PACKET structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
