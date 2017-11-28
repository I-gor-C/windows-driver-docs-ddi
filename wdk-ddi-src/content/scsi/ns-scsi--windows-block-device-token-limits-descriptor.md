---
UID: NS.scsi._WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR
title: WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR
author: windows-driver-content
description: The WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure is the third party copy descriptor for Windows systems.
old-location: storage\windows_block_device_token_limits_descriptor.htm
old-project: storage
ms.assetid: A4DB93FE-96ED-4E6D-B912-31C53AD000FF
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR, WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR, *PWINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR
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
req.alt-api: WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR
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

# WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure



## -description
<p>The <b>WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR</b> structure is the third party copy descriptor for Windows systems. This structure serves as the descriptor for the vital product data (VPD) third party copy page.</p>


## -syntax

````
typedef struct _WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR {
  UCHAR DescriptorType[2];
  UCHAR DescriptorLength[2];
  UCHAR VendorSpecific[6];
  UCHAR MaximumRangeDescriptors[2];
  UCHAR MaximumInactivityTimer[4];
  UCHAR DefaultInactivityTimer[4];
  UCHAR MaximumTokenTransferSize[8];
  UCHAR OptimalTransferCount[8];
} WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR, *PWINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>DescriptorType</b>

<dd>
<p>The descriptor type identifying this structure. The descriptor type is defined in <i>storport.h</i> as <b>BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR_TYPE_WINDOWS</b>.</p>
</dd>

### -field <b>DescriptorLength</b>

<dd>
<p>The length of this structure starting with the <b>VendorSpecific</b> member.</p>
</dd>

### -field <b>VendorSpecific</b>

<dd>
<p>Vendor specific bytes included in the descriptor. Windows applications must treat this member as reserved and ignore the reported value.</p>
</dd>

### -field <b>MaximumRangeDescriptors</b>

<dd>
<p>The maximum number of range descriptors that may be included along with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a> or the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967746">WRITE_USING_TOKEN_HEADER</a> structures.</p>
</dd>

### -field <b>MaximumInactivityTimer</b>

<dd>
<p>The maximum available to specify as the timeout value in the <b>InactivityTimeout</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a> structure.</p>
</dd>

### -field <b>DefaultInactivityTimer</b>

<dd>
<p>The default value that is used by the copy provider when the <b>InactivityTimeout</b> of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a> structure is set to 0.</p>
</dd>

### -field <b>MaximumTokenTransferSize</b>

<dd>
<p>The maximum number of logical blocks that can be specified as a total of the block range descriptors in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a> or the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967746">WRITE_USING_TOKEN_HEADER</a> structures.</p>
</dd>

### -field <b>OptimalTransferCount</b>

<dd>
<p>The optimal number of logical blocks, as a maximum, to specify as a total of the block range descriptors in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a> or the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967746">WRITE_USING_TOKEN_HEADER</a> structures. Offload data transfer performance may degrade if the transfer count is larger than this value.</p>
</dd>
</dl>

## -remarks
<p>All multibyte values are in big endian format. Prior to evaluation, these values must be converted to match the endian format of the current platform.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967744">VPD_THIRD_PARTY_COPY_PAGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967746">WRITE_USING_TOKEN_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
