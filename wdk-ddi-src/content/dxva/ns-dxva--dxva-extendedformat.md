---
UID: NS.dxva._DXVA_ExtendedFormat
title: DXVA_ExtendedFormat
author: windows-driver-content
description: The DXVA_ExtendedFormat structure describes the extended format of the video frame.
old-location: display\dxva_extendedformat.htm
ms.assetid: b4d01c1f-8267-490e-a808-87d9be666a94
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_ExtendedFormat
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
ms.keywords: DXVA_ExtendedFormat, DXVA_ExtendedFormat
req.iface: 
---

# DXVA_ExtendedFormat structure



## -description
<p>The DXVA_ExtendedFormat structure describes the extended format of the video frame. </p>


## -syntax

````
typedef struct _DXVA_ExtendedFormat {
  UINT                       SampleFormat  :8;
  UINT                       VideoChromaSubsampling  :4;
  DXVA_NominalRange          NominalRange  :3;
  DXVA_VideoTransferMatrix   VideoTransferMatrix  :3;
  DXVA_VideoLighting         VideoLighting  :4;
  DXVA_VideoPrimaries        VideoPrimaries  :5;
  DXVA_VideoTransferFunction VideoTransferFunction  :5;
} DXVA_ExtendedFormat;
````


## -struct-fields
<dl>

### -field <b>SampleFormat</b>

<dd>
<p>Specifies how a video frame is sampled. The 8 bits are defined by one of the enumerators in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564045">DXVA_SampleFormat</a> enumeration type.</p>
</dd>

### -field <b>VideoChromaSubsampling</b>

<dd>
<p>Specifies the chroma encoding scheme for Y'Cb'Cr' data. The 4 bits are defined by an ORed combination of the enumerators in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564067">DXVA_VideoChromaSubsampling</a> enumeration type. </p>
</dd>

### -field <b>NominalRange</b>

<dd>
<p>Specifies whether sample data includes headroom (values beyond 1.0 white) and toeroom (superblacks below the reference 0.0 black). The 3 bits are defined by one of the enumerators in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564006">DXVA_NominalRange</a> enumeration type. </p>
</dd>

### -field <b>VideoTransferMatrix</b>

<dd>
<p>Specifies the conversion matrix from Y'Cb'Cr' to (studio) R'G'B'. The 3 bits are defined by one of the enumerators in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564108">DXVA_VideoTransferMatrix</a> enumeration type. </p>
</dd>

### -field <b>VideoLighting</b>

<dd>
<p>Specifies lighting conditions for viewing video. The 4 bits are defined by one of the enumerators in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564071">DXVA_VideoLighting</a> enumeration type. </p>
</dd>

### -field <b>VideoPrimaries</b>

<dd>
<p>Specifies color primaries, which state which RGB basis functions are used. The 5 bits are defined by one of the enumerators in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564073">DXVA_VideoPrimaries</a> enumeration type. </p>
</dd>

### -field <b>VideoTransferFunction</b>

<dd>
<p>Specifies the conversion function from R'G'B' to RGB. The 5 bits are defined by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564105">DXVA_VideoTransferFunction</a> enumeration type. </p>
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
<p>This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564006">DXVA_NominalRange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564045">DXVA_SampleFormat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564067">DXVA_VideoChromaSubsampling</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564071">DXVA_VideoLighting</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564073">DXVA_VideoPrimaries</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564105">DXVA_VideoTransferFunction</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564108">DXVA_VideoTransferMatrix</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_ExtendedFormat structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
