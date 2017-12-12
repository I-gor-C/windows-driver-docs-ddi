---
UID: NI.ntddstor.IOCTL_STORAGE_REINITIALIZE_MEDIA
title: IOCTL_STORAGE_REINITIALIZE_MEDIA
author: windows-driver-content
description: A driver can use the IOCTL_STORAGE_REINITIALIZE_MEDIA control code to reinitialize/erase a device.
old-location: storage\ioctl_storage_reinitialize_media.htm
old-project: storage
ms.assetid: 4ECF51C3-D098-49E2-A675-78066A15C221
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION, STORAGE_ZONE_CONDITION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_STORAGE_REINITIALIZE_MEDIA
req.alt-loc: Ntddstor.h
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

# IOCTL_STORAGE_REINITIALIZE_MEDIA IOCTL



## -description

     A driver can use the <b> IOCTL_STORAGE_REINITIALIZE_MEDIA</b> control code to reinitialize/erase a device. The IOCTL offloads the erasure to the storage device; there is no guarantee as to the successful deletion or recoverability of the data of the storage device after the command completes.  This IOCTL is limited to data disks on devices in the desktop device family. In Windows Preinstallation Environment (WinPE), this IOCTL is supported for both boot and data disks.

    
   

None

None

The <b>Information</b> field is set to zero if the operation completes successfully; otherwise, it is set to a non-zero value.



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
None</p>None


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
None</p>None


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to zero if the operation completes successfully; otherwise, it is set to a non-zero value.</p>The <b>Information</b>Information field is set to zero if the operation completes successfully; otherwise, it is set to a non-zero value.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10, version 1607

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>