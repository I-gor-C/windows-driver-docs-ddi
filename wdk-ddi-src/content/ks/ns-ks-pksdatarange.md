---
UID: NS.ks.PKSDATARANGE
title: PKSDATARANGE
author: windows-driver-content
description: The KSDATARANGE structure is a variable-length structure that describes a range of data formats.
old-location: stream\ksdatarange.htm
ms.assetid: 76d8adf2-935d-4f78-aff2-c061414fe094
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
req.alt-api: KSDATAFORMAT
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
ms.keywords: PKSDATARANGE, KSDATAFORMAT, *PKSDATAFORMAT, KSDATARANGE, *PKSDATARANGE
req.iface: 
---

# PKSDATARANGE structure



## -description
<p>The KSDATARANGE structure is a variable-length structure that describes a range of data formats.</p>


## -syntax

````
typedef union {
  struct {
    ULONG FormatSize;
    ULONG Flags;
    ULONG SampleSize;
    ULONG Reserved;
    GUID  MajorFormat;
    GUID  SubFormat;
    GUID  Specifier;
  };
  LONGLONG Alignment;
} KSDATAFORMAT, *PKSDATAFORMAT, KSDATARANGE, *PKSDATARANGE;
````


## -struct-fields
<dl>

### -field <b>FormatSize</b>

<dd>
<p>Specifies the size, in bytes, of this structure. This must be at least <b>sizeof</b>(KSDATARANGE), but can be larger for specific settings of <b>MajorFormat</b>, <b>SubFormat</b>, and <b>Specifier</b>. See the descriptions for these members for more information. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Set Flags to KSDATARANGE_ATTRIBUTES (0x2) to indicate that the following KSDATARANGE is to be interpreted as an attribute list that uses the <a href="https://msdn.microsoft.com/library/windows/hardware/mt727894">KSATTRIBUTE_LIST</a> structure.</p>
</dd>

### -field <b>SampleSize</b>

<dd>
<p>This member is ignored.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Drivers must set this member to zero.</p>
</dd>

### -field <b>MajorFormat</b>

<dd>
<p>Specifies either the specific major format of a data format that this data range matches, or KSDATAFORMAT_TYPE_WILDCARD if this data range matches all major formats. When <b>MajorFormat</b> has this value, both <b>SubFormat</b> and <b>Specifier</b> must also take on their wild card values. For more information about this member, see <b>Remarks</b>.</p>
</dd>

### -field <b>SubFormat</b>

<dd>
<p>Specifies either the specific subformat of a data format that this data range matches, or KSDATAFORMAT_SUBTYPE_WILDCARD if this data range matches all subformats. (In this instance, the specifier is not required to be its wild card value, unless <b>MajorFormat</b> is KSDATAFORMAT_TYPE_WILDCARD.) For more information about this member, see <b>Remarks</b>.</p>
</dd>

### -field <b>Specifier</b>

<dd>
<p>Specifies either the specifier of the data format that this data range matches, or KSDATAFORMAT_SPECIFIER_WILDCARD if this data range matches all specifier values. For more information about this member, see <b>Remarks</b>.</p>
</dd>

### -field <b>Alignment</b>

<dd>
<p>This member specifies the memory alignment in bytes for this buffer.</p>
</dd>
</dl>

## -remarks
<p>Drivers use data ranges to describe the ranges of data formats they support.</p>

<p>For a list of <b>MajorFormat</b>, <b>SubFormat</b>, and <b>Specifier</b> GUIDs, see <a href="NULL">Stream Categories</a> and its subtopics.</p>

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
<a href="NULL">Stream Categories</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSDATARANGE union%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
