---
UID: NS.ksmedia.PKSRTAUDIO_BUFFER
title: PKSRTAUDIO_BUFFER
author: windows-driver-content
description: The KSRTAUDIO_BUFFER structure specifies the buffer address, size, and a call memory barrier flag for a cyclic audio data buffer.
old-location: audio\ksrtaudio_buffer.htm
ms.assetid: b80efaf0-ecee-40cd-befb-2139a20840a5
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSRTAUDIO_BUFFER
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
ms.keywords: PKSRTAUDIO_BUFFER, KSRTAUDIO_BUFFER, *PKSRTAUDIO_BUFFER
req.iface: 
---

# PKSRTAUDIO_BUFFER structure



## -description
<p>The KSRTAUDIO_BUFFER structure specifies the buffer address, size, and a call memory barrier flag for a cyclic audio data buffer.</p>


## -syntax

````
typedef struct {
  PVOID BufferAddress;
  ULONG ActualBufferSize;
  BOOL  CallMemoryBarrier;
} KSRTAUDIO_BUFFER, *PKSRTAUDIO_BUFFER;
````


## -struct-fields
<dl>

### -field <b>BufferAddress</b>

<dd>
<p>Specifies the base address of the cyclic buffer. This is a virtual memory address through which the user-mode client can directly access the buffer. The driver writes the actual base address of the allocated buffer into this member.</p>
</dd>

### -field <b>ActualBufferSize</b>

<dd>
<p>Specifies the buffer size, in bytes. The driver sets this member to the actual size of the allocated buffer.</p>
</dd>

### -field <b>CallMemoryBarrier</b>

<dd>
<p>Specifies a flag based on cache type of the allocated buffer. The driver sets this flag to <b>TRUE</b> if the cache type is <b>MmWriteCombined</b>; otherwise, the flag should be set to <b>FALSE</b>. For more information about <b>MmWriteCombined</b>, see <a href="https://msdn.microsoft.com/14cde545-e9bb-4b96-ba10-a63595e8a107">MEMORY_CACHING_TYPE </a>,</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537370">KSPROPERTY_RTAUDIO_BUFFER</a> request uses the KSRTAUDIO_BUFFER structure to describe the actual cyclic buffer that the driver allocates. This client fills in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537494">KSRTAUDIO_BUFFER_PROPERTY</a> structure to request the audio buffer, and the driver fills in a KSRTAUDIO_BUFFER structure with the results from the buffer allocation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later Windows operating systems.</p>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537494">KSRTAUDIO_BUFFER_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537370">KSPROPERTY_RTAUDIO_BUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSRTAUDIO_BUFFER structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
