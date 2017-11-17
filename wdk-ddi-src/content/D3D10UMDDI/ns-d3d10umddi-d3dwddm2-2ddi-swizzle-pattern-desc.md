---
UID: NS.d3d10umddi.D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
title: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
author: windows-driver-content
description: Describes a swizzle pattern.
old-location: display\d3dwddm2_2ddi_swizzle_pattern_desc.htm
ms.assetid: AD3D5847-862F-41AA-90C0-0F8A1D0A617B
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.alt-loc: d3d10umddi.h
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC structure



## -description
<p>Describes a swizzle pattern. </p>


## -syntax

````
typedef struct D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC {
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternSourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXORSourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR2SourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR3SourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR4SourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY PostambleXORSourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY PostambleXOR2SourceBits[32];
  UINT                            PostambleXORImmediate;
  UINT                            Flags;
} D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC;
````


## -struct-fields
<dl>

### -field <b>InterleavePatternSourceBits</b>

<dd>
<p>The interleave pattern source bits.</p>
</dd>

### -field <b>InterleavePatternXORSourceBits</b>

<dd>
<p>The interleave pattern XOR source bits.</p>
</dd>

### -field <b>InterleavePatternXOR2SourceBits</b>

<dd>
<p>The interleave pattern second XOR source bits.</p>
</dd>

### -field <b>InterleavePatternXOR3SourceBits</b>

<dd>
<p>The interleave pattern third XOR source bits.</p>
</dd>

### -field <b>InterleavePatternXOR4SourceBits</b>

<dd>
<p>The interleave pattern fourth XOR source bits.</p>
</dd>

### -field <b>PostambleXORSourceBits</b>

<dd>
<p>Postamble XOR source bits.</p>
</dd>

### -field <b>PostambleXOR2SourceBits</b>

<dd>
<p>Postamble second XOR source bits.</p>
</dd>

### -field <b>PostambleXORImmediate</b>

<dd>
<p>A postamble XOR immediate value. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags. For more information, see the <a href="https://msdn.microsoft.com/4C3E818B-E265-4AB8-BAAF-D3155578E558">D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS</a> enumeration. </p>
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
<dt>D3d10umddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/4C3E818B-E265-4AB8-BAAF-D3155578E558">D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
