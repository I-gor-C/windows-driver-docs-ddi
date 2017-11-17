---
UID: NE.ksmedia.KS_CompressionCaps
title: KS_CompressionCaps
author: windows-driver-content
description: The KS_CompressionCaps enumeration defines compression capabilities of a device.
old-location: stream\ks_compressioncaps.htm
ms.assetid: 47781af6-bf14-4b95-bef2-506aadb2d1fb
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
req.alt-api: KS_CompressionCaps
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

# KS_CompressionCaps enumeration



## -description
<p>The KS_CompressionCaps enumeration defines compression capabilities of a device.</p>


## -syntax

````
typedef enum  { 
  KS_CompressionCaps_CanQuality   = 1,
  KS_CompressionCaps_CanCrunch    = 2,
  KS_CompressionCaps_CanKeyFrame  = 4,
  KS_CompressionCaps_CanBFrame    = 8,
  KS_CompressionCaps_CanWindow    = 0x10
} KS_CompressionCaps;
````


## -enum-fields
<dl>

### -field <a id="KS_CompressionCaps_CanQuality"></a><a id="ks_compressioncaps_canquality"></a><a id="KS_COMPRESSIONCAPS_CANQUALITY"></a><b>KS_CompressionCaps_CanQuality</b>

<dd>
<p>The video compressor supports quality settings.</p>
</dd>

### -field <a id="KS_CompressionCaps_CanCrunch"></a><a id="ks_compressioncaps_cancrunch"></a><a id="KS_COMPRESSIONCAPS_CANCRUNCH"></a><b>KS_CompressionCaps_CanCrunch</b>

<dd>
<p>The video compressor can compress the video to a specified data rate. If a minidriver supports this capability, the <b>dwBitRate</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567700">KS_VIDEOINFOHEADER</a> structure specifies the default data rate.</p>
</dd>

### -field <a id="KS_CompressionCaps_CanKeyFrame"></a><a id="ks_compressioncaps_cankeyframe"></a><a id="KS_COMPRESSIONCAPS_CANKEYFRAME"></a><b>KS_CompressionCaps_CanKeyFrame</b>

<dd>
<p>The video compressor supports a user-specified key-frame rate.</p>
</dd>

### -field <a id="KS_CompressionCaps_CanBFrame"></a><a id="ks_compressioncaps_canbframe"></a><a id="KS_COMPRESSIONCAPS_CANBFRAME"></a><b>KS_CompressionCaps_CanBFrame</b>

<dd>
<p>The video compressor supports a user-specified P frame interval. The frames that occur between the key frames and P frames are bidirectional (B) frames.</p>
</dd>

### -field <a id="KS_CompressionCaps_CanWindow"></a><a id="ks_compressioncaps_canwindow"></a><a id="KS_COMPRESSIONCAPS_CANWINDOW"></a><b>KS_CompressionCaps_CanWindow</b>

<dd>
<p>The video compressor supports a user-specified window size (that is, the number of frames whose average size cannot exceed the specified data rate).</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567700">KS_VIDEOINFOHEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565979">KSPROPERTY_VIDEOCOMPRESSION_GETINFO_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_CompressionCaps enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
