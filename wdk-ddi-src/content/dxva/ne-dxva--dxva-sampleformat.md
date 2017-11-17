---
UID: NE.dxva._DXVA_SampleFormat
title: DXVA_SampleFormat
author: windows-driver-content
description: The DXVA_SampleFormat enumeration type describes the format of data that the input sample contains.
old-location: display\dxva_sampleformat.htm
ms.assetid: 90cec61b-fe49-4fc7-b666-e74f745a00b1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_SampleFormat
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
ms.keywords: DXGIDDICB_PRESENT, DXGIDDICB_PRESENT
req.iface: 
---

# DXVA_SampleFormat enumeration



## -description
<p>The DXVA_SampleFormat enumeration type describes the format of data that the input sample contains.</p>


## -syntax

````
typedef enum _DXVA_SampleFormat { 
  DXVA_SampleFormatMask                 = 0xFF,
  DXVA_SampleUnknown                    = 0,
  DXVA_SamplePreviousFrame              = 1,
  DXVA_SampleProgressiveFrame           = 2,
  DXVA_SampleFieldInterleavedEvenFirst  = 3,
  DXVA_SampleFieldInterleavedOddFirst   = 4,
  DXVA_SampleFieldSingleEven            = 5,
  DXVA_SampleFieldSingleOdd             = 6,
  DXVA_SampleSubStream                  = 7
} DXVA_SampleFormat;
````


## -enum-fields
<dl>

### -field <a id="DXVA_SampleFormatMask"></a><a id="dxva_sampleformatmask"></a><a id="DXVA_SAMPLEFORMATMASK"></a><b>DXVA_SampleFormatMask</b>

<dd>
<p>Specifies the sample format mask. The first 8 (0x000000FF) bits of a DWORD can be used to specify input sample format. 
</p>
</dd>

### -field <a id="DXVA_SampleUnknown"></a><a id="dxva_sampleunknown"></a><a id="DXVA_SAMPLEUNKNOWN"></a><b>DXVA_SampleUnknown</b>

<dd>
<p>Specifies that the sample format is unknown. 
</p>
</dd>

### -field <a id="DXVA_SamplePreviousFrame"></a><a id="dxva_samplepreviousframe"></a><a id="DXVA_SAMPLEPREVIOUSFRAME"></a><b>DXVA_SamplePreviousFrame</b>

<dd>
<p>Specifies that the sample contains the previous output frame.</p>
</dd>

### -field <a id="DXVA_SampleProgressiveFrame"></a><a id="dxva_sampleprogressiveframe"></a><a id="DXVA_SAMPLEPROGRESSIVEFRAME"></a><b>DXVA_SampleProgressiveFrame</b>

<dd>
<p>Specifies that the sample contains a progressive frame.</p>
</dd>

### -field <a id="DXVA_SampleFieldInterleavedEvenFirst"></a><a id="dxva_samplefieldinterleavedevenfirst"></a><a id="DXVA_SAMPLEFIELDINTERLEAVEDEVENFIRST"></a><b>DXVA_SampleFieldInterleavedEvenFirst</b>

<dd>
<p>Specifies that the sample contains two interleaved fields; the even field is temporally first.</p>
</dd>

### -field <a id="DXVA_SampleFieldInterleavedOddFirst"></a><a id="dxva_samplefieldinterleavedoddfirst"></a><a id="DXVA_SAMPLEFIELDINTERLEAVEDODDFIRST"></a><b>DXVA_SampleFieldInterleavedOddFirst</b>

<dd>
<p>Specifies that the sample contains two interleaved fields; the odd field is temporally first.</p>
</dd>

### -field <a id="DXVA_SampleFieldSingleEven"></a><a id="dxva_samplefieldsingleeven"></a><a id="DXVA_SAMPLEFIELDSINGLEEVEN"></a><b>DXVA_SampleFieldSingleEven</b>

<dd>
<p>Specifies that the sample contains an even interleaved field.</p>
</dd>

### -field <a id="DXVA_SampleFieldSingleOdd"></a><a id="dxva_samplefieldsingleodd"></a><a id="DXVA_SAMPLEFIELDSINGLEODD"></a><b>DXVA_SampleFieldSingleOdd</b>

<dd>
<p>Specifies that the sample contains an odd interleaved field.</p>
</dd>

### -field <a id="DXVA_SampleSubStream"></a><a id="dxva_samplesubstream"></a><a id="DXVA_SAMPLESUBSTREAM"></a><b>DXVA_SampleSubStream</b>

<dd>
<p>Windows Server 2003 SP1 and later and Windows XP SP2 and later versions only.</p>
<p>Specifies that the sample contains a video substream.</p>
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
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564085">DXVA_VideoSample</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564092">DXVA_VideoSample2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_SampleFormat enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
