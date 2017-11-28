---
UID: NS.fltuserstructures._FILTER_AGGREGATE_BASIC_INFORMATION
title: FILTER_AGGREGATE_BASIC_INFORMATION
author: windows-driver-content
description: The FILTER_AGGREGATE_BASIC_INFORMATION structure contains basic information for a minifilter or legacy filter driver.
old-location: ifsk\filter_aggregate_basic_information.htm
old-project: ifsk
ms.assetid: c60ac4b8-3e55-42c8-a693-4fc6bbec0de8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILTER_AGGREGATE_BASIC_INFORMATION, FILTER_AGGREGATE_BASIC_INFORMATION, *PFILTER_AGGREGATE_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltuserstructures.h
req.include-header: FltUser.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Microsoft Windows Server 2003 SP1 and Windows XP SP2 with filter manager rollup.  For more information on the filter manager rollup package for Windows XP SP2, see article 914882, "The filter manager rollup package for Windows XP SP2," in the Microsoft Knowledge Base.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILTER_AGGREGATE_BASIC_INFORMATION
req.alt-loc: fltuserstructures.h
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

# FILTER_AGGREGATE_BASIC_INFORMATION structure



## -description
<p>The FILTER_AGGREGATE_BASIC_INFORMATION structure contains basic information for a minifilter or legacy filter driver. </p>


## -syntax

````
typedef struct _FILTER_AGGREGATE_BASIC_INFORMATION {
  ULONG NextEntryOffset;
  ULONG Flags;
  union {
    struct {
      ULONG  FrameID;
      ULONG  NumberOfInstances;
      USHORT FilterNameLength;
      USHORT FilterNameBufferOffset;
      USHORT FilterAltitudeLength;
      USHORT FilterAltitudeBufferOffset;
    } MiniFilter;
    struct {
      USHORT FilterNameLength;
      USHORT FilterNameBufferOffset;
    } LegacyFilter;
  } Type;
} FILTER_AGGREGATE_BASIC_INFORMATION, *PFILTER_AGGREGATE_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NextEntryOffset</b>

<dd>
<p>Byte offset of the next FILTER_AGGREGATE_BASIC_INFORMATION entry, if multiple entries are present in a buffer. This member is zero if no other entries follow this one. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Indicates whether the filter driver is a legacy filter or a minifilter.  This member must be one of the following values.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLTFL_AGGREGATE_INFO_IS_MINIFILTER</p>
</td>
<td>
<p>The filter is a minifilter - use the <b>MiniFilter</b> portion of the union.</p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_AGGREGATE_INFO_IS_LEGACYFILTER</p>
</td>
<td>
<p>The filter is a legacy filter - use the <b>LegacyFilter</b> portion of the union.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Type</b>

<dd>
<p> </p>
<dl>

### -field <b>MiniFilter</b>

<dd>
<p> </p>
<dl>

### -field <b>FrameID</b>

<dd>
<p>Zero-based index of the current frame. </p>
</dd>

### -field <b>NumberOfInstances</b>

<dd>
<p>Number of instances that currently exist for the minifilter. </p>
</dd>

### -field <b>FilterNameLength</b>

<dd>
<p>Length, in bytes, of the filter name. </p>
</dd>

### -field <b>FilterNameBufferOffset</b>

<dd>
<p>Byte offset of the first character of the filter name string. </p>
</dd>

### -field <b>FilterAltitudeLength</b>

<dd>
<p>Length, in bytes, of the minifilter altitude string. </p>
</dd>

### -field <b>FilterAltitudeBufferOffset</b>

<dd>
<p>Byte offset of the first character of the minifilter altitude string. </p>
</dd>
</dl>
</dd>

### -field <b>LegacyFilter</b>

<dd>
<p> </p>
<dl>

### -field <b>FilterNameLength</b>

<dd>
<p>Length, in bytes, of the filter name. </p>
</dd>

### -field <b>FilterNameBufferOffset</b>

<dd>
<p>Byte offset of the first character of the filter name string. </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The FILTER_AGGREGATE_BASIC_INFORMATION structure is passed as a parameter to routines such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff540485">FilterFindFirst</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff540488">FilterFindNext</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff540500">FilterGetInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542060">FltEnumerateFilterInformation</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543053">FltGetFilterInformation</a>. </p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry, except the last, falls on an 8-byte boundary.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Microsoft Windows Server 2003 SP1 and Windows XP SP2 with filter manager rollup.  For more information on the filter manager rollup package for Windows XP SP2, see article 914882, "The filter manager rollup package for Windows XP SP2," in the Microsoft Knowledge Base. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltuserstructures.h (include FltUser.h or FltKernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541567">FILTER_AGGREGATE_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541587">FILTER_FULL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540481">FilterFindClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540485">FilterFindFirst</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540488">FilterFindNext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540500">FilterGetInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542060">FltEnumerateFilterInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543053">FltGetFilterInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILTER_AGGREGATE_BASIC_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
