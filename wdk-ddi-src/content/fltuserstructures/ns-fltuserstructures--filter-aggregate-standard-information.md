---
UID: NS.fltuserstructures._FILTER_AGGREGATE_STANDARD_INFORMATION
title: FILTER_AGGREGATE_STANDARD_INFORMATION
author: windows-driver-content
description: The FILTER_AGGREGATE_STANDARD_INFORMATION structure contains information about a minifilter or legacy filter driver.
old-location: ifsk\filter_aggregate_standard_information.htm
old-project: ifsk
ms.assetid: 76703a53-45c1-4dfa-b8aa-4f73d4d84538
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILTER_AGGREGATE_STANDARD_INFORMATION, FILTER_AGGREGATE_STANDARD_INFORMATION, *PFILTER_AGGREGATE_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltuserstructures.h
req.include-header: FltUser.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILTER_AGGREGATE_STANDARD_INFORMATION
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

# FILTER_AGGREGATE_STANDARD_INFORMATION structure



## -description
<p>The FILTER_AGGREGATE_STANDARD_INFORMATION structure contains information about a minifilter or legacy filter driver.</p>


## -syntax

````
typedef struct _FILTER_AGGREGATE_STANDARD_INFORMATION {
  ULONG NextEntryOffset;
  ULONG Flags;
  union {
    struct {
      ULONG  Flags;
      ULONG  FrameID;
      ULONG  NumberOfInstances;
      USHORT FilterNameLength;
      USHORT FilterNameBufferOffset;
      USHORT FilterAltitudeLength;
      USHORT FilterAltitudeBufferOffset;
    } MiniFilter;
    struct {
      ULONG  Flags;
      USHORT FilterNameLength;
      USHORT FilterNameBufferOffset;
      USHORT FilterAltitudeLength;
      USHORT FilterAltitudeBufferOffset;
    } LegacyFilter;
  } Type;
} FILTER_AGGREGATE_STANDARD_INFORMATION, *PFILTER_AGGREGATE_STANDARD_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NextEntryOffset</b>

<dd>
<p>Byte offset of the next FILTER_AGGREGATE_STANDARD_INFORMATION entry, if multiple entries are present in a buffer. This member is zero if no other entries follow this one.</p>
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
<p>FLTFL_ASI_IS_MINIFILTER</p>
</td>
<td>
<p>The filter is a minifilter - use the <b>MiniFilter</b> portion of the union.</p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_ASI_IS_LEGACYFILTER</p>
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
<dl>

### -field <b>MiniFilter</b>

<dd>
<p>Nested structure variable with the following members:</p>
<dl>

### -field <b>Flags</b>

<dd>
<p>There are currently no flags defined for this member.</p>
</dd>

### -field <b>FrameID</b>

<dd>
<p>Zero-based index used to identify the filter manager frame that the minifilter is in.</p>
</dd>

### -field <b>NumberOfInstances</b>

<dd>
<p>Number of instances that currently exist for the minifilter.</p>
</dd>

### -field <b>FilterNameLength</b>

<dd>
<p>Length, in bytes, of the minifilter name string.</p>
</dd>

### -field <b>FilterNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode minifilter name string.  The string is not NULL-terminated.</p>
</dd>

### -field <b>FilterAltitudeLength</b>

<dd>
<p>Length, in bytes, of the minifilter altitude string.</p>
</dd>

### -field <b>FilterAltitudeBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode minifilter altitude string. The string is not NULL-terminated.</p>
</dd>
</dl>
</dd>

### -field <b>LegacyFilter</b>

<dd>
<p>Nested structure variable with the following members:</p>
<dl>

### -field <b>Flags</b>

<dd>
<p>There are currently no flags defined for this member.</p>
</dd>

### -field <b>FilterNameLength</b>

<dd>
<p>Length, in bytes, of the legacy filter name string.</p>
</dd>

### -field <b>FilterNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode legacy filter name string.  The string is not NULL-terminated.</p>
</dd>

### -field <b>FilterAltitudeLength</b>

<dd>
<p>Length, in bytes, of the legacy filter altitude string.</p>
</dd>

### -field <b>FilterAltitudeBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode legacy filter altitude string.  The string is not NULL-terminated.</p>
<p>Starting with Windows Vista, altitudes are assigned to legacy filter drivers based on the driver's load order group.  This ensures that minifilter drivers will layer properly above and below legacy filter drivers even if one or more of the filter drivers are loaded out-of-order.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The FILTER_AGGREGATE_STANDARD_INFORMATION structure can be allocated from paged or nonpaged pool.  This structure is passed as a parameter to routines such as:</p>

<p>
<a href="ifsk.filterfindfirst">FilterFindFirst</a>
</p>

<p>
<a href="ifsk.filterfindnext">FilterFindNext</a>
</p>

<p>
<a href="ifsk.filtergetinformation">FilterGetInformation</a>
</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltenumeratefilterinformation.md">FltEnumerateFilterInformation</a>
</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltgetfilterinformation.md">FltGetFilterInformation</a>
</p>

<p>The FILTER_AGGREGATE_STANDARD_INFORMATION structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry falls on an 8-byte boundary.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows Vista. </p>
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
<a href="..\fltuserstructures\ns-fltuserstructures--filter-aggregate-basic-information.md">FILTER_AGGREGATE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--filter-full-information.md">FILTER_FULL_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.filterfindfirst">FilterFindFirst</a>
</dt>
<dt>
<a href="ifsk.filterfindnext">FilterFindNext</a>
</dt>
<dt>
<a href="ifsk.filtergetinformation">FilterGetInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenumeratefilterinformation.md">FltEnumerateFilterInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetfilterinformation.md">FltGetFilterInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILTER_AGGREGATE_STANDARD_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
