---
UID: NE.ksmedia.KSPROPERTY_AUDIOSIGNALPROCESSING
title: KSPROPERTY_AUDIOSIGNALPROCESSING
author: windows-driver-content
description: The KSPROPERTY_AUDIOSIGNALPROCESSING enumeration defines a constant that is used by audio drivers in connection with audio processing modes on pins.
old-location: audio\ksproperty_audiosignalprocessing.htm
old-project: audio
ms.assetid: E0552FFF-E10F-496A-9D67-0AE06AF7B877
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_AUDIOSIGNALPROCESSING
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

# KSPROPERTY_AUDIOSIGNALPROCESSING enumeration



## -description
<p>The KSPROPERTY_AUDIOSIGNALPROCESSING enumeration defines a constant that is used  by audio drivers in connection with audio processing modes on pins.</p>


## -syntax

````
typedef enum _KSPROPERTY_AUDIOSIGNALPROCESSING { 
  KSPROPERTY_AUDIOSIGNALPROCESSING_MODES
} KSPROPERTY_AUDIOSIGNALPROCESSING;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_AUDIOSIGNALPROCESSING_MODES"></a><a id="ksproperty_audiosignalprocessing_modes"></a><b>KSPROPERTY_AUDIOSIGNALPROCESSING_MODES</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn457708">KSPROPERTY_AUDIOSIGNALPROCESSING_MODES</a> property.</p>
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
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn457708">KSPROPERTY_AUDIOSIGNALPROCESSING_MODES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn457710">KSPROPSETID_AudioSignalProcessing</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSPROPERTY_AUDIOSIGNALPROCESSING enumeration%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
