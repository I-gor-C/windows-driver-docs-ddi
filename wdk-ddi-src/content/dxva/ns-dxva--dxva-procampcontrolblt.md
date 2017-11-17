---
UID: NS.dxva._DXVA_ProcAmpControlBlt
title: DXVA_ProcAmpControlBlt
author: windows-driver-content
description: The DXVA_ProcAmpControlBlt structure contains the ProcAmp adjustment data that is output to the destination surface.
old-location: display\dxva_procampcontrolblt.htm
ms.assetid: 93f321e1-a38b-43a2-bfbd-35411a62194e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: DirectX 9.0 and later versions only.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_ProcAmpControlBlt
req.alt-loc: dxva.h
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
ms.keywords: DXVA_ProcAmpControlBlt, DXVA_ProcAmpControlBlt
req.iface: 
---

# DXVA_ProcAmpControlBlt structure



## -description
<p>The DXVA_ProcAmpControlBlt structure contains the ProcAmp adjustment data that is output to the destination surface.</p>


## -syntax

````
typedef struct _DXVA_ProcAmpControlBlt {
  DWORD Size;
  RECT  DstRect;
  RECT  SrcRect;
  FLOAT Alpha;
  FLOAT Brightness;
  FLOAT Contrast;
  FLOAT Hue;
  FLOAT Saturation;
} DXVA_ProcAmpControlBlt;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size of this structure in bytes.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>Specifies the destination rectangle as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure. The destination rectangle is required for subrectangle stretching. Support for stretching is optional and is reported by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564019">DXVA_ProcAmpControlCaps</a> structure. Support for subrectangles is optional.</p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>Specifies the source rectangle as a RECT structure. The source rectangle is required for subrectangle stretching.sub Support for stretching is optional and is reported by the DXVA_ProcAmpControlCaps structure. Support for subrectangles is also optional.</p>
</dd>

### -field <b>Alpha</b>

<dd>
<p>Specifies the transparency of the output image as it is written to the destination surface. A value of 0.0F indicates transparent. A value of 1.0F indicates opaque.</p>
</dd>

### -field <b>Brightness</b>

<dd>
<p>Specifies the brightness of the output image as it is written to the destination surface.</p>
</dd>

### -field <b>Contrast</b>

<dd>
<p>Specifies the contrast of the output image as it is written to the destination surface.</p>
</dd>

### -field <b>Hue</b>

<dd>
<p>Specifies the hue of the output image as it is written to the destination surface.</p>
</dd>

### -field <b>Saturation</b>

<dd>
<p>Specifies the saturation of the output image as it is written to the destination surface.</p>
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
<p>DirectX 9.0 and later versions only.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564019">DXVA_ProcAmpControlCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564032">DXVA_ProcAmpControlQueryRange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_ProcAmpControlBlt structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
