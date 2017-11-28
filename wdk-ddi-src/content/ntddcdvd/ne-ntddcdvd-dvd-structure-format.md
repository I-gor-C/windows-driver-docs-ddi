---
UID: NE.ntddcdvd.DVD_STRUCTURE_FORMAT
title: DVD_STRUCTURE_FORMAT
author: windows-driver-content
description: The DVD_STRUCTURE_FORMAT enumeration type is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request and the DVD_READ_STRUCTURE structure to retrieve a DVD descriptor.
old-location: storage\dvd_structure_format.htm
old-project: storage
ms.assetid: 0f3ca59b-f7e9-4bd7-a652-f7f0a6075d80
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: VOLUME_CONTROL, VOLUME_CONTROL, *PVOLUME_CONTROL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DVD_STRUCTURE_FORMAT
req.alt-loc: ntddcdvd.h
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

# DVD_STRUCTURE_FORMAT enumeration



## -description
<p>The DVD_STRUCTURE_FORMAT enumeration type is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560426">IOCTL_DVD_READ_STRUCTURE</a> request and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553738">DVD_READ_STRUCTURE</a> structure to retrieve a DVD descriptor.</p>


## -syntax

````
typedef enum DVD_STRUCTURE_FORMAT { 
  DvdPhysicalDescriptor      = 0,
  DvdCopyrightDescriptor     = 1,
  DvdDiskKeyDescriptor       = 2,
  DvdBCADescriptor           = 3,
  DvdManufacturerDescriptor  = 4,
  DvdMaxDescriptor           = 5
} DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="DvdPhysicalDescriptor"></a><a id="dvdphysicaldescriptor"></a><a id="DVDPHYSICALDESCRIPTOR"></a><b>DvdPhysicalDescriptor</b>

<dd>
<p>Indicates that caller is requesting a DVD physical descriptor. </p>
</dd>

### -field <a id="DvdCopyrightDescriptor"></a><a id="dvdcopyrightdescriptor"></a><a id="DVDCOPYRIGHTDESCRIPTOR"></a><b>DvdCopyrightDescriptor</b>

<dd>
<p>Indicates that caller is requesting a DVD copyright descriptor containing copyright information from the DVD lead-in area. </p>
</dd>

### -field <a id="DvdDiskKeyDescriptor"></a><a id="dvddiskkeydescriptor"></a><a id="DVDDISKKEYDESCRIPTOR"></a><b>DvdDiskKeyDescriptor</b>

<dd>
<p>Indicates that caller is requesting a DVD key descriptor containing the disc key obfuscated using the bus key. </p>
</dd>

### -field <a id="DvdBCADescriptor"></a><a id="dvdbcadescriptor"></a><a id="DVDBCADESCRIPTOR"></a><b>DvdBCADescriptor</b>

<dd>
<p>Indicates that caller is requesting a DVD burst cutting area (BCA) descriptor. </p>
</dd>

### -field <a id="DvdManufacturerDescriptor"></a><a id="dvdmanufacturerdescriptor"></a><a id="DVDMANUFACTURERDESCRIPTOR"></a><b>DvdManufacturerDescriptor</b>

<dd>
<p>Indicates that caller is requesting a DVD manufacturer descriptor containing disc manufacturing information from the DVD lead-in area. </p>
</dd>

### -field <a id="DvdMaxDescriptor"></a><a id="dvdmaxdescriptor"></a><a id="DVDMAXDESCRIPTOR"></a><b>DvdMaxDescriptor</b>

<dd>
<p>Indicates that caller is requesting a DVD max descriptor. </p>
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
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553738">DVD_READ_STRUCTURE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560426">IOCTL_DVD_READ_STRUCTURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DVD_STRUCTURE_FORMAT enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
