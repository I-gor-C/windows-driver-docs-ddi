---
UID: NS.ksmedia._KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT
title: KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT
author: windows-driver-content
description: The KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure describes the constraints specific to any signal processing mode.
old-location: audio\ksaudio_packetsize_processingmode_constraint.htm
old-project: audio
ms.assetid: 0BC6A03C-CF6D-4F56-985E-933E87200DFE
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT, KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT
req.alt-loc: ksmedia.h
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

# KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT structure



## -description
<p>The <b>KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT</b> structure describes the constraints specific to any signal processing mode.</p>


## -syntax

````
typedef struct _KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT {
  GUID  ProcessingMode;
  ULONG SamplesPerProcessingPacket;
  ULONG ProcessingPacketDurationInHns;
} KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT;
````


## -struct-fields
<dl>

### -field <b>ProcessingMode</b>

<dd>
<p>The signal processing mode that this constraint applies to.</p>
</dd>

### -field <b>SamplesPerProcessingPacket</b>

<dd>
<p>The processing frame size for the processing mode, expressed in number of samples. If this value is 0, the constraint is expressed by the <b>ProcessingPacketDurationInHns</b> field.</p>
</dd>

### -field <b>ProcessingPacketDurationInHns</b>

<dd>
<p>The processing frame size for the processing mode, expressed in hundred-nanosecond (HNS) units. This field is ignored if <b>SamplesPerProcessingPacket</b> is nonzero.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn965561">KSAUDIO_PACKETSIZE_CONSTRAINTS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
