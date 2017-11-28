---
UID: NS.ksmedia.PKSVPMAXPIXELRATE~r1
title: PKSVPMAXPIXELRATE
author: windows-driver-content
description: The KSVPMAXPIXELRATE structure is used to describe the maximum pixel rate of a video port.
old-location: stream\ksvpmaxpixelrate.htm
old-project: stream
ms.assetid: 6510e732-b0ad-43c7-87a3-3630fdfd848d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSVPMAXPIXELRATE, KSVPMAXPIXELRATE, *PKSVPMAXPIXELRATE
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
req.alt-api: KSVPMAXPIXELRATE
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

# PKSVPMAXPIXELRATE structure



## -description
<p>The KSVPMAXPIXELRATE structure is used to describe the maximum pixel rate of a video port.</p>


## -syntax

````
typedef struct {
  AMVPSIZE Size;
  DWORD    MaxPixelsPerSecond;
  DWORD    Reserved;
} KSVPMAXPIXELRATE, *PKSVPMAXPIXELRATE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the dimension (width by height) of the video port.</p>
</dd>

### -field <b>MaxPixelsPerSecond</b>

<dd>
<p>Indicates the maximum pixel throughput for the selected image size.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566494">KSPROPERTY_VPCONFIG_MAXPIXELRATE</a> property.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566494">KSPROPERTY_VPCONFIG_MAXPIXELRATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSVPMAXPIXELRATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
