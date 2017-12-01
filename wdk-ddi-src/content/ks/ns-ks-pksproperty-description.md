---
UID: NS.ks.PKSPROPERTY_DESCRIPTION
title: PKSPROPERTY_DESCRIPTION
author: windows-driver-content
description: The KSPROPERTY_DESCRIPTION structure specifies the size and type of values contained in a specific property.
old-location: stream\ksproperty_description.htm
old-project: stream
ms.assetid: d3d59dca-7214-493c-bb70-4391696fe017
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_DESCRIPTION, KSPROPERTY_DESCRIPTION, *PKSPROPERTY_DESCRIPTION
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
req.alt-api: KSPROPERTY_DESCRIPTION
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

# PKSPROPERTY_DESCRIPTION structure



## -description
<p>The KSPROPERTY_DESCRIPTION structure specifies the size and type of values contained in a specific property.</p>


## -syntax

````
typedef struct {
  ULONG        AccessFlags;
  ULONG        DescriptionSize;
  KSIDENTIFIER PropTypeSet;
  ULONG        MembersListCount;
  ULONG        Reserved;
} KSPROPERTY_DESCRIPTION, *PKSPROPERTY_DESCRIPTION;
````


## -struct-fields
<dl>

### -field <b>AccessFlags</b>

<dd>
<p>Specifies the access allowed to this property. A basic-support request sets this member to the bitwise OR of the flags for all the access types that the handler supports for this property. For a list of possible flag values, see <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a>.</p>
</dd>

### -field <b>DescriptionSize</b>

<dd>
<p>Specifies total size in bytes of the KSPROPERTY_DESCRIPTION structure and any values entries that follow it. If the basic-support property request returns no values entries, this member is the size of KSPROPERTY_DESCRIPTION.</p>
</dd>

### -field <b>PropTypeSet</b>

<dd>
<p>A structure of type <a href="stream.ksidentifier">KSIDENTIFIER</a>. If supported by the specific property, specifies the type of values contained in this property. This group is uniquely specified by a GUID, such that new types of values may be created without overlapping with extensions to this set. The value types indicate the type of the value (like VT_BOOL, VT_UI4 in the standard set). This is GUID_NULL, with an identifier of zero, if values information is not supported by this property.</p>
</dd>

### -field <b>MembersListCount</b>

<dd>
<p>Specifies the number of <a href="stream.ksproperty_membersheader">KSPROPERTY_MEMBERSHEADER</a> structures to follow this header.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use. Set to zero.</p>
</dd>
</dl>

## -remarks
<p>A driver returns the <b>KSPROPERTY_DESCRIPTION</b> structure in response to a basic support property request from a client.</p>

<p>The property values type set is specified by a KSIDENTIFIER structure. The basic set supported is <a href="https://msdn.microsoft.com/library/windows/hardware/ff566576">KSPROPSETID_General</a>. The identifiers within that set are the standard VARENUM types used for OLE.</p>

<p>The values information that may follow the KSPROPERTY_DESCRIPTION structure is described by a list of <a href="stream.ksproperty_memberslist">KSPROPERTY_MEMBERSLIST</a> structures, each of which contains data range information.</p>

<p>For more information, see <a href="NULL">KS Properties</a>.</p>

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
<a href="stream.ksproperty_values">KSPROPERTY_VALUES</a>
</dt>
<dt>
<a href="stream.ksproperty_membersheader">KSPROPERTY_MEMBERSHEADER</a>
</dt>
<dt>
<a href="stream.ksproperty_item">KSPROPERTY_ITEM</a>
</dt>
<dt>
<a href="stream.ksidentifier">KSIDENTIFIER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_DESCRIPTION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
