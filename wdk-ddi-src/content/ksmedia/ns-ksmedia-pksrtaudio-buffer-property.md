---
UID: NS.ksmedia.PKSRTAUDIO_BUFFER_PROPERTY
title: PKSRTAUDIO_BUFFER_PROPERTY
author: windows-driver-content
description: The KSRTAUDIO_BUFFER_PROPERTY structure appends a buffer base address and requested buffer size to a KSPROPERTY structure. This structure is used by the client to request allocation of the audio buffer via KSPROPERTY_RTAUDIO_BUFFER.
old-location: audio\ksrtaudio_buffer_property.htm
ms.assetid: 6fc33d5d-5d7e-4d04-a9b0-864cba961077
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
req.alt-api: KSRTAUDIO_BUFFER_PROPERTY
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
ms.keywords: PKSRTAUDIO_BUFFER_PROPERTY, KSRTAUDIO_BUFFER_PROPERTY, *PKSRTAUDIO_BUFFER_PROPERTY
req.iface: 
---

# PKSRTAUDIO_BUFFER_PROPERTY structure



## -description
<p>The KSRTAUDIO_BUFFER_PROPERTY structure appends a buffer base address and requested buffer size to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure.  This structure is used by the client to request allocation of the audio buffer via <a href="https://msdn.microsoft.com/library/windows/hardware/ff537370">KSPROPERTY_RTAUDIO_BUFFER</a>.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  PVOID      BaseAddress;
  ULONG      RequestedBufferSize;
} KSRTAUDIO_BUFFER_PROPERTY, *PKSRTAUDIO_BUFFER_PROPERTY;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>A KSPROPERTY structure that the client initializes appropriately prior to calling KSPROPERTY_RTAUDIO_BUFFER.</p>
</dd>

### -field <b>BaseAddress</b>

<dd>
<p>Specifies the desired buffer base address.  Unless the client specifies a base address, this parameter is set to <b>NULL</b>.</p>
</dd>

### -field <b>RequestedBufferSize</b>

<dd>
<p>Specifies the desired buffer size in bytes.  The driver returns the actual size of the allocated buffer in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537493">KSRTAUDIO_BUFFER</a> structure that it returns.</p>
</dd>
</dl>

## -remarks
<p>The KSPROPERTY_RTAUDIO_BUFFER request uses the KSRTAUDIO_BUFFER_PROPERTY structure to describe the cyclic buffer that the client requests.  The driver returns a KSRTAUDIO_BUFFER structure to describe the buffer that was actually allocated.</p>

<p>The value that the client writes into the <b>RequestedBufferSize</b> member is not binding on the driver. However, the driver must specify a buffer size that is as close as possible to the requested size, taking into account the buffer size constraints on the driver itself. The driver allocates a buffer of a different size if the hardware cannot handle the requested size or the system is low on memory. For example, a driver allocates a buffer no smaller than a memory page, or it rounds the buffer size down to the next whole sample block. Also, if the system is running low on memory, the driver allocates a buffer that is smaller than the requested size.</p>

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