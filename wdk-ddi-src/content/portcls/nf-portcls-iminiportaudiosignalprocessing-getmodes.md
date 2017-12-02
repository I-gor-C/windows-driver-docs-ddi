---
UID: NF.portcls.IMiniportAudioSignalProcessing.GetModes
title: IMiniportAudioSignalProcessing::GetModes
author: windows-driver-content
description: The GetModes method, Gets the audio signal processing modes supported by an audio pin.
old-location: audio\iminiportaudiosignalprocessing_getmodes.htm
old-project: audio
ms.assetid: 7175453E-DF6D-45F0-B666-CF4FCF1F880C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportAudioSignalProcessing, GetModes, IMiniportAudioSignalProcessing::GetModes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportAudioSignalProcessing.GetModes
req.alt-loc: Portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IMiniportAudioSignalProcessing
---

# IMiniportAudioSignalProcessing::GetModes method



## -description
<p>The GetModes method, Gets the audio signal processing modes supported by an audio pin.</p>


## -syntax

````
NTSTATUS GetModes(
  [in]            ULONG                            Pin,
  [out, optional] (*NumSignalProcessingModes) GUID *SignalProcessingModes,
  [in, out]       ULONG                            *NumSignalProcessingModes
);
````


## -parameters
<dl>

### -param Pin [in]

<dd>
<p>The index of the audio pin.</p>
</dd>

### -param SignalProcessingModes [out, optional]

<dd>
<p>This parameter is optional. It returns an array of GUIDs that identify the  signal processing modes supported by the  <i>Pin</i> parameter.</p>
</dd>

### -param NumSignalProcessingModes [in, out]

<dd>
<p>When used as an input, it specifies the number of elements that can be written to the buffer that is specified in <i>SignalProcessingModes</i>. When used as an output, it returns the number of elements that were written to the buffer.</p>
</dd>
</dl>

## -returns
<p><b>GetModes</b> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>If <i>SignalProcessingModes</i> is NULL, then <b>GetModes</b> writes the number of supported modes to <i>NumSignalProcessingModes</i> and returns STATUS_SUCCESS. This allows callers to query the number of supported modes in order to allocate buffers.</p>

<p>If <i>SignalProcessingModes</i> is not NULL, then <b>GetModes</b> verifies that <i>NumSignalProcessingModes</i> is greater than or equal to the number of supported modes. If it is, then the method writes the supported modes to the <i>SignalProcessingModes</i> buffer, writes the actual number of supported modes to <i>NumSignalProcessingModes</i>, and returns STATUS_SUCCESS.</p>

<p>The following table presents and explains  the error messages than can be returned by <b>GetModes</b>.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iminiportaudiosignalprocessing.md">IMiniportAudioSignalProcessing</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportAudioSignalProcessing::GetModes method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
