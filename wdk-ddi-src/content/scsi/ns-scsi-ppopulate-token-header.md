---
UID: NS.scsi.PPOPULATE_TOKEN_HEADER
title: PPOPULATE_TOKEN_HEADER
author: windows-driver-content
description: A populate token parameter list starts with a POPULATE_TOKEN_HEADER structure. This is the header for the parameters in a command data block (CDB) of the POPULATE TOKEN command.
old-location: storage\populate_token_header.htm
ms.assetid: 897C74A3-041D-487E-8891-7161B76ABAA1
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsi.h
req.include-header: Scsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POPULATE_TOKEN_HEADER
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
ms.keywords: PPOPULATE_TOKEN_HEADER, POPULATE_TOKEN_HEADER, *PPOPULATE_TOKEN_HEADER
req.iface: 
req.product: Windows 10 or later.
---

# PPOPULATE_TOKEN_HEADER structure



## -description
<p>A populate token parameter list starts with a <b>POPULATE_TOKEN_HEADER</b> structure. This is the header for the parameters in a command data block (CDB) of the  POPULATE TOKEN command.</p>


## -syntax

````
typedef struct _POPULATE_TOKEN_HEADER {
  UCHAR PopulateTokenDataLength[2];
  UCHAR Immediate  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2;
  UCHAR InactivityTimeout[4];
  UCHAR Reserved3[6];
  UCHAR BlockDeviceRangeDescriptorListLength[2];
  UCHAR BlockDeviceRangeDescriptor[ANYSIZE_ARRAY];
} POPULATE_TOKEN_HEADER, *PPOPULATE_TOKEN_HEADER;
````


## -struct-fields
<dl>

### -field <b>PopulateTokenDataLength</b>

<dd>
<p>The length of this structure beginning with the <i>Immediate</i> parameter and include all of the elements of the <b>BlockDeviceRangeDescriptor</b> array.</p>
</dd>

### -field <b>Immediate</b>

<dd>
<p>If set, the status of the POPULATE TOKEN command is returned immediately after receipt and validation of the range descriptors. Otherwise, status is returned after all command processing is complete.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved bits.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>InactivityTimeout</b>

<dd>
<p>The timeout duration for which the copy provider waits for the next command using the token created for this representation of data (ROD). The validity of the token created  for the ROD described by this structure expires at this timeout value.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>BlockDeviceRangeDescriptorListLength</b>

<dd>
<p>The length, in bytes, for all  of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures in the <b>BlockDeviceRangeDescriptor</b> array.</p>
</dd>

### -field <b>BlockDeviceRangeDescriptor</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures which describe the logical blocks representing the file being read from the LUN.</p>
</dd>
</dl>

## -remarks
<p>The <b>POPULATE_TOKEN_HEADER</b> structure contains a series of <a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures which describe the token ROD.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20POPULATE_TOKEN_HEADER structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
