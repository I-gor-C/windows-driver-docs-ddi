---
UID: NS.ksmedia.PKSRTAUDIO_SETWRITEPACKET_INFO
title: PKSRTAUDIO_SETWRITEPACKET_INFO
author: windows-driver-content
description: The KSRTAUDIO_SETWRITEPACKET_INFO structure describes information associated with an audio packet.
old-location: audio\ksrtaudio_setwritepacket_info.htm
ms.assetid: 641DE2B5-7903-4D25-A280-F2BCCE8B1500
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10 and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSRTAUDIO_SETWRITEPACKET_INFO
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
ms.keywords: PKSRTAUDIO_SETWRITEPACKET_INFO, KSRTAUDIO_SETWRITEPACKET_INFO, *PKSRTAUDIO_SETWRITEPACKET_INFO
req.iface: 
---

# PKSRTAUDIO_SETWRITEPACKET_INFO structure



## -description
<p>The KSRTAUDIO_SETWRITEPACKET_INFO structure describes information associated with an audio packet.</p>


## -syntax

````
typedef struct _KSRTAUDIO_SETWRITEPACKET_INFO {
  ULONG PacketNumber;
  DWORD Flags ;
  ULONG EosPacketLength;
} KSRTAUDIO_SETWRITEPACKET_INFO, *PKSRTAUDIO_SETWRITEPACKET_INFO;
````


## -struct-fields
<dl>

### -field <b>PacketNumber</b>

<dd>
<p> The number of the packet written by the OS to the WaveRT buffer. Depending on the values returned by the driver in the KSPROPERTY_RTAUDIO_GETPACKETCOUNT property, the PacketNumber may skip values. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt171559">KSPROPERTY_RTAUDIO_PACKETCOUNT</a>. 

</p>
</dd>

### -field <b>Flags </b>

<dd>
<p>Additional attributes related to the packet or stream. 

</p>
<p><i>KSSTREAM_HEADER_OPTIONSF_ENDOFSTREAM</i> - This flag indicates that this packet represents the end of the data stream. 

</p>
</dd>

### -field <b>EosPacketLength</b>

<dd>
<p>The length of the EOS packet if <i>KSSTREAM_HEADER_OPTIONSF_ENDOFSTREAM</i> is specified in Flags. Zero is a valid value. If <i>KSSTREAM_HEADER_OPTIONSF_ENDOFSTREAM</i> is not specified in Flags, this parameter is ignored. The EosPacketLength is measured in bytes.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10 and later Windows operating systems. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt786975">KSPROPERTY_RTAUDIO_SETWRITEPACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSRTAUDIO_SETWRITEPACKET_INFO structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
