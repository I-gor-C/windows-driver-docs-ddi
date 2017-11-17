---
UID: NE.ksmedia.KS_VIDEODECODER_FLAGS
title: KS_VIDEODECODER_FLAGS
author: windows-driver-content
description: The KS_VIDEODECODER_FLAGS enumeration defines video decoder capabilities.
old-location: stream\ks_videodecoder_flags.htm
ms.assetid: 120d7714-8c32-4b83-adc2-c9a933e541e5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_VIDEODECODER_FLAGS
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
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# KS_VIDEODECODER_FLAGS enumeration



## -description
<p>The KS_VIDEODECODER_FLAGS enumeration defines video decoder capabilities.</p>


## -syntax

````
typedef enum  { 
  KS_VIDEODECODER_FLAGS_CAN_DISABLE_OUTPUT   = 0X0001,
  KS_VIDEODECODER_FLAGS_CAN_USE_VCR_LOCKING  = 0X0002,
  KS_VIDEODECODER_FLAGS_CAN_INDICATE_LOCKED  = 0X0004
} KS_VIDEODECODER_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="KS_VIDEODECODER_FLAGS_CAN_DISABLE_OUTPUT"></a><a id="ks_videodecoder_flags_can_disable_output"></a><b>KS_VIDEODECODER_FLAGS_CAN_DISABLE_OUTPUT</b>

<dd>
<p>The decoder can translate its output lines. Video decoders that use a video port use this flag.</p>
</dd>

### -field <a id="KS_VIDEODECODER_FLAGS_CAN_USE_VCR_LOCKING"></a><a id="ks_videodecoder_flags_can_use_vcr_locking"></a><b>KS_VIDEODECODER_FLAGS_CAN_USE_VCR_LOCKING</b>

<dd>
<p>The video decoder can alter its phase locked loop (PLL) timings to lock on to noisy signals. This flag typically is used when the video source is a VCR that introduces variability in the vertical and horizontal sync timing.</p>
</dd>

### -field <a id="KS_VIDEODECODER_FLAGS_CAN_INDICATE_LOCKED"></a><a id="ks_videodecoder_flags_can_indicate_locked"></a><b>KS_VIDEODECODER_FLAGS_CAN_INDICATE_LOCKED</b>

<dd>
<p>The video decoder can distinguish whether it has locked to an incoming analog video signal.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566047">KSPROPERTY_VIDEODECODER_CAPS_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_VIDEODECODER_FLAGS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
