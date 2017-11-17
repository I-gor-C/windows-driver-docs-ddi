---
UID: NS.ks.PKSPROPERTY_MEMBERSHEADER
title: PKSPROPERTY_MEMBERSHEADER
author: windows-driver-content
description: A driver provides a structure of type KSPROPERTY_MEMBERSHEADER to describe the size and type of each element in an array containing property values or ranges.
old-location: stream\ksproperty_membersheader.htm
ms.assetid: 8a5d8f8c-4924-4ae0-a7b2-8d2b04a49a9e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_MEMBERSHEADER
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
ms.keywords: PKSPROPERTY_MEMBERSHEADER, KSPROPERTY_MEMBERSHEADER, *PKSPROPERTY_MEMBERSHEADER
req.iface: 
---

# PKSPROPERTY_MEMBERSHEADER structure



## -description
<p>A driver provides a structure of type KSPROPERTY_MEMBERSHEADER to describe the size and type of each element in an array containing property values or ranges.</p>


## -syntax

````
typedef struct {
  ULONG MembersFlags;
  ULONG MembersSize;
  ULONG MembersCount;
  ULONG Flags;
} KSPROPERTY_MEMBERSHEADER, *PKSPROPERTY_MEMBERSHEADER;
````


## -struct-fields
<dl>

### -field <b>MembersFlags</b>

<dd>
<p>Specifies the type of entries in the members list. The size of valid values is determined by value type, as specified in the <b>PropTypeSet</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565132">KSPROPERTY_DESCRIPTION</a> structure. The number of range pairs is determined by <b>MembersCount</b>. This should be one of the values listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_MEMBER_RANGES</p>
</td>
<td>
<p>Indicates that list members are ranges, of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff564394">KSPROPERTY_BOUNDS_LONG</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564395">KSPROPERTY_BOUNDS_LONGLONG</a>.</p>
</td>
</tr>
<tr>
<td>
<p>
<dl>

### -field KSPROPERTY_MEMBER


### -field _STEPPEDRANGES

</dl>
</p>
</td>
<td>
<p>Indicates that the following members are stepped values within ranges, of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn936838">KSPROPERTY_STEPPING_LONG</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/dn936841">KSPROPERTY_STEPPING_LONGLONG</a>..</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_MEMBER_VALUES</p>
</td>
<td>
<p>Each entry in the members array is a single value.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MembersSize</b>

<dd>
<p>Specifies the size, in bytes, of an individual array element.</p>
</dd>

### -field <b>MembersCount</b>

<dd>
<p>Specifies the number of entries in the members array.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the type of entries in the members list. The size of valid values is determined by value type, as specified in the <b>PropTypeSet</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565132">KSPROPERTY_DESCRIPTION</a> structure. The number of range pairs is determined by <b>MembersCount</b>. This should be one of the values listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_MEMBER_RANGES</p>
</td>
<td>
<p>Indicates that list members are ranges, of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff564394">KSPROPERTY_BOUNDS_LONG</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564395">KSPROPERTY_BOUNDS_LONGLONG</a>.</p>
</td>
</tr>
<tr>
<td>
<p>
<dl>

### -field KSPROPERTY_MEMBER


### -field _STEPPEDRANGES

</dl>
</p>
</td>
<td>
<p>Indicates that the following members are stepped values within ranges, of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn936838">KSPROPERTY_STEPPING_LONG</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/dn936841">KSPROPERTY_STEPPING_LONGLONG</a>..</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_MEMBER_VALUES</p>
</td>
<td>
<p>Each entry in the members array is a single value.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>The size of the array can be determined by multiplying <b>MembersCount</b> by <b>MembersSize</b>.</p>

<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff565190">KSPROPERTY_MEMBERSLIST</a> structure contains a KSPROPERTY_MEMBERSHEADER structure as its first member. The second member, <b>Members</b>, points to an array of property values or ranges.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565176">KSPROPERTY_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565190">KSPROPERTY_MEMBERSLIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565132">KSPROPERTY_DESCRIPTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564394">KSPROPERTY_BOUNDS_LONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564395">KSPROPERTY_BOUNDS_LONGLONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn936838">KSPROPERTY_STEPPING_LONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn936841">KSPROPERTY_STEPPING_LONGLONG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_MEMBERSHEADER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
