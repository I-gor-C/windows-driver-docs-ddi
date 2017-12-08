---
UID: NS.ksmedia.PKSWAVE_OUTPUT_CAPABILITIES
title: PKSWAVE_OUTPUT_CAPABILITIES
author: windows-driver-content
description: The KSWAVE_OUTPUT_CAPABILITIES structure is used to describe the output capabilities of a device.
old-location: stream\kswave_output_capabilities.htm
old-project: stream
ms.assetid: 3f7d534d-bfd8-4aca-a14d-97c047fb5aeb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSWAVE_OUTPUT_CAPABILITIES, KSWAVE_OUTPUT_CAPABILITIES, *PKSWAVE_OUTPUT_CAPABILITIES
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
req.alt-api: KSWAVE_OUTPUT_CAPABILITIES
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

# PKSWAVE_OUTPUT_CAPABILITIES structure



## -description
<p>The KSWAVE_OUTPUT_CAPABILITIES structure is used to describe the output capabilities of a device.</p>


## -syntax

````
typedef struct {
  ULONG MaximumChannelsPerConnection;
  ULONG MinimumBitsPerSample;
  ULONG MaximumBitsPerSample;
  ULONG MinimumSampleFrequency;
  ULONG MaximumSampleFrequency;
  ULONG TotalConnections;
  ULONG StaticConnections;
  ULONG StreamingConnections;
  ULONG ActiveConnections;
  ULONG ActiveStaticConnections;
  ULONG ActiveStreamingConnections;
  ULONG Total3DConnections;
  ULONG Static3DConnections;
  ULONG Streaming3DConnections;
  ULONG Active3DConnections;
  ULONG ActiveStatic3DConnections;
  ULONG ActiveStreaming3DConnections;
  ULONG TotalSampleMemory;
  ULONG FreeSampleMemory;
  ULONG LargestFreeContiguousSampleMemory;
} KSWAVE_OUTPUT_CAPABILITIES, *PKSWAVE_OUTPUT_CAPABILITIES;
````


## -struct-fields
<dl>

### -field MaximumChannelsPerConnection

<dd>
<p>Specifies the maximum number of channels per connection.</p>
</dd>

### -field MinimumBitsPerSample

<dd>
<p>Specifies the minimum bits per sample.</p>
</dd>

### -field MaximumBitsPerSample

<dd>
<p>Specifies the maximum bits per sample.</p>
</dd>

### -field MinimumSampleFrequency

<dd>
<p>Specifies the minimum sampling frequency.</p>
</dd>

### -field MaximumSampleFrequency

<dd>
<p>Specifies the maximum sampling frequency.</p>
</dd>

### -field TotalConnections

<dd>
<p>Indicates the total number of connections.</p>
</dd>

### -field StaticConnections

<dd>
<p>Indicates the number of static connections.</p>
</dd>

### -field StreamingConnections

<dd>
<p>Indicates the number of streaming connections.</p>
</dd>

### -field ActiveConnections

<dd>
<p>Indicates the number of active connections.</p>
</dd>

### -field ActiveStaticConnections

<dd>
<p>Indicates the number of active static connections.</p>
</dd>

### -field ActiveStreamingConnections

<dd>
<p>Indicates the number of active streaming connections.</p>
</dd>

### -field Total3DConnections

<dd>
<p>Indicates the total number of 3D connections.</p>
</dd>

### -field Static3DConnections

<dd>
<p>Indicates the number of static 3D connections.</p>
</dd>

### -field Streaming3DConnections

<dd>
<p>Indicates the number of streaming 3D connections.</p>
</dd>

### -field Active3DConnections

<dd>
<p>Indicates the number of active 3D connections.</p>
</dd>

### -field ActiveStatic3DConnections

<dd>
<p>Indicates the number of static 3D connections.</p>
</dd>

### -field ActiveStreaming3DConnections

<dd>
<p>Indicates the number of streaming 3D connections.</p>
</dd>

### -field TotalSampleMemory

<dd>
<p>Specifies the total amount of sample memory.</p>
</dd>

### -field FreeSampleMemory

<dd>
<p>Specifies the available free sample memory.</p>
</dd>

### -field LargestFreeContiguousSampleMemory

<dd>
<p>Specifies the largest, free contiguous amount of sample memory.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566523">KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</a> property.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566523">KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSWAVE_OUTPUT_CAPABILITIES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
