---
UID: NE.dxva._DXVA_SampleFlags
title: DXVA_SampleFlags
author: windows-driver-content
description: The DXVA_SampleFlags enumeration type contains a collection of flags that identify changes in the current sample frame from the previous sample frame.
old-location: display\dxva_sampleflags.htm
old-project: display
ms.assetid: 24f77f16-e043-4d58-87ef-6c834e61cb5d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_GAMMA_CONTROL_CAPABILITIES, DXGI_GAMMA_CONTROL_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_SampleFlags
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
req.iface: 
---

# DXVA_SampleFlags enumeration



## -description
<p>The DXVA_SampleFlags enumeration type contains a collection of flags that identify changes in the current sample frame from the previous sample frame.</p>


## -syntax

````
typedef enum _DXVA_SampleFlags { 
  DXVA_SampleFlagsMask               = DXVABit(3)|DXVABit(2)|DXVABit(1)|DXVABit(0),
  DXVA_SampleFlag_Palette_Changed    = 0x0001,
  DXVA_SampleFlag_SrcRect_Changed    = 0x0002,
  DXVA_SampleFlag_DstRect_Changed    = 0x0004,
  DXVA_SampleFlag_ColorData_Changed  = 0x0008
} DXVA_SampleFlags;
````


## -enum-fields
<dl>

### -field DXVA_SampleFlagsMask

<dd>
<p>Specifies the sample-flag mask, which consists of the first 4 bits of a DWORD. </p>
</dd>

### -field DXVA_SampleFlag_Palette_Changed

<dd>
<p>Indicates that the palette of the sample frame changed. </p>
</dd>

### -field DXVA_SampleFlag_SrcRect_Changed

<dd>
<p>Indicates that the source rectangle of the sample frame changed. </p>
</dd>

### -field DXVA_SampleFlag_DstRect_Changed

<dd>
<p>Indicates that the destination rectangle of the sample frame changed. </p>
</dd>

### -field DXVA_SampleFlag_ColorData_Changed

<dd>
<p>Indicates that the color data of the sample frame changed.</p>
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
<p>This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p>
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
<a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DXVA_DeinterlaceBobDeviceClass::DeinterlaceBltEx</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-deinterlacebltex.md">DXVA_DeinterlaceBltEx</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-videosample2.md">DXVA_VideoSample2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_SampleFlags enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
