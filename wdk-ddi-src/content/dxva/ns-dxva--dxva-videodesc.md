---
UID: NS.dxva._DXVA_VideoDesc
title: DXVA_VideoDesc
author: windows-driver-content
description: The DXVA_VideoDesc structure is sent by the renderer to the driver to specify a description of the video stream on which the deinterlacing or frame-rate conversion operation is to be performed.
old-location: display\dxva_videodesc.htm
ms.assetid: 5623ed85-e78a-48f2-ab21-e6364da86b2a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_VideoDesc
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
ms.keywords: DXVA_VideoDesc, DXVA_VideoDesc, *LPDXVA_VideoDesc
req.iface: 
---

# DXVA_VideoDesc structure



## -description
<p>The DXVA_VideoDesc structure is sent by the renderer to the driver to specify a description of the video stream on which the deinterlacing or frame-rate conversion operation is to be performed.</p>


## -syntax

````
typedef struct _DXVA_VideoDesc {
  DWORD          Size;
  DWORD          SampleWidth;
  DWORD          SampleHeight;
  DWORD          SampleFormat;
  D3DFORMAT      d3dFormat;
  DXVA_Frequency InputSampleFreq;
  DXVA_Frequency OutputFrameFreq;
} DXVA_VideoDesc, *LPDXVA_VideoDesc;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size of this structure, in bytes.</p>
</dd>

### -field <b>SampleWidth</b>

<dd>
<p>Specifies the width of the sample, in pixels.</p>
</dd>

### -field <b>SampleHeight</b>

<dd>
<p>Specifies the height of the sample, in pixels.</p>
</dd>

### -field <b>SampleFormat</b>

<dd>
<p>Specifies the format of the sample defined by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564045">DXVA_SampleFormat</a> structure.</p>
</dd>

### -field <b>d3dFormat</b>

<dd>
<p>Specifies the Direct3D surface format of the sample.</p>
</dd>

### -field <b>InputSampleFreq</b>

<dd>
<p>Specifies the frequency of incoming video defined by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563969">DXVA_Frequency</a> structure.</p>
</dd>

### -field <b>OutputFrameFreq</b>

<dd>
<p>Specifies the desired frame rate of output video as defined by <a href="https://msdn.microsoft.com/library/windows/hardware/ff563969">DXVA_Frequency</a>.</p>
</dd>
</dl>

## -remarks
<p>For examples showing structure member values for deinterlacing or converting different types of content, see <a href="https://msdn.microsoft.com/be721bde-3c72-4942-9f33-5ea1bf2d187c">DeinterlaceQueryAvailableModes</a>.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564045">DXVA_SampleFormat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563969">DXVA_Frequency</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_VideoDesc structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
