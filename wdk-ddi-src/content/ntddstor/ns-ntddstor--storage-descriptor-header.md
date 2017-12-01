---
UID: NS.ntddstor._STORAGE_DESCRIPTOR_HEADER
title: STORAGE_DESCRIPTOR_HEADER
author: windows-driver-content
description: The STORAGE_DESCRIPTOR_HEADER structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the properties of a storage device or adapter.
old-location: storage\storage_descriptor_header.htm
old-project: storage
ms.assetid: 57d019b0-7914-42f6-a888-16042aa97444
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DESCRIPTOR_HEADER, STORAGE_DESCRIPTOR_HEADER, *PSTORAGE_DESCRIPTOR_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DESCRIPTOR_HEADER
req.alt-loc: ntddstor.h
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

# STORAGE_DESCRIPTOR_HEADER structure



## -description
<p>The STORAGE_DESCRIPTOR_HEADER structure is used in conjunction with the <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> request to retrieve the properties of a storage device or adapter. </p>


## -syntax

````
typedef struct _STORAGE_DESCRIPTOR_HEADER {
  ULONG Version;
  ULONG Size;
} STORAGE_DESCRIPTOR_HEADER, *PSTORAGE_DESCRIPTOR_HEADER;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the version of the data reported. </p>
</dd>

### -field <b>Size</b>

<dd>
<p>Indicates the quantity of data reported, in bytes. </p>
</dd>
</dl>

## -remarks
<p>The data retrieved by IOCTL_STORAGE_QUERY_PROPERTY is reported in the buffer immediately following this structure. </p>

<p>The IOCTL_STORAGE_QUERY_PROPERTY request reports one of three types of properties: a device descriptor, an adapter descriptor, or a set of device IDs taken from the device's SCSI vital product data pages. Device descriptors are reported in a structure of type <a href="..\ntddstor\ns-ntddstor--storage-device-descriptor.md">STORAGE_DEVICE_DESCRIPTOR</a>. Adapter descriptors are reported in a structure of type <a href="..\ntddstor\ns-ntddstor--storage-adapter-descriptor.md">STORAGE_ADAPTER_DESCRIPTOR</a>. Vital product page device IDs are reported in a structure of type <a href="..\ntddstor\ns-ntddstor--storage-device-id-descriptor.md">STORAGE_DEVICE_ID_DESCRIPTOR</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_DESCRIPTOR_HEADER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
