---
UID: NI.bthhfpddi.IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE
title: IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE
author: windows-driver-content
description: The IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's speaker.
old-location: audio\ioctl_bthhfp_speaker_get_volume_status_update.htm
old-project: audio
ms.assetid: CE122D3F-CD8F-47F5-88E0-AB0140A8DE1E
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE
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

# IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL



## -description
<p>The <b>IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE</b> 
   IOCTL Gets the volume level setting of the Bluetooth device's speaker.</p>


## -ioctlparameters

### -input-buffer
<p>A BOOL that is set to TRUE to request an immediate update. Otherwise, set this to FALSE.</p>

### -input-buffer-length
<p>The size of a BOOL.</p>

<p>The size of a BOOL.</p>

### -output-buffer
<p>A LONG that represents the speaker's volume level in 1/65536 decibels.</p>

<p>A LONG that represents the speaker's volume level in 1/65536 decibels.</p>

<p>A LONG that represents the speaker's volume level in 1/65536 decibels.</p>

### -output-buffer-length
<p>The size of a LONG.</p>

<p>The size of a LONG.</p>

<p>The size of a LONG.</p>

<p>The size of a LONG.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If a request is already pending the new request fails and a STATUS_INVALID_DEVICE_REQUEST message is returned.</p>

<p>If a request is already pending the new request fails and a STATUS_INVALID_DEVICE_REQUEST message is returned.</p>

<p>If a request is already pending the new request fails and a STATUS_INVALID_DEVICE_REQUEST message is returned.</p>

<p>If a request is already pending the new request fails and a STATUS_INVALID_DEVICE_REQUEST message is returned.</p>

<p>If a request is already pending the new request fails and a STATUS_INVALID_DEVICE_REQUEST message is returned.</p>

## -remarks
<p>This request will complete immediately if the input parameter is TRUE, or if the volume status has changed since the last request. Otherwise this request will remain pending until the volume status changes or the request is cancelled.</p>

<p>The audio driver sends this request to get the initial speaker and microphone volume levels, and sends subsequent requests "asking" to be  updated when the levels change. The driver stores the volume levels in appropriate context data. When the volume level changes, the audio driver generates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a> event for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the speaker or microphone path.</p>

<p>The request’s output parameter is the same as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property value.</p>

<p>This request will complete immediately if the input parameter is TRUE, or if the volume status has changed since the last request. Otherwise this request will remain pending until the volume status changes or the request is cancelled.</p>

<p>The audio driver sends this request to get the initial speaker and microphone volume levels, and sends subsequent requests "asking" to be  updated when the levels change. The driver stores the volume levels in appropriate context data. When the volume level changes, the audio driver generates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a> event for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the speaker or microphone path.</p>

<p>The request’s output parameter is the same as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property value.</p>

<p>This request will complete immediately if the input parameter is TRUE, or if the volume status has changed since the last request. Otherwise this request will remain pending until the volume status changes or the request is cancelled.</p>

<p>The audio driver sends this request to get the initial speaker and microphone volume levels, and sends subsequent requests "asking" to be  updated when the levels change. The driver stores the volume levels in appropriate context data. When the volume level changes, the audio driver generates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a> event for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the speaker or microphone path.</p>

<p>The request’s output parameter is the same as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property value.</p>

<p>This request will complete immediately if the input parameter is TRUE, or if the volume status has changed since the last request. Otherwise this request will remain pending until the volume status changes or the request is cancelled.</p>

<p>The audio driver sends this request to get the initial speaker and microphone volume levels, and sends subsequent requests "asking" to be  updated when the levels change. The driver stores the volume levels in appropriate context data. When the volume level changes, the audio driver generates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a> event for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the speaker or microphone path.</p>

<p>The request’s output parameter is the same as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property value.</p>

<p>This request will complete immediately if the input parameter is TRUE, or if the volume status has changed since the last request. Otherwise this request will remain pending until the volume status changes or the request is cancelled.</p>

<p>The audio driver sends this request to get the initial speaker and microphone volume levels, and sends subsequent requests "asking" to be  updated when the levels change. The driver stores the volume levels in appropriate context data. When the volume level changes, the audio driver generates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a> event for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the speaker or microphone path.</p>

<p>The request’s output parameter is the same as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property value.</p>

<p>This request will complete immediately if the input parameter is TRUE, or if the volume status has changed since the last request. Otherwise this request will remain pending until the volume status changes or the request is cancelled.</p>

<p>The audio driver sends this request to get the initial speaker and microphone volume levels, and sends subsequent requests "asking" to be  updated when the levels change. The driver stores the volume levels in appropriate context data. When the volume level changes, the audio driver generates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a> event for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the speaker or microphone path.</p>

<p>The request’s output parameter is the same as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn302027">Bluetooth HFP DDI IOCTLs</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537128">KSEVENT_CONTROL_CHANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE control code%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
