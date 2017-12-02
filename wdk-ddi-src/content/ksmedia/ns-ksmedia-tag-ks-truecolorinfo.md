---
UID: NS.ksmedia.tag_KS_TRUECOLORINFO
title: tag_KS_TRUECOLORINFO
author: windows-driver-content
description: The KS_TRUECOLORINFO structure describes color palette and bitmask information for video images that also contain a palette.
old-location: stream\ks_truecolorinfo.htm
old-project: stream
ms.assetid: 8297a687-1c8f-4c19-913d-2796e7ef3a60
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tag_KS_TRUECOLORINFO, KS_TRUECOLORINFO, *PKS_TRUECOLORINFO
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
req.alt-api: KS_TRUECOLORINFO
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

# tag_KS_TRUECOLORINFO structure



## -description
<p>The KS_TRUECOLORINFO structure describes color palette and bitmask information for video images that also contain a palette.</p>


## -syntax

````
typedef struct tag_KS_TRUECOLORINFO {
  DWORD      dwBitMasks[KS_iMASK_COLORS];
  KS_RGBQUAD bmiColors[KS_iPALETTE_COLORS];
} KS_TRUECOLORINFO, *PKS_TRUECOLORINFO;
````


## -struct-fields
<dl>

### -field dwBitMasks

<dd>
<p>Array of color masks (one per color element).</p>
</dd>

### -field bmiColors

<dd>
<p>Array of palette colors.</p>
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
<a href="stream.ks_rgbquad">KS_RGBQUAD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_TRUECOLORINFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
