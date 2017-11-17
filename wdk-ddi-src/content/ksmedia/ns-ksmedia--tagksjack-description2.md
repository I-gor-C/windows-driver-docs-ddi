---
UID: NS.ksmedia._tagKSJACK_DESCRIPTION2
title: tagKSJACK_DESCRIPTION2
author: windows-driver-content
description: The KSJACK_DESCRIPTION2 structure specifies the capabilities and the current state of a jack that supports jack presence detection.
old-location: audio\ksjack_description2.htm
ms.assetid: 0db29870-20d0-459b-a531-3dea5d073183
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSJACK_DESCRIPTION2
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
ms.keywords: tagKSJACK_DESCRIPTION2, KSJACK_DESCRIPTION2, *PKSJACK_DESCRIPTION2
req.iface: 
---

# tagKSJACK_DESCRIPTION2 structure



## -description
<p>The <code>KSJACK_DESCRIPTION2</code> structure specifies the capabilities and the current state of a jack that supports jack presence detection.</p>


## -syntax

````
typedef struct _tagKSJACK_DESCRIPTION2 {
  DWORD DeviceStateInfo;
  DWORD JackCapabilities;
} KSJACK_DESCRIPTION2, *PKSJACK_DESCRIPTION2;
````


## -struct-fields
<dl>

### -field <b>DeviceStateInfo</b>

<dd>
<p>Specifies the lower 16 bits of the DWORD parameter. This parameter indicates whether the jack is currently active, streaming, idle, or hardware not ready.</p>
</dd>

### -field <b>JackCapabilities</b>

<dd>
<p>Specifies the lower 16 bits of the DWORD parameter. This parameter is a flag and it indicates the capabilities of the jack. This flag can be set to one of the values in the following table. </p>
<table>
<tr>
<td>
<p><b>Flag</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>JACKDESC2_PRESENCE_DETECT_CAPABILITY (0x00000001)</p>
</td>
<td>
<p>Jack supports jack presence detection.</p>
</td>
</tr>
<tr>
<td>
<p>JACKDESC2_DYNAMIC_FORMAT_CHANGE_CAPABILITY (0x00000002)</p>
</td>
<td>
<p>Jack supports dynamic format change.</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about dynamic format change, see <a href="NULL">Dynamic Format Change</a>.</p>
</dd>
</dl>

## -remarks
<p>If an audio device lacks jack presence detection, the <b>IsConnected</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537136">KSJACK_DESCRIPTION</a> structure must always be set to <b>TRUE</b>. To remove the ambiguity that results from this dual meaning of the <b>TRUE</b> value for <b>IsConnected</b>, a client application can call <a href="http://go.microsoft.com/fwlink/p/?linkid=143698">IKsJackDescription2::GetJackDescription2</a> to read the <b>JackCapabilities</b> flag of the <code>KSJACK_DESCRIPTION2</code> structure. If this flag has the JACKDESC2_PRESENCE_DETECT_CAPABILITY bit set, it indicates that the endpoint does in fact support jack presence detection. In that case, the return value of the <b>IsConnected</b> member can be interpreted to accurately reflect the insertion status of the jack.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537136">KSJACK_DESCRIPTION</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=143698">IKsJackDescription2::GetJackDescription2 </a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSJACK_DESCRIPTION2 structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
