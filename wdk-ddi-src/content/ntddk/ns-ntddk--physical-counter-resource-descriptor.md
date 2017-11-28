---
UID: NS.ntddk._PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR
title: PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR
author: windows-driver-content
description: The PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure describes the counter resources available on the platform.
old-location: kernel\physical_counter_resource_descriptor.htm
old-project: kernel
ms.assetid: 9b4c35a1-04b9-4d4d-9a57-2f5711ec7418
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR, PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR, *PPHYSICAL_COUNTER_RESOURCE_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure



## -description
<p>The <b>PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR</b> structure describes the counter resources available on the platform.</p>


## -syntax

````
typedef struct _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR {
  PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE Type;
  ULONG                                     Flags;
  union {
    ULONG  CounterIndex;
    ULONG  ExtendedRegisterAddress;
    struct {
      ULONG Begin;
      ULONG End;
    } Range;
  } u;
} PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR, *PPHYSICAL_COUNTER_RESOURCE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Indicates the type of counter resource described by the structure. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff558797">PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE</a> enumeration constants:</p>
<ul>
<li>
<p><b>ResourceTypeSingle</b></p>
</li>
<li>
<p><b>ResourceTypeRange</b></p>
</li>
<li>
<p><b>ResourceTypeExtendedCounterConfiguration</b></p>
</li>
<li>
<p><b>ResourceTypeOverflow</b></p>
</li>
</ul>
</dd>

### -field <b>Flags</b>

<dd>
<p>No flags are currently defined. Set this member to zero.</p>
</dd>

### -field <b>u</b>

<dd>
<p>A union that can contain a <b>CounterIndex</b>, <b>ExtendedRegisterAddress</b>, or <b>Range</b> value.</p>
<dl>

### -field <b>CounterIndex</b>

<dd>
<p>A physical counter index. </p>
</dd>

### -field <b>ExtendedRegisterAddress</b>

<dd>
<p>An extended configuration register address. </p>
</dd>

### -field <b>Range</b>

<dd>
<p>A range of counter indexes. </p>
<dl>

### -field <b>Begin</b>

<dd>
<p>The starting counter index of a block of contiguous counters. </p>
</dd>

### -field <b>End</b>

<dd>
<p>The ending counter index of a block of contiguous counters. </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>Most processors have performance monitor units that contain a number of hardware counters for measuring various aspects of system performance. The <b>PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR</b> structure describes a counter resource, which can be a single hardware counter, a block of contiguous counters, or a counter overflow interrupt. This structure's <b>Type</b> member indicates which type of counter resource is described by the structure.</p>

<p>To specify a set of counter resources, a kernel-mode client can provide an array of <b>PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR</b> structures. A <a href="https://msdn.microsoft.com/library/windows/hardware/ff558798">PHYSICAL_COUNTER_RESOURCE_LIST</a> structure serves as a header for the array. The client can allocate and free the set of counter resources described by the array as a single unit.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 7 and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558797">PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558798">PHYSICAL_COUNTER_RESOURCE_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
