---
UID: NS.scsi.PWRITE_USING_TOKEN_HEADER
title: PWRITE_USING_TOKEN_HEADER
author: windows-driver-content
description: The WRITE_USING_TOKEN_HEADER structure describes the destination data locations for an offload write data operation.
old-location: storage\write_using_token_header.htm
old-project: storage
ms.assetid: A46ED23A-7DB0-4792-B903-F748BCDAD55E
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PWRITE_USING_TOKEN_HEADER, WRITE_USING_TOKEN_HEADER, *PWRITE_USING_TOKEN_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsi.h
req.include-header: Scsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WRITE_USING_TOKEN_HEADER
req.alt-loc: scsi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PWRITE_USING_TOKEN_HEADER structure



## -description
<p>The <b>WRITE_USING_TOKEN_HEADER</b> structure describes the destination data locations for an offload write data operation.  The offload write data operation described by this structure is associated with a token representation of data (ROD).</p>


## -syntax

````
typedef struct _WRITE_USING_TOKEN_HEADER {
  UCHAR WriteUsingTokenDataLength[2];
  UCHAR Immediate  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2[5];
  UCHAR BlockOffsetIntoToken[8];
  UCHAR Token[BLOCK_DEVICE_TOKEN_SIZE];
  UCHAR Reserved3[6];
  UCHAR BlockDeviceRangeDescriptorListLength[2];
  UCHAR BlockDeviceRangeDescriptor[ANYSIZE_ARRAY];
} WRITE_USING_TOKEN_HEADER, *PWRITE_USING_TOKEN_HEADER;
````


## -struct-fields
<dl>

### -field <b>WriteUsingTokenDataLength</b>

<dd>
<p>The length of this structure beginning with the <i>Immediate</i> parameter and include all of the elements of the <b>BlockDeviceRangeDescriptor</b> array.</p>
</dd>

### -field <b>Immediate</b>

<dd>
<p>If set, the status of the WRITE USING TOKEN command is returned immediately after receipt and validation of the token ROD and range descriptors. Otherwise, status is returned after all command processing is complete.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved bits.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>BlockOffsetIntoToken</b>

<dd>
<p>The offset, in logical blocks,  in the ROD for <b>Token</b> indicating the start of the source data for the offload write data operation.</p>
</dd>

### -field <b>Token</b>

<dd>
<p>A token created by a previous the POPULATE TOKEN command operation.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>BlockDeviceRangeDescriptorListLength</b>

<dd>
<p>The length, in bytes, for all  of the <a href="storage.block_device_range_descriptor">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures in the <b>BlockDeviceRangeDescriptor</b> array.</p>
</dd>

### -field <b>BlockDeviceRangeDescriptor</b>

<dd>
<p>An array of <a href="storage.block_device_range_descriptor">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures which describe the destination data blocks for the offload write data transfer.</p>
</dd>
</dl>

## -remarks
<p>All multibyte values are in big endian format. Prior to setting, these values must be converted from the endian format of the current platform.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsi.h (include Scsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.block_device_range_descriptor">BLOCK_DEVICE_RANGE_DESCRIPTOR</a>
</dt>
<dt>
<a href="storage.populate_token_header">POPULATE_TOKEN_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20WRITE_USING_TOKEN_HEADER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
