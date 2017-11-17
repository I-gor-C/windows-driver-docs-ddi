---
UID: NS.d3dumddi._D3DDDI_BLTFLAGS
title: D3DDDI_BLTFLAGS
author: windows-driver-content
description: The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform.
old-location: display\d3dddi_bltflags.htm
ms.assetid: 844d6aed-2ca2-45ef-bd53-54344dbdadbf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_BLTFLAGS
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
ms.keywords: D3DDDI_BLTFLAGS, D3DDDI_BLTFLAGS
req.iface: 
---

# D3DDDI_BLTFLAGS structure



## -description
<p>The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform.</p>


## -syntax

````
typedef struct _D3DDDI_BLTFLAGS {
  union {
    struct {
      UINT Point  :1;
      UINT Linear  :1;
      UINT SrcColorKey  :1;
      UINT DstColorKey  :1;
      UINT MirrorLeftRight  :1;
      UINT MirrorUpDown  :1;
      UINT LinearToSrgb  :1;
      UINT Rotate  :1;
      UINT BeginPresentToDwm  :1;
      UINT ContinuePresentToDwm  :1;
      UINT EndPresentToDwm  :1;
#if (D3D_UMD_INTERFACE_VERSION < D3D_UMD_INTERFACE_VERSION_WIN8)
      UINT Reserved  :21;
#else 
      UINT Discard  :1;
      UINT NoOverwrite  :1;
      UINT Tileable  :1;
      UINT Reserved  :18;
#endif 
    };
    UINT Value;
  };
} D3DDDI_BLTFLAGS;
````


## -struct-fields
<dl>

### -field <b>Point</b>

<dd>
<p>A UINT value that specifies whether to use point filtering in the bit-block transfer. Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Linear</b>

<dd>
<p>A UINT value that specifies whether to use linear filtering in the bit-block transfer. Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>SrcColorKey</b>

<dd>
<p>A UINT value that specifies whether to perform source color-keying by using the value in the <b>ColorKey</b> member. That is, any pixel in the source surface that matches the color key should not be copied to the destination surface, and all of the source pixels that do not match the color key should be copied. </p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>DstColorKey</b>

<dd>
<p>A UINT value that specifies whether to perform destination color-keying by using the value in the <b>ColorKey</b> member. That is, any pixel in the destination surface that matches the color key should be replaced with the corresponding pixel from the source surface, and all of the destination pixels that do not match the color key should not be replaced.</p>
<p>Setting this member is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x00000008).</p>
</dd>

### -field <b>MirrorLeftRight</b>

<dd>
<p>A UINT value that specifies whether the contents of the source surface are flipped horizontally along the center axis in the bitblt to the destination surface. That is, contents on the left side of the source surface are copied to the right side of the destination surface, and vice versa.</p>
<p>Setting this member is equivalent to setting the fifth bit of the 32-bit <b>Value</b> member (0x00000010).</p>
</dd>

### -field <b>MirrorUpDown</b>

<dd>
<p>A UINT value that specifies whether the contents of the source surface are flipped vertically along the center axis in the bitblt to the destination surface. That is, the contents on the top of the source surface are copied to the bottom of the destination surface, and vice versa.</p>
<p>Setting this member is equivalent to setting the sixth bit of the 32-bit <b>Value</b> member (0x00000020).</p>
</dd>

### -field <b>LinearToSrgb</b>

<dd>
<p>A UINT value that specifies whether to convert the linear-formatted source to sRGB format during the bitblt operation. sRGB format is gamma corrected. For more information about sRGB format, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a> website.</p>
<p>Setting this member is equivalent to setting the seventh bit of the 32-bit <b>Value</b> member (0x00000040).</p>
</dd>

### -field <b>Rotate</b>

<dd>
<p>A UINT value that specifies whether to rotate the source during the bitblt operation. </p>
<p>Setting this member is equivalent to setting the eighth bit of the 32-bit <b>Value</b> member (0x00000080).</p>
</dd>

### -field <b>BeginPresentToDwm</b>

<dd>
<p>A UINT value that specifies whether the Microsoft Direct3D runtime begins a DWM present operation during the bitblt operation. For more information about <b>BeginPresentToDwm</b>, see Remarks.</p>
<p>Setting this member is equivalent to setting the ninth bit of the 32-bit <b>Value</b> member (0x00000100).</p>
</dd>

### -field <b>ContinuePresentToDwm</b>

<dd>
<p>A UINT value that specifies whether the Direct3D runtime continues a DWM present operation during the bitblt operation. For more information about <b>ContinuePresentToDwm</b>, see Remarks.</p>
<p>Setting this member is equivalent to setting the tenth bit of the 32-bit <b>Value</b> member (0x00000200).</p>
</dd>

### -field <b>EndPresentToDwm</b>

<dd>
<p>A UINT value that specifies whether the Direct3D runtime ends a DWM present operation during the bitblt operation. For more information about <b>EndPresentToDwm</b>, see Remarks.</p>
<p>Setting this member is equivalent to setting the eleventh bit of the 32-bit <b>Value</b> member (0x00000400).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 21 bits (0xFFFFF800) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Discard</b>

<dd>
<p>Indicates that the user-mode display driver can discard previous contents of the entire resource. The driver can take advantage of this capability to optimize performance and memory usage.</p>
<p>If this member is not <b>NULL</b>, <b>NoOverwrite</b> and  <b>Tileable</b> must be <b>NULL</b>.</p>
<p>Setting this member is equivalent to setting the twelfth bit (0xFFFFF800) of the 32-bit <b>Value</b> member to zeros.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>NoOverwrite</b>

<dd>
<p>Indicates that the caller guarantees that the portion of the surface that is being written to with new data is not currently being referenced or accessed by any previous render operation. The driver can take advantage of this capability to optimize performance and memory usage.</p>
<p>If this member is not <b>NULL</b>, <b>Discard</b> must be <b>NULL</b>.</p>
<p>Setting this member is equivalent to setting the thirteenth bit (0x00001000) of the 32-bit <b>Value</b> member to zeros.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Tileable</b>

<dd>
<p>For tile-based deferred rendering, indicates that a copy operation can operate on only the currently processed tile in the source or destination resource, and the scene does not have to be flushed in all tiles.</p>
<p>If this member is not <b>NULL</b>, <b>Discard</b> must be <b>NULL</b>.</p>
<p>Setting this member is equivalent to setting the fourteenth bit (0x00002000) of the 32-bit <b>Value</b> member to zeros.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. </p>
<p>Setting this member to zero is equivalent to setting the remaining 18 bits (0xFFFFC000) of the 32-bit <b>Value</b> member to zeros.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that is contained in D3DDDI_BLTFLAGS that can hold one 32-bit value that identifies the type of bitblt to perform.</p>
</dd>
</dl>

## -remarks
<p>The <b>BeginPresentToDwm</b>, <b>ContinuePresentToDwm</b>, and <b>EndPresentToDwm</b> bit-field flags inform the user-mode display driver about the time when the Direct3D runtime performs parts of a DWM present operation.  Because DWM present operations can occur in multiple steps, the Direct3D runtime uses these flags to mark the steps in a sequence of bitblts. For example:  </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_BLTFLAGS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
