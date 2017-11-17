---
UID: NS.strmini._HW_STREAM_INFORMATION
title: HW_STREAM_INFORMATION
author: windows-driver-content
description: The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an HW_STREAM_DESCRIPTOR structure.
old-location: stream\hw_stream_information.htm
ms.assetid: d1163185-4cae-4f14-ae99-78795da89fb8
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
req.alt-api: HW_STREAM_INFORMATION
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
ms.keywords: HW_STREAM_INFORMATION, HW_STREAM_INFORMATION, *PHW_STREAM_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# HW_STREAM_INFORMATION structure



## -description
<p>The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a> structure.</p>


## -syntax

````
typedef struct _HW_STREAM_INFORMATION {
  ULONG              NumberOfPossibleInstances;
  KSPIN_DATAFLOW     DataFlow;
  BOOLEAN            DataAccessible;
  ULONG              NumberOfFormatArrayEntries;
  PKSDATAFORMAT      *StreamFormatsArray;
  PVOID              ClassReserved[4];
  ULONG              NumStreamPropArrayEntries;
  PKSPROPERTY_SET    StreamPropertiesArray;
  ULONG              NumStreamEventArrayEntries;
  PKSEVENT_SET       StreamEventsArray;
  GUID               *Category;
  GUID               *Name;
  ULONG              MediumsCount;
  const KSPIN_MEDIUM *Mediums;
  BOOLEAN            BridgeStream;
  ULONG              Reserved[2];
} HW_STREAM_INFORMATION, *PHW_STREAM_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NumberOfPossibleInstances</b>

<dd>
<p>Specifies the number of possible instances of this stream that can be opened.</p>
</dd>

### -field <b>DataFlow</b>

<dd>
<p>The direction that data can travel on this stream. For unidirectional data flow, <b>DataFlow</b> has the value <b>KSPIN_DATAFLOW_IN</b> or KSPIN_DATAFLOW_OUT.</p>
</dd>

### -field <b>DataAccessible</b>

<dd>
<p>Specifies <b>TRUE</b> if the stream data is accessible to the class driver. </p>
</dd>

### -field <b>NumberOfFormatArrayEntries</b>

<dd>
<p>The number of entries in the array that begins at the address in the <b>StreamFormatsArray</b> member.</p>
</dd>

### -field <b>StreamFormatsArray</b>

<dd>
<p>Pointer to the beginning of the array of data ranges that this stream supports. (The name of this member is deceptive. This member points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures, not KSDATAFORMAT structures.)</p>
</dd>

### -field <b>ClassReserved</b>

<dd>
<p>Reserved for use by the class driver. Do not use.</p>
</dd>

### -field <b>NumStreamPropArrayEntries</b>

<dd>
<p>The number of entries in the array that begins at the address in the <b>StreamPropertiesArray</b> member.</p>
</dd>

### -field <b>StreamPropertiesArray</b>

<dd>
<p>Pointer to the beginning of the array of property sets supported by this stream.</p>
</dd>

### -field <b>NumStreamEventArrayEntries</b>

<dd>
<p>The number of entries in the array that begins at the address in the <b>StreamEventsArray</b> field.</p>
</dd>

### -field <b>StreamEventsArray</b>

<dd>
<p>Pointer to the beginning of the array of event sets supported by this stream.</p>
</dd>

### -field <b>Category</b>

<dd>
<p>Specifies the GUID of the pin category.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>Specifies the GUID of the localized Unicode string name for the pin type, stored in the Registry.</p>
</dd>

### -field <b>MediumsCount</b>

<dd>
<p>The number of entries in the array that begins at the address in the <b>Mediums</b> field.</p>
</dd>

### -field <b>Mediums</b>

<dd>
<p>Pointer to the beginning of the array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structures supported by this stream. If the minidriver does not specify a medium, the class driver uses the KSMEDIUMSETID_STANDARD, KSMEDIUM_TYPE_ANYINSTANCE medium as the default.</p>
</dd>

### -field <b>BridgeStream</b>

<dd>
<p>If <b>TRUE</b>, the communications type of this stream's underlying pin type is KSPIN_COMMUNICATION_BRIDGE. Otherwise, the default communications type of a stream is KSPIN_COMMUNICATION_SINK.</p>
<p>Most minidrivers will set this member to <b>FALSE</b>. See KSPROPERTY_PIN_COMMUNICATIONS for a description of communication types.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for use by the class driver. Do not use.</p>
</dd>
</dl>

## -remarks
<p>The class driver uses the elements of HW_STREAM_INFORMATION to handle the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a> property requests. The index within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a> structure serves as the pin type ID number.</p>

<p>Note that the class driver does not use this data to handle the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a> property. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff568299">STREAM_DATA_INTERSECT_INFO</a> for a description of how the class driver handles this property.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559690">HW_STREAM_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HW_STREAM_INFORMATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
