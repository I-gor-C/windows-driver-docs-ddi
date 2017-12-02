---
UID: NS.ksmedia.PKSWAVE_COMPATCAPS
title: PKSWAVE_COMPATCAPS
author: windows-driver-content
description: The KSWAVE_COMPATCAPS structure is used to describe the compatible capabilities of a device.
old-location: stream\kswave_compatcaps.htm
old-project: stream
ms.assetid: 92e6090e-6a31-45d9-ac6d-a20bf180f12e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSWAVE_COMPATCAPS, KSWAVE_COMPATCAPS, *PKSWAVE_COMPATCAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSWAVE_COMPATCAPS
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

# PKSWAVE_COMPATCAPS structure



## -description
<p>The KSWAVE_COMPATCAPS structure is used to describe the compatible capabilities of a device.</p>


## -syntax

````
typedef struct {
  ULONG ulDeviceType;
} KSWAVE_COMPATCAPS, *PKSWAVE_COMPATCAPS;
````


## -struct-fields
<dl>

### -field ulDeviceType

<dd>
<p>Specifies the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSWAVE_COMPATCAPS_INPUT</p>
</td>
<td>
<p>Indicates that the device accepts input.</p>
</td>
</tr>
<tr>
<td>
<p>KSWAVE_COMPATCAPS_OUTPUT</p>
</td>
<td>
<p>Indicates that the device produces output.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566516">KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES</a> property.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566516">KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSWAVE_COMPATCAPS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
