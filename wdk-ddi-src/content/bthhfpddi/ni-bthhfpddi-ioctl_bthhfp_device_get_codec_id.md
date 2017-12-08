---
UID: NI.bthhfpddi.IOCTL_BTHHFP_DEVICE_GET_CODEC_ID
title: IOCTL_BTHHFP_DEVICE_GET_CODEC_ID
author: windows-driver-content
description: An audio driver can send an IOCTL_BTHHFP_DEVICE_GET_CODEC_ID control code to query the Bluetooth driver stack about the codec ID used by the HFP service. This helps the audio driver determine the sampling rate for the data.
old-location: audio\ioctl_bthhfp_device_get_codec_id.htm
old-project: audio
ms.assetid: 38B67F0E-46A4-4AB5-B122-F5DE282FE52D
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BTHHFP_DEVICE_GET_CODEC_ID
req.alt-loc: Bthhfpddi.h
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

# IOCTL_BTHHFP_DEVICE_GET_CODEC_ID IOCTL



## -description
An audio driver can send an <b>IOCTL_BTHHFP_DEVICE_GET_CODEC_ID</b> 
   control code to query the Bluetooth driver stack about the codec ID used by the HFP service. This helps the audio driver determine the sampling rate for the data.


## -ioctlparameters

### -input-buffer
An <a href="audio.hfp_bypass_codec_id_version">HFP_BYPASS_CODEC_ID_VERSION</a> enumeration value. Currently, only REQ_HFP_BYPASS_CODEC_ID_V1 is supported.

### -input-buffer-length
The size of an <a href="audio.hfp_bypass_codec_id_version">HFP_BYPASS_CODEC_ID_VERSION</a> enumeration value.

### -output-buffer
A codec ID structure containing the codec ID information. Currently, only <a href="audio.hfp_bypass_codec_id_v1">HFP_BYPASS_CODEC_ID_V1</a> is supported.

### -output-buffer-length
The size of a codec ID structure.

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
If the routine succeeds, then Status is set to STATUS_SUCCESS and the <i>Information</i> member is the codec ID.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
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
<dt>Bthhfpddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="audio.bluetooth_hfp_ddi_ioctls">Bluetooth HFP DDI IOCTLs</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IOCTL_BTHHFP_DEVICE_GET_CODEC_ID control code%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
