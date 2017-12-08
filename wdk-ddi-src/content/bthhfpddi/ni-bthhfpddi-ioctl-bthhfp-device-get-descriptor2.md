---
UID: NI.bthhfpddi.IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2
title: IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2
author: windows-driver-content
description: The IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL Gets descriptive information about the paired Handsfree profile (HFP) device.
old-location: audio\ioctl_bthhfp_device_get_descriptor2.htm
old-project: audio
ms.assetid: B72D0236-1C2B-4D0B-86B4-4E9B667BA1B3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2
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
req.iface: 
---

# IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL



## -description
<p>The <b>IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2</b> 
   IOCTL Gets descriptive information about the paired Handsfree profile (HFP) device.</p>
<p>This IOCTL is available in Windows 8.1 and later operating systems, and it supersedes <a href="..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-descriptor.md">IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR</a>.</p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>A buffer containing a <a href="..\bthhfpddi\ns-bthhfpddi--bthhfp-descriptor2.md">BTHHFP_DESCRIPTOR2</a> structure followed by any other data that is referenced by the structure. This is true,  if the output buffer size is sufficient and the request succeeds. In particular, the buffer includes storage for the string that is referenced by the <i>FriendlyName</i> field of the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>A buffer containing a <a href="..\bthhfpddi\ns-bthhfpddi--bthhfp-descriptor2.md">BTHHFP_DESCRIPTOR2</a> structure followed by any other data that is referenced by the structure. This is true,  if the output buffer size is sufficient and the request succeeds. In particular, the buffer includes storage for the string that is referenced by the <i>FriendlyName</i> field of the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>A buffer containing a <a href="..\bthhfpddi\ns-bthhfpddi--bthhfp-descriptor2.md">BTHHFP_DESCRIPTOR2</a> structure followed by any other data that is referenced by the structure. This is true,  if the output buffer size is sufficient and the request succeeds. In particular, the buffer includes storage for the string that is referenced by the <i>FriendlyName</i> field of the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

### -output-buffer-length
<p>The size of a <b>BTHHFP_DESCRIPTOR2</b> structure and referenced data.</p>

<p>The size of a <b>BTHHFP_DESCRIPTOR2</b> structure and referenced data.</p>

<p>The size of a <b>BTHHFP_DESCRIPTOR2</b> structure and referenced data.</p>

<p>The size of a <b>BTHHFP_DESCRIPTOR2</b> structure and referenced data.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If the routine succeeds, then Status is set to STATUS_SUCCESS and the <i>Information</i> member is the number of bytes that the routine writes to the output buffer. Note this can be larger than the size of the <b>BTHHFP_DESCRIPTOR2</b> structure, as the output buffer may contain other data referenced by the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>If Status is set to STATUS_BUFFER_TOO_SMALL, then <i>Information</i> is the size of the buffer that the caller should allocate for this request.</p>

<p>If the routine succeeds, then Status is set to STATUS_SUCCESS and the <i>Information</i> member is the number of bytes that the routine writes to the output buffer. Note this can be larger than the size of the <b>BTHHFP_DESCRIPTOR2</b> structure, as the output buffer may contain other data referenced by the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>If Status is set to STATUS_BUFFER_TOO_SMALL, then <i>Information</i> is the size of the buffer that the caller should allocate for this request.</p>

<p>If the routine succeeds, then Status is set to STATUS_SUCCESS and the <i>Information</i> member is the number of bytes that the routine writes to the output buffer. Note this can be larger than the size of the <b>BTHHFP_DESCRIPTOR2</b> structure, as the output buffer may contain other data referenced by the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>If Status is set to STATUS_BUFFER_TOO_SMALL, then <i>Information</i> is the size of the buffer that the caller should allocate for this request.</p>

<p>If the routine succeeds, then Status is set to STATUS_SUCCESS and the <i>Information</i> member is the number of bytes that the routine writes to the output buffer. Note this can be larger than the size of the <b>BTHHFP_DESCRIPTOR2</b> structure, as the output buffer may contain other data referenced by the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>If Status is set to STATUS_BUFFER_TOO_SMALL, then <i>Information</i> is the size of the buffer that the caller should allocate for this request.</p>

<p>If the routine succeeds, then Status is set to STATUS_SUCCESS and the <i>Information</i> member is the number of bytes that the routine writes to the output buffer. Note this can be larger than the size of the <b>BTHHFP_DESCRIPTOR2</b> structure, as the output buffer may contain other data referenced by the <b>BTHHFP_DESCRIPTOR2</b> structure.</p>

<p>If Status is set to STATUS_BUFFER_TOO_SMALL, then <i>Information</i> is the size of the buffer that the caller should allocate for this request.</p>

## -remarks
<p>The audio driver sends this request to obtain information about an enabled GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS device interface. The information does not change while the interface is enabled, but can change while the interface is disabled. Therefore the audio driver sends this request shortly after discovering an enabled device interface and uses the information to build an appropriate KSFILTER_DESCRIPTOR structure.</p>

<p>The audio driver sends this request once with an output buffer size of zero (0) in order to determine the required output buffer size. In this case, the request will complete with Status STATUS_BUFFER_TOO_SMALL and the <i>Information</i> parameter will  contain the required buffer size. The audio driver then allocates the necessary storage and sends the request again. Typically an audio driver will keep a pointer to this storage location in its device context for reference during later activity.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<dt>
<a href="..\bthhfpddi\ns-bthhfpddi--bthhfp-descriptor2.md">BTHHFP_DESCRIPTOR2</a>
</dt>
<dt>
<a href="..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-descriptor.md">IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 control code%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
