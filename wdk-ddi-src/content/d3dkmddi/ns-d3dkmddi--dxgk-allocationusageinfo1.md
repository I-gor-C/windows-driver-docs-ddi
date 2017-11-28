---
UID: NS.d3dkmddi._DXGK_ALLOCATIONUSAGEINFO1
title: DXGK_ALLOCATIONUSAGEINFO1
author: windows-driver-content
description: The DXGK_ALLOCATIONUSAGEINFO1 structure describes how an allocation can be used in DMA buffering.
old-location: display\dxgk_allocationusageinfo1.htm
old-project: display
ms.assetid: 6de3363c-fcf8-4350-acee-b401bb3f82a6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_ALLOCATIONUSAGEINFO1, DXGK_ALLOCATIONUSAGEINFO1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_ALLOCATIONUSAGEINFO1
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_ALLOCATIONUSAGEINFO1 structure



## -description
<p>The DXGK_ALLOCATIONUSAGEINFO1 structure describes how an allocation can be used in DMA buffering.</p>


## -syntax

````
typedef struct _DXGK_ALLOCATIONUSAGEINFO1 {
  union {
    struct {
      UINT PrivateFormat  :1;
      UINT Swizzled  :1;
      UINT MipMap  :1;
      UINT Cube  :1;
      UINT Volume  :1;
      UINT Vertex  :1;
      UINT Index  :1;
      UINT Reserved  :25;
    };
    UINT Value;
  } Flags;
  union {
    D3DDDIFORMAT Format;
    UINT         PrivateFormat;
  };
  UINT SwizzledFormat;
  UINT ByteOffset;
  UINT Width;
  UINT Height;
  UINT Pitch;
  UINT Depth;
  UINT SlicePitch;
} DXGK_ALLOCATIONUSAGEINFO1;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>[out] A union that contains either a structure (with the first eight members that are described below) or a 32-bit value (in the <b>Value</b> member) that identifies how the allocation is used:</p>
<dl>

### -field <b>PrivateFormat</b>

<dd>
<p>A UINT value that specifies whether the allocation is a private vendor format.  </p>
<p>Setting this is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Swizzled</b>

<dd>
<p>A UINT value that specifies whether the allocation is swizzled or tiled. </p>
<p>Setting this is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>MipMap</b>

<dd>
<p>A UINT value that specifies whether the allocation is a MIP-mapped texture.</p>
<p>Setting this is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>Cube</b>

<dd>
<p>A UINT value that specifies whether the allocation is a cube texture. </p>
<p>Setting this is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x00000008).</p>
</dd>

### -field <b>Volume</b>

<dd>
<p>A UINT value that specifies whether the allocation is a volume texture.</p>
<p>Setting this is equivalent to setting the fifth bit of the 32-bit <b>Value</b> member (0x00000010).</p>
</dd>

### -field <b>Vertex</b>

<dd>
<p>A UINT value that specifies whether the allocation is a vertex buffer.</p>
<p>Setting this is equivalent to setting the sixth bit of the 32-bit <b>Value</b> member (0x00000020).</p>
</dd>

### -field <b>Index</b>

<dd>
<p>A UINT value that specifies whether the allocation is an index buffer.</p>
<p>Setting this is equivalent to setting the seventh bit of the 32-bit <b>Value</b> member (0x00000040).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this to zero is equivalent to setting the remaining 25 bits (0xFFFFFF80) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Specifies a member in the union contained in the <b>Flags</b> member that can hold one 32-bit value that identifies how the allocation is used.</p>
</dd>
</dl>
</dd>

### -field <b>Format</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the allocation. The <b>PrivateFormat</b> bit-field flag in the <b>Flags</b> member must be set to 0 (FALSE).</p>
</dd>

### -field <b>PrivateFormat</b>

<dd>
<p>[out] A private format value for the allocation. The <b>PrivateFormat</b> bit-field flag in the <b>Flags</b> member must be set to 1 (TRUE).</p>
</dd>

### -field <b>SwizzledFormat</b>

<dd>
<p>[out] A swizzled format value for the allocation that is private to a specific vendor.</p>
</dd>

### -field <b>ByteOffset</b>

<dd>
<p>[out] The offset, in bytes, into the video memory manager's allocation that marks the start of the driver's version of the allocation.</p>
</dd>

### -field <b>Width</b>

<dd>
<p>[out] The width, in pixels, of the allocation.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>[out] The height, in number of lines, of the allocation.</p>
</dd>

### -field <b>Pitch</b>

<dd>
<p>[out] The pitch, in bytes, of the allocation--that is, the distance, in bytes, to the start of the next line.</p>
</dd>

### -field <b>Depth</b>

<dd>
<p>[out] The depth, in levels, of the allocation (for MIP-mapped and volume textures only).</p>
</dd>

### -field <b>SlicePitch</b>

<dd>
<p>[out] The slice pitch, in bytes, from level to level (for cube and volume textures only).</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560981">DXGK_ALLOCATIONUSAGEHINT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_ALLOCATIONUSAGEINFO1 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
