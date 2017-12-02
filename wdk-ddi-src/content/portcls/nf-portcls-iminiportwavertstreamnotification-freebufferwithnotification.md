---
UID: NF.portcls.IMiniportWaveRTStreamNotification.FreeBufferWithNotification
title: IMiniportWaveRTStreamNotification::FreeBufferWithNotification
author: windows-driver-content
description: The FreeBufferWithNotification method is used to free an audio buffer previously allocated with a call to IMiniportWaveRTStreamNotification::AllocateBufferWithNotification.
old-location: audio\iminiportwavertstreamnotification_freebufferwithnotification.htm
old-project: audio
ms.assetid: 2ec9222b-d9e7-4386-ac66-30c5436f549d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportWaveRTStreamNotification, FreeBufferWithNotification, IMiniportWaveRTStreamNotification::FreeBufferWithNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWaveRTStreamNotification.FreeBufferWithNotification
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Passive level.
req.iface: IMiniportWaveRTStreamNotification
---

# IMiniportWaveRTStreamNotification::FreeBufferWithNotification method



## -description
<p>The <code>FreeBufferWithNotification</code> method is used to free an audio buffer previously allocated with a call to <a href="audio.iminiportwavertstreamnotification_allocatebufferwithnotification">IMiniportWaveRTStreamNotification::AllocateBufferWithNotification</a>.</p>


## -syntax

````
VOID FreeBufferWithNotification(
  [in] PMDL  AudioBufferMdl,
  [in] ULONG SizeWritten
);
````


## -parameters
<dl>

### -param AudioBufferMdl [in]

<dd>
<p>Specifies a memory descriptor list (<a href="..\wdm\ns-wdm--mdl.md">MDL</a>) previously allocated with a call to <b>IMiniportWaveRTStreamNotification::AllocateBufferWithNotification</b>.</p>
</dd>

### -param SizeWritten [in]

<dd>
<p>Output pointer for the number of bytes the method has written to the Attributes buffer. This parameter points to a ULONG variable into which the method writes the byte count.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The port driver calls this method to free an audio buffer that was allocated with a previous call to <b>IMiniportWaveRTStreamNotification::AllocateBufferWithNotification</b>.</p>

## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later Windows operating systems.</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Passive level.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iminiportwavertstreamnotification.md">IMiniportWaveRTStreamNotification</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--mdl.md">MDL</a>
</dt>
<dt>
<a href="audio.iminiportwavertstreamnotification_allocatebufferwithnotification">IMiniportWaveRTStreamNotification::AllocateBufferWithNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWaveRTStreamNotification::FreeBufferWithNotification method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
