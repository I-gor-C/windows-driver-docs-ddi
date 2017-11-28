---
UID: NS.ks.PKSALLOCATOR_FRAMING
title: PKSALLOCATOR_FRAMING
author: windows-driver-content
description: The KSALLOCATOR_FRAMING structure is used to query framing requirements and submit allocator creation requests.
old-location: stream\ksallocator_framing.htm
old-project: stream
ms.assetid: db96eccd-6747-458b-9a9e-ec909146f3fa
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSALLOCATOR_FRAMING, KSALLOCATOR_FRAMING, *PKSALLOCATOR_FRAMING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSALLOCATOR_FRAMING
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
req.iface: 
---

# PKSALLOCATOR_FRAMING structure



## -description
<p>The KSALLOCATOR_FRAMING structure is used to query framing requirements and submit allocator creation requests.</p>


## -syntax

````
typedef struct {
  union {
    ULONG OptionsFlags;
    ULONG RequirementsFlags;
  };
  ULONG PoolType;
  ULONG Frames;
  ULONG FrameSize;
  ULONG FileAlignment;
  ULONG Reserved;
} KSALLOCATOR_FRAMING, *PKSALLOCATOR_FRAMING;
````


## -struct-fields
<dl>

### -field <b>OptionsFlags</b>

<dd>
<p>Specifies the allocator option flags specified during allocator creation for the connection point. The <b>OptionsFlags</b> member can contain one of the following values.</p>
<table>
<tr>
<th>OptionsFlags</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSALLOCATOR_OPTIONF_COMPATIBLE</p>
</td>
<td>
<p>Indicates that the framing options of the allocator being created are compatible with the downstream allocator. This option is typically specified when an in-place modifier is assigned an allocator for copy buffers. If the filter is not required to modify a given frame, it may submit the frame to the downstream filter without allocating an additional frame from the downstream allocator when this option is specified.</p>
</td>
</tr>
<tr>
<td>
<p>KSALLOCATOR_OPTIONF_SYSTEM_MEMORY</p>
</td>
<td>
<p>Indicates that system memory should be used for allocations. When specified, the allocator must allocate memory from the pool as specified in the <b>PoolType</b> member. Otherwise, it is assumed that the sink provides a system address mapping to on-board RAM or other forms of storage on the device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RequirementsFlags</b>

<dd>
<p>A value of type ULONG that describes the allocator requirements for this connection point for query operations. The <b>RequirementsFlags</b> member can contain the following values.</p>
<table>
<tr>
<th>Flag Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSALLOCATOR_REQUIREMENTF_INPLACE_MODIFIER</p>
</td>
<td>
<p>Indicates that the connection point can perform an in-place modification.</p>
</td>
</tr>
<tr>
<td>
<p>KSALLOCATOR_REQUIREMENTF_SYSTEM_MEMORY</p>
</td>
<td>
<p>Indicates that the connection point requires system memory for allocations. If this option is not set, it is assumed that the sink provides a system address space mapping to on-board RAM or other forms of storage on the device.</p>
</td>
</tr>
<tr>
<td>
<p>KSALLOCATOR_REQUIREMENTF_FRAME_INTEGRITY</p>
</td>
<td>
<p>Indicates that the connection point requires that downstream filters maintain the data integrity of specified frames.</p>
</td>
</tr>
<tr>
<td>
<p>KSALLOCATOR_REQUIREMENTF_MUST_ALLOCATE</p>
</td>
<td>
<p>Indicates that the connection point requires that it allocate any frames sent.</p>
</td>
</tr>
<tr>
<td>
<p>KSALLOCATOR_REQUIREMENTF_PREFERENCES_ONLY</p>
</td>
<td>
<p>Indicates that the Requirements flags are preferences only and the connection point is able to allocate frames that do not meet those specifications.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PoolType</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> that specifies kernel-mode allocation pool type.</p>
</dd>

### -field <b>Frames</b>

<dd>
<p>Specifies the total number of allowable outstanding frames. Zero indicates that the filter has no requirement for this member.</p>
</dd>

### -field <b>FrameSize</b>

<dd>
<p>Specifies the total size of the frame, including prefix and postfix. Zero indicates that the filter has no requirement for this member.</p>
</dd>

### -field <b>FileAlignment</b>

<dd>
<p>A value of type ULONG that describes the byte alignment to use when allocating frames. The following table describes several possible alignment values.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>FILE_BYTE_ALIGNMENT</p>
</td>
<td>
<p>1-byte alignment</p>
</td>
</tr>
<tr>
<td>
<p>FILE_WORD_ALIGNMENT</p>
</td>
<td>
<p>2-byte alignment</p>
</td>
</tr>
<tr>
<td>
<p>FILE_LONG_ALIGNMENT</p>
</td>
<td>
<p>4-byte alignment</p>
</td>
</tr>
<tr>
<td>
<p>FILE_32_BYTE_ALIGNMENT</p>
</td>
<td>
<p>32-byte alignment</p>
</td>
</tr>
<tr>
<td>
<p>FILE_64_BYTE_ALIGNMENT</p>
</td>
<td>
<p>64-byte alignment</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
</dd>
</dl>

## -remarks
<p>Use KSALLOCATOR_FRAMING to submit an allocator creation request to a handle of a sink by using IRP_MJ_CREATE.</p>

<p>When you specify a value for the <b>FileAlignment</b> member, the smallest allocation alignment is 1 byte (FILE_BYTE_ALIGNMENT). Software that functions as an allocation should support 4-byte alignment (FILE_LONG_ALIGNMENT), if possible.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561633">KsCreateAllocator</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSALLOCATOR_FRAMING structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
