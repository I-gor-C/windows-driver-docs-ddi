---
UID: NS.ksmedia.PKSRTAUDIO_GETREADPACKET_INFO
title: PKSRTAUDIO_GETREADPACKET_INFO
author: windows-driver-content
description: The KSRTAUDIO_GETREADPACKET_INFO structure describes information for an audio packet.
old-location: audio\ksrtaudio_getreadpacket_info.htm
ms.assetid: 0157FA09-C227-4BB2-BB75-0AB5802BC150
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
req.alt-api: KSRTAUDIO_GETREADPACKET_INFO
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
ms.keywords: PKSRTAUDIO_GETREADPACKET_INFO, KSRTAUDIO_GETREADPACKET_INFO, *PKSRTAUDIO_GETREADPACKET_INFO
req.iface: 
---

# PKSRTAUDIO_GETREADPACKET_INFO structure



## -description
<p>The KSRTAUDIO_GETREADPACKET_INFO structure describes information for an audio packet.</p>


## -syntax

````
typedef struct _KSRTAUDIO_GETREADPACKET_INFO {
  ULONG                PacketNumber;
  DWORD                Flags;
   ULONG64      PerformanceCounterValue;
  BOOL                  MoreData;
} KSRTAUDIO_GETREADPACKET_INFO, *PKSRTAUDIO_GETREADPACKET_INFO;
````


## -struct-fields
<dl>

### -field <b>       PacketNumber</b>

<dd>
<p>Returns the packet number relative to the start of capture. </p>
</dd>

### -field <b>       Flags</b>

<dd>
<p>Reserved for future use. Must be set to 0. </p>
</dd>

### -field <b>PerformanceCounterValue</b>

<dd>
<p>Returns the performance counter value corresponding to the sampling instant of the first sample in the packet. </p>
</dd>

### -field <b>        MoreData</b>

<dd>
<p>Returns TRUE if there is more data ready immediately. The OS may optionally immediately call this routine again after processing the packet to get the next packet information. If the driver returns FALSE, then capture is operating at real time. </p>
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
<p>Available in Windows 10 and later Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt786974">KSPROPERTY_RTAUDIO_GETREADPACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSRTAUDIO_GETREADPACKET_INFO structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
