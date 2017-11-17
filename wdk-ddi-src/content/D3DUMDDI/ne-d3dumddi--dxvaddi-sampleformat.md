---
UID: NE.d3dumddi._DXVADDI_SAMPLEFORMAT
title: DXVADDI_SAMPLEFORMAT
author: windows-driver-content
description: The DXVADDI_SAMPLEFORMAT enumeration type contains values that identify how a video frame is sampled.
old-location: display\dxvaddi_sampleformat.htm
ms.assetid: 23482cdc-6412-4309-805e-a439d8e81b59
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_SAMPLEFORMAT
req.alt-loc: d3dumddi.h
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# DXVADDI_SAMPLEFORMAT enumeration



## -description
<p>The DXVADDI_SAMPLEFORMAT enumeration type contains values that identify how a video frame is sampled.</p>


## -syntax

````
typedef enum _DXVADDI_SAMPLEFORMAT { 
  DXVADDI_SampleFormatMask                 = 0x00FF,
  DXVADDI_SampleUnknown                    = 0,
  DXVADDI_SampleProgressiveFrame           = 2,
  DXVADDI_SampleFieldInterleavedEvenFirst  = 3,
  DXVADDI_SampleFieldInterleavedOddFirst   = 4,
  DXVADDI_SampleFieldSingleEven            = 5,
  DXVADDI_SampleFieldSingleOdd             = 6,
  DXVADDI_SampleSubStream                  = 7
} DXVADDI_SAMPLEFORMAT;
````


## -enum-fields
<dl>

### -field <a id="DXVADDI_SampleFormatMask"></a><a id="dxvaddi_sampleformatmask"></a><a id="DXVADDI_SAMPLEFORMATMASK"></a><b>DXVADDI_SampleFormatMask</b>

<dd>
<p>The sample format mask. The first 8 (0xFF) bits of a DWORD can be used to specify input sample format.</p>
</dd>

### -field <a id="DXVADDI_SampleUnknown"></a><a id="dxvaddi_sampleunknown"></a><a id="DXVADDI_SAMPLEUNKNOWN"></a><b>DXVADDI_SampleUnknown</b>

<dd>
<p>The sample format is unknown.</p>
</dd>

### -field <a id="DXVADDI_SampleProgressiveFrame"></a><a id="dxvaddi_sampleprogressiveframe"></a><a id="DXVADDI_SAMPLEPROGRESSIVEFRAME"></a><b>DXVADDI_SampleProgressiveFrame</b>

<dd>
<p>The sample contains a progressive frame.</p>
</dd>

### -field <a id="DXVADDI_SampleFieldInterleavedEvenFirst"></a><a id="dxvaddi_samplefieldinterleavedevenfirst"></a><a id="DXVADDI_SAMPLEFIELDINTERLEAVEDEVENFIRST"></a><b>DXVADDI_SampleFieldInterleavedEvenFirst</b>

<dd>
<p>The sample contains two interleaved fields; the even field is temporally first.</p>
</dd>

### -field <a id="DXVADDI_SampleFieldInterleavedOddFirst"></a><a id="dxvaddi_samplefieldinterleavedoddfirst"></a><a id="DXVADDI_SAMPLEFIELDINTERLEAVEDODDFIRST"></a><b>DXVADDI_SampleFieldInterleavedOddFirst</b>

<dd>
<p>The sample contains two interleaved fields; the odd field is temporally first.</p>
</dd>

### -field <a id="DXVADDI_SampleFieldSingleEven"></a><a id="dxvaddi_samplefieldsingleeven"></a><a id="DXVADDI_SAMPLEFIELDSINGLEEVEN"></a><b>DXVADDI_SampleFieldSingleEven</b>

<dd>
<p>The sample contains an even interleaved field.</p>
</dd>

### -field <a id="DXVADDI_SampleFieldSingleOdd"></a><a id="dxvaddi_samplefieldsingleodd"></a><a id="DXVADDI_SAMPLEFIELDSINGLEODD"></a><b>DXVADDI_SampleFieldSingleOdd</b>

<dd>
<p>The sample contains an odd interleaved field.</p>
</dd>

### -field <a id="DXVADDI_SampleSubStream"></a><a id="dxvaddi_samplesubstream"></a><a id="DXVADDI_SAMPLESUBSTREAM"></a><b>DXVADDI_SampleSubStream</b>

<dd>
<p>The sample contains a video substream.</p>
</dd>
</dl>

## -remarks
<p>One of the values of DXVADDI_SAMPLEFORMAT can be specified in the <b>SampleFormat</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>One of the values of DXVADDI_SAMPLEFORMAT can be specified in the <b>SampleFormat</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>One of the values of DXVADDI_SAMPLEFORMAT can be specified in the <b>SampleFormat</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_SAMPLEFORMAT enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
