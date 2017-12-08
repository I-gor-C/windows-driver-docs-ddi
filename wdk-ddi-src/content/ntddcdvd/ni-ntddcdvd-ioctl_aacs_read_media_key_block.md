---
UID: NI.ntddcdvd.IOCTL_AACS_READ_MEDIA_KEY_BLOCK
title: IOCTL_AACS_READ_MEDIA_KEY_BLOCK
author: windows-driver-content
description: Queries the logical unit for the Media Key Block (MKB).
old-location: storage\ioctl_aacs_read_media_key_block.htm
old-project: storage
ms.assetid: 08852f41-1836-4c55-bf6f-0246caa2c8bd
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
req.alt-api: IOCTL_AACS_READ_MEDIA_KEY_BLOCK
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

# IOCTL_AACS_READ_MEDIA_KEY_BLOCK IOCTL



## -description
Queries the logical unit for the Media Key Block (MKB).
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains the <a href="storage.aacs_layer_number">AACS_LAYER_NUMBER</a> number of the layer.
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(AACS_LAYER_NUMBER). 
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains an opaque, variable-length MKB. The size of the MKB is always a multiple of 32,768 (0x8000). 
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS if the operation succeeds. If <b>Irp-&gt;AssociatedIrp.SystemBuffer </b>is <b>NULL</b> or the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> is not sufficient to contain the full MKB, the operation fails and returns a status of STATUS_BUFFER_TOO_SMALL, and the required buffer size is returned in <b>IoStatus.Information</b>.


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
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains an opaque, variable-length MKB. The size of the MKB is always a multiple of 32,768 (0x8000). The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains an opaque, variable-length MKB. The size of the MKB is always a multiple of 32,768 (0x8000). 


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS if the operation succeeds. If <b>Irp-&gt;AssociatedIrp.SystemBuffer </b>is <b>NULL</b> or the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> is not sufficient to contain the full MKB, the operation fails and returns a status of STATUS_BUFFER_TOO_SMALL, and the required buffer size is returned in <b>IoStatus.Information</b>.The <b>Information</b>Information field is set to the number of bytes transferred. The <b>Status</b>Status field is set to STATUS_SUCCESS if the operation succeeds. If <b>Irp-&gt;AssociatedIrp.SystemBuffer </b>Irp->AssociatedIrp.SystemBuffer is <b>NULL</b>NULL or the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer is not sufficient to contain the full MKB, the operation fails and returns a status of STATUS_BUFFER_TOO_SMALL, and the required buffer size is returned in <b>IoStatus.Information</b>IoStatus.Information.


## -remarks
The storage stack uses a READ DISC STRUCTURE command (format 0x17) with Advanced Access Control System (AACS) extensions to retrieve the MKB. IOCTL_AACS_READ_MEDIA_KEY_BLOCK request will not work if the media in the logical unit is not AACS protected. 

Unlike the MKB that is used with Content-Scrambling System (CSS) encryption, AACS MKBs are self-protected with digital signatures. The MKB structure is fully documented in the <i>Advanced Access Content System, Introduction and Common Cryptographic Elements</i> specification that is published by Advanced Access Content System Licensing Administrator (AACS LA).

The IOCTL_AACS_READ_MEDIA_KEY_BLOCK request corresponds to one of the steps of the Advanced Access Content System (AACS) authentication algorithm (AACS-Auth). For a complete description of AACS-Auth, see the <i>Advanced Access Content System, Introduction and Common Cryptographic Elements</i> specification.

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