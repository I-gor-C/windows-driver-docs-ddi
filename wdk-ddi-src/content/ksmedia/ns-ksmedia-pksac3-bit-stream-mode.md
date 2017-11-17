---
UID: NS.ksmedia.PKSAC3_BIT_STREAM_MODE
title: PKSAC3_BIT_STREAM_MODE
author: windows-driver-content
description: The KSAC3_BIT_STREAM_MODE structure specifies the bit-stream mode, which is the type of audio service that is encoded into an AC-3 stream.
old-location: audio\ksac3_bit_stream_mode.htm
ms.assetid: 1395687d-643a-40b5-9ca9-bff34c0dd6d5
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAC3_BIT_STREAM_MODE
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
ms.keywords: PKSAC3_BIT_STREAM_MODE, KSAC3_BIT_STREAM_MODE, *PKSAC3_BIT_STREAM_MODE
req.iface: 
---

# PKSAC3_BIT_STREAM_MODE structure



## -description
<p>The KSAC3_BIT_STREAM_MODE structure specifies the bit-stream mode, which is the type of audio service that is encoded into an AC-3 stream.</p>


## -syntax

````
typedef struct {
  LONG BitStreamMode;
} KSAC3_BIT_STREAM_MODE, *PKSAC3_BIT_STREAM_MODE;
````


## -struct-fields
<dl>

### -field <b>BitStreamMode</b>

<dd>
<p>Specifies the bit-stream mode. The <b>BitStreamMode</b> member is set to a value in the range 0 to 7. Specify the value of this member as one of the following constants:</p>
<table>
<tr>
<th>Constant name</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_MAIN_AUDIO</p>
</td>
<td>
<p>0</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_NO_DIALOG</p>
</td>
<td>
<p>1</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_VISUALLY_IMPAIRED</p>
</td>
<td>
<p>2</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_HEARING_IMPAIRED</p>
</td>
<td>
<p>3</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_DIALOG_ONLY</p>
</td>
<td>
<p>4</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_COMMENTARY</p>
</td>
<td>
<p>5</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_EMERGENCY_FLASH</p>
</td>
<td>
<p>6</p>
</td>
</tr>
<tr>
<td>
<p>KSAC3_SERVICE_VOICE_OVER</p>
</td>
<td>
<p>7</p>
</td>
</tr>
</table>
<p> </p>
<p>These constants correspond to the bit-stream modes that are defined in the AC-3 specification. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537212">KSPROPERTY_AC3_BIT_STREAM_MODE</a> property.</p>

<p>For more information about bit stream modes, see the AC-3 specification at the <a href="http://go.microsoft.com/fwlink/p/?linkid=8730">Dolby Laboratories</a> website. The specification is titled Digital Audio Compression Standard (AC-3).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537212">KSPROPERTY_AC3_BIT_STREAM_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAC3_BIT_STREAM_MODE structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
