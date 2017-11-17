---
UID: NS.strmini._HW_STREAM_HEADER
title: HW_STREAM_HEADER
author: windows-driver-content
description: The HW_STREAM_HEADER structure describes the kernel streaming semantics supported by the minidriver as a whole, as part of a HW_STREAM_DESCRIPTOR structure.
old-location: stream\hw_stream_header.htm
ms.assetid: 1931c640-666b-4db5-8d05-eab43ae96665
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HW_STREAM_HEADER
req.alt-loc: strmini.h
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
ms.keywords: HW_STREAM_HEADER, HW_STREAM_HEADER, *PHW_STREAM_HEADER
req.iface: 
req.product: Windows 10 or later.
---

# HW_STREAM_HEADER structure



## -description
<p>The HW_STREAM_HEADER structure describes the kernel streaming semantics supported by the minidriver as a whole, as part of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a> structure.</p>


## -syntax

````
typedef struct _HW_STREAM_HEADER {
  ULONG             NumberOfStreams;
  ULONG             SizeOfHwStreamInformation;
  ULONG             NumDevPropArrayEntries;
  PKSPROPERTY_SET   DevicePropertiesArray;
  ULONG             NumDevEventArrayEntries;
  PKSEVENT_SET      DeviceEventsArray;
  PKSTOPOLOGY       Topology;
  PHW_EVENT_ROUTINE DeviceEventRoutine;
  ULONG             Reserved[2];
} HW_STREAM_HEADER, *PHW_STREAM_HEADER;
````


## -struct-fields
<dl>

### -field <b>NumberOfStreams</b>

<dd>
<p>The number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559692">HW_STREAM_INFORMATION</a> structures that follow this header.</p>
</dd>

### -field <b>SizeOfHwStreamInformation</b>

<dd>
<p>The size, in bytes, of the HW_STREAM_INFORMATION structure.</p>
</dd>

### -field <b>NumDevPropArrayEntries</b>

<dd>
<p>The number of entries in the array pointed to by <b>DevicePropertiesArray</b>.</p>
</dd>

### -field <b>DevicePropertiesArray</b>

<dd>
<p>Pointer to the beginning of the array of property sets that the minidriver as a whole supports. (Property sets supported by individual streams can be found in the <b>StreamPropertiesArray</b> member of the stream's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559692">HW_STREAM_INFORMATION</a> structure.)</p>
</dd>

### -field <b>NumDevEventArrayEntries</b>

<dd>
<p>The number of entries in the array pointed to by <b>DeviceEventsArray</b>.</p>
</dd>

### -field <b>DeviceEventsArray</b>

<dd>
<p>Pointer to the beginning of the array of event sets supported by the minidriver.</p>
</dd>

### -field <b>Topology</b>

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567146">KSTOPOLOGY</a> structure that describes the minidriver's internal topology of nodes and pins. The class driver uses this to handle the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566598">KSPROPSETID_Topology</a> property set for the minidriver.</p>
</dd>

### -field <b>DeviceEventRoutine</b>

<dd>
<p>Points to the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568457">StrMiniEvent</a> routine.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559692">HW_STREAM_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HW_STREAM_HEADER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
