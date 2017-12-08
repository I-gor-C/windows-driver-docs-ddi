---
UID: NI.ntddcdvd.IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE
title: IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE
author: windows-driver-content
description: Queries the logical unit for the size of the buffer that is required to hold the Advanced Access Control System (AACS) Media Key Block (MKB).
old-location: storage\ioctl_aacs_read_media_key_block_size.htm
old-project: storage
ms.assetid: 2b8e5461-c935-46d8-afe3-c82a7566a4c7
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT, DVD_STRUCTURE_FORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE
req.alt-loc: Ntddcdvd.h
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
---

# IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE IOCTL



## -description
Queries the logical unit for the size of the buffer that is required to hold the Advanced Access Control System (AACS) Media Key Block (MKB). 
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains the <a href="storage.aacs_layer_number">AACS_LAYER_NUMBER</a> number of the layer.
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(AACS_LAYER_NUMBER).
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a ULONG that holds the size in bytes of the full AACS MKB for this media.
Use this value to determine the size of the buffer to allocate for <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_aacs_read_media_key_block.md">IOCTL_AACS_READ_MEDIA_KEY_BLOCK</a>. The size is always a multiple of 32,768 (0x8000).
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS if the operation succeeds. The following failure codes are common with this operation:

Failure of one of the copy protection mechanisms.
The authentication process has failed.
No AACS protection exists for this media.
The AGID for AACS has not been established.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains the <a href="storage.aacs_layer_number">AACS_LAYER_NUMBER</a> number of the layer.The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains the <a href="storage.aacs_layer_number">AACS_LAYER_NUMBER</a>AACS_LAYER_NUMBER number of the layer.
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(AACS_LAYER_NUMBER).
<b>Parameters.DeviceIoControl.InputBufferLength</b>Parameters.DeviceIoControl.InputBufferLength in the I/O stack location indicates the size, in bytes, of the buffer, which must be >= <b>sizeof</b>sizeof(AACS_LAYER_NUMBER).


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a ULONG that holds the size in bytes of the full AACS MKB for this media.The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains a ULONG that holds the size in bytes of the full AACS MKB for this media.
Use this value to determine the size of the buffer to allocate for <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_aacs_read_media_key_block.md">IOCTL_AACS_READ_MEDIA_KEY_BLOCK</a>. The size is always a multiple of 32,768 (0x8000).Use this value to determine the size of the buffer to allocate for <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_aacs_read_media_key_block.md">IOCTL_AACS_READ_MEDIA_KEY_BLOCK</a><b>IOCTL_AACS_READ_MEDIA_KEY_BLOCK</b>IOCTL_AACS_READ_MEDIA_KEY_BLOCK. The size is always a multiple of 32,768 (0x8000).


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS if the operation succeeds. The following failure codes are common with this operation:The <b>Information</b>Information field is set to the number of bytes transferred. The <b>Status</b>Status field is set to STATUS_SUCCESS if the operation succeeds. The following failure codes are common with this operation:

<dl>
<dt><a id="STATUS_COPY_PROTECTION_FAILURE_or_STG_E_STATUS_COPY_PROTECTION_FAILURE"></a><a id="status_copy_protection_failure_or_stg_e_status_copy_protection_failure"></a><a id="STATUS_COPY_PROTECTION_FAILURE_OR_STG_E_STATUS_COPY_PROTECTION_FAILURE"></a>STATUS_COPY_PROTECTION_FAILURE or STG_E_STATUS_COPY_PROTECTION_FAILURE</dt>
<dd>
Failure of one of the copy protection mechanisms.
</dd>
<dt><a id="STATUS_CSS_AUTHENTICATION_FAILURE_or_STG_E_CSS_AUTHENTICATION_FAILURE"></a><a id="status_css_authentication_failure_or_stg_e_css_authentication_failure"></a><a id="STATUS_CSS_AUTHENTICATION_FAILURE_OR_STG_E_CSS_AUTHENTICATION_FAILURE"></a>STATUS_CSS_AUTHENTICATION_FAILURE or STG_E_CSS_AUTHENTICATION_FAILURE</dt>
<dd>
The authentication process has failed.
</dd>
<dt><a id="STATUS_CSS_KEY_NOT_PRESENT_or_STG_E_CSS_KEY_NOT_PRESENT"></a><a id="status_css_key_not_present_or_stg_e_css_key_not_present"></a><a id="STATUS_CSS_KEY_NOT_PRESENT_OR_STG_E_CSS_KEY_NOT_PRESENT"></a>STATUS_CSS_KEY_NOT_PRESENT or STG_E_CSS_KEY_NOT_PRESENT</dt>
<dd>
No AACS protection exists for this media.
</dd>
<dt><a id="STATUS_CSS_KEY_NOT_ESTABLISHED_or_STG_E_CSS_KEY_NOT_ESTABLISHED"></a><a id="status_css_key_not_established_or_stg_e_css_key_not_established"></a><a id="STATUS_CSS_KEY_NOT_ESTABLISHED_OR_STG_E_CSS_KEY_NOT_ESTABLISHED"></a>STATUS_CSS_KEY_NOT_ESTABLISHED or STG_E_CSS_KEY_NOT_ESTABLISHED</dt>
<dd>
The AGID for AACS has not been established.
</dd>
</dl>
<dt><a id="STATUS_COPY_PROTECTION_FAILURE_or_STG_E_STATUS_COPY_PROTECTION_FAILURE"></a><a id="status_copy_protection_failure_or_stg_e_status_copy_protection_failure"></a><a id="STATUS_COPY_PROTECTION_FAILURE_OR_STG_E_STATUS_COPY_PROTECTION_FAILURE"></a>STATUS_COPY_PROTECTION_FAILURE or STG_E_STATUS_COPY_PROTECTION_FAILURE</dt><a id="STATUS_COPY_PROTECTION_FAILURE_or_STG_E_STATUS_COPY_PROTECTION_FAILURE"></a><a id="status_copy_protection_failure_or_stg_e_status_copy_protection_failure"></a><a id="STATUS_COPY_PROTECTION_FAILURE_OR_STG_E_STATUS_COPY_PROTECTION_FAILURE"></a>STATUS_COPY_PROTECTION_FAILURE or STG_E_STATUS_COPY_PROTECTION_FAILURE
<dd>
Failure of one of the copy protection mechanisms.
</dd>
Failure of one of the copy protection mechanisms.Failure of one of the copy protection mechanisms.

<dt><a id="STATUS_CSS_AUTHENTICATION_FAILURE_or_STG_E_CSS_AUTHENTICATION_FAILURE"></a><a id="status_css_authentication_failure_or_stg_e_css_authentication_failure"></a><a id="STATUS_CSS_AUTHENTICATION_FAILURE_OR_STG_E_CSS_AUTHENTICATION_FAILURE"></a>STATUS_CSS_AUTHENTICATION_FAILURE or STG_E_CSS_AUTHENTICATION_FAILURE</dt><a id="STATUS_CSS_AUTHENTICATION_FAILURE_or_STG_E_CSS_AUTHENTICATION_FAILURE"></a><a id="status_css_authentication_failure_or_stg_e_css_authentication_failure"></a><a id="STATUS_CSS_AUTHENTICATION_FAILURE_OR_STG_E_CSS_AUTHENTICATION_FAILURE"></a>STATUS_CSS_AUTHENTICATION_FAILURE or STG_E_CSS_AUTHENTICATION_FAILURE
<dd>
The authentication process has failed.
</dd>
The authentication process has failed.The authentication process has failed.

<dt><a id="STATUS_CSS_KEY_NOT_PRESENT_or_STG_E_CSS_KEY_NOT_PRESENT"></a><a id="status_css_key_not_present_or_stg_e_css_key_not_present"></a><a id="STATUS_CSS_KEY_NOT_PRESENT_OR_STG_E_CSS_KEY_NOT_PRESENT"></a>STATUS_CSS_KEY_NOT_PRESENT or STG_E_CSS_KEY_NOT_PRESENT</dt><a id="STATUS_CSS_KEY_NOT_PRESENT_or_STG_E_CSS_KEY_NOT_PRESENT"></a><a id="status_css_key_not_present_or_stg_e_css_key_not_present"></a><a id="STATUS_CSS_KEY_NOT_PRESENT_OR_STG_E_CSS_KEY_NOT_PRESENT"></a>STATUS_CSS_KEY_NOT_PRESENT or STG_E_CSS_KEY_NOT_PRESENT
<dd>
No AACS protection exists for this media.
</dd>
No AACS protection exists for this media.No AACS protection exists for this media.

<dt><a id="STATUS_CSS_KEY_NOT_ESTABLISHED_or_STG_E_CSS_KEY_NOT_ESTABLISHED"></a><a id="status_css_key_not_established_or_stg_e_css_key_not_established"></a><a id="STATUS_CSS_KEY_NOT_ESTABLISHED_OR_STG_E_CSS_KEY_NOT_ESTABLISHED"></a>STATUS_CSS_KEY_NOT_ESTABLISHED or STG_E_CSS_KEY_NOT_ESTABLISHED</dt><a id="STATUS_CSS_KEY_NOT_ESTABLISHED_or_STG_E_CSS_KEY_NOT_ESTABLISHED"></a><a id="status_css_key_not_established_or_stg_e_css_key_not_established"></a><a id="STATUS_CSS_KEY_NOT_ESTABLISHED_OR_STG_E_CSS_KEY_NOT_ESTABLISHED"></a>STATUS_CSS_KEY_NOT_ESTABLISHED or STG_E_CSS_KEY_NOT_ESTABLISHED
<dd>
The AGID for AACS has not been established.
</dd>
The AGID for AACS has not been established.The AGID for AACS has not been established.


## -remarks
The IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE request will not work if the media in the logical unit is not AACS protected.

The IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE request corresponds to one of the steps of the Advanced Access Content System (AACS) authentication algorithm (AACS-Auth). For a complete description of AACS-Auth, see the <i>Advanced Access Content System, Introduction and Common Cryptographic Elements</i> specification that is published by Advanced Access Content System Licensing Administrator (AACS LA).

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>