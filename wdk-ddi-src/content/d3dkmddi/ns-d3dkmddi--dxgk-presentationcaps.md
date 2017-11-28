---
UID: NS.d3dkmddi._DXGK_PRESENTATIONCAPS
title: DXGK_PRESENTATIONCAPS
author: windows-driver-content
description: The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_presentationcaps.htm
old-project: display
ms.assetid: 38de4631-535f-4950-b361-d70f8c638c36
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PRESENTATIONCAPS, DXGK_PRESENTATIONCAPS
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
req.alt-api: DXGK_PRESENTATIONCAPS
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

# DXGK_PRESENTATIONCAPS structure



## -description
<p>The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function.</p>


## -syntax

````
typedef struct _DXGK_PRESENTATIONCAPS {
  union {
    struct {
      UINT NoScreenToScreenBlt  :1;
      UINT NoOverlapScreenBlt  :1;
      UINT SupportKernelModeCommandBuffer  :1;
      UINT NoSameBitmapAlphaBlend  :1;
      UINT NoSameBitmapStretchBlt  :1;
      UINT NoSameBitmapTransparentBlt  :1;
      UINT NoSameBitmapOverlappedAlphaBlend  :1;
      UINT NoSameBitmapOverlappedStretchBlt  :1;
      UINT DriverSupportsCddDwmInterop  :1;
      UINT Reserved0  :1;
      UINT AlignmentShift  :4;
      UINT MaxTextureWidthShift  :3;
      UINT MaxTextureHeightShift  :3;
      UINT SupportAllBltRops  :1;
      UINT SupportMirrorStretchBlt  :1;
      UINT SupportMonoStretchBltModes  :1;
      UINT StagingRectStartPitchAligned  :1;
      UINT NoSameBitmapBitBlt  :1;
      UINT NoSameBitmapOverlappedBitBlt  :1;
      UINT Reserved1  :1;
      UINT NoTempSurfaceForClearTypeBlend  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT SupportSoftwareDeviceBitmaps  :1;
      UINT NoCacheCoherentApertureMemory  :1;
      UINT SupportLinearHeap  :1;
      UINT Reserved  :1;
#else 
      UINT Reserved  :4;
#endif 
    };
     Value;
  };
} DXGK_PRESENTATIONCAPS;
````


## -struct-fields
<dl>

### -field <b>NoScreenToScreenBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a bit-block transfer (bitblt) from the primary surface to the same primary surface. If <b>NoScreenToScreenBlt</b> is set, the driver cannot perform a screen-to-screen bit-block transfer. Therefore, the Microsoft DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) will not request the driver to perform such a bit-block transfer.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>NoOverlapScreenBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a bit-block transfer that overlaps. If <b>NoOverlapScreenBlt</b> is set, the driver cannot perform a bit-block transfer that overlaps. Therefore, the DirectX graphics kernel subsystem will not request the driver to perform such a bit-block transfer.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>SupportKernelModeCommandBuffer</b>

<dd>
<p> [in] A UINT value that specifies whether the display miniport driver supports GDI hardware-accelerated command buffer processing. If <b>SupportKernelModeCommandBuffer</b> is set, the driver can perform various hardware-accelerated bit-block transfer (bitblt) and fill operations when the DirectX graphics kernel subsystem calls the display miniport driver's <a href="display.dxgkddirenderkm">DxgkDdiRenderKm</a> function.</p>
<div class="alert"><b>Note</b>    A display miniport driver should report that it supports GDI hardware acceleration only if the cache-coherent GPU aperture segment exists and there is no significant performance penalty when the CPU accesses the memory.</div>
<div> </div>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapAlphaBlend</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform an alpha-blending operation when the source and destination allocations are the same. If <b>NoSameBitmapAlphaBlend</b> is set, the driver cannot perform such an operation and the DirectX graphics kernel subsystem will not request it.</p>
<p>Setting this member is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x00000008). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapStretchBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a stretch bit-block transfer operation when the source and destination allocations are the same. If <b>NoSameBitmapStretchBlt</b> is set, the driver cannot perform such an operation and the DirectX graphics kernel subsystem will not request it.</p>
<p>Setting this member is equivalent to setting the fifth bit of the 32-bit <b>Value</b> member (0x00000010). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapTransparentBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a transparent bit-block transfer operation when the source and destination allocations are the same. If <b>NoSameBitmapStretchBlt</b> is set, the driver cannot perform such an operation and the DirectX graphics kernel subsystem will not request it.</p>
<p>Setting this member is equivalent to setting the sixth bit of the 32-bit <b>Value</b> member (0x00000020). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapOverlappedAlphaBlend</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform an alpha-blending operation when the source and destination allocations are the same and source and destination rectangles overlap. If <b>NoSameBitmapOverlappedAlphaBlend</b> is set, the driver cannot perform such an operation and the DirectX graphics kernel subsystem will not request it.</p>
<p>Setting this member is equivalent to setting the seventh bit of the 32-bit <b>Value</b> member (0x00000040). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapOverlappedStretchBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a stretch bit-block transfer operation when the source and destination allocations are the same and source and destination rectangles overlap. If <b>NoSameBitmapOverlappedStretchBlt</b> is set, the driver cannot perform such an operation and the DirectX graphics kernel subsystem will not request it.</p>
<p>Setting this member is equivalent to setting the eight bit of the 32-bit <b>Value</b> member (0x00000080). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>DriverSupportsCddDwmInterop</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver supports Canonical Display Driver (CDD) present operations to texture allocations that are created by the user-mode driver for the Desktop Windows Manager (DWM) to use. If <b>DriverSupportsCddDwmInterop</b> is set, the display miniport driver supports such present operations.</p>
<p>If the display miniport driver supports GDI hardware acceleration, <b>DriverSupportsCddDwmInterop</b> is ignored. In this case the driver must support present CDD operations to DWM texture allocations that are created by the user-mode driver.</p>
<p>Setting this member is equivalent to setting the ninth bit of the 32-bit <b>Value</b> member (0x00000100). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
<p>Setting this member is equivalent to setting the tenth bit of the 32-bit <b>Value</b> member (0x00000200). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>AlignmentShift</b>

<dd>
<p>[in] A UINT value that specifies the minimum alignment value, in bytes, that the <b>XxxPitch</b> members of the DXGK_GDIARG_XXX structures require. <b>AlignmentShift</b> is given as a binary exponent. For example, to specify a required alignment value of 16 bytes, the display miniport driver should set <b>AlignmentShift</b> = 4. The minimum value is <b>AlignmentShift</b> = 2, which specifies a 4-byte alignment.</p>
<p>Setting this member is equivalent to setting the eleventh bit of the 32-bit <b>Value</b> member (0x00000400). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>MaxTextureWidthShift</b>

<dd>
<p>[in] A UINT value that specifies the maximum texture width that the display miniport driver supports, which is computed as:</p>
<p>maximum supported texture width = 2 ^ (<b>MaxTextureWidthShift</b> + 11) texels.</p>
<p>For example, if <b>MaxTextureWidthShift</b> = 0, the maximum supported texture width is 2 ^ 11 = 2048.</p>
<p>Setting this member is equivalent to setting the twelfth bit of the 32-bit <b>Value</b> member (0x00000800). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>MaxTextureHeightShift</b>

<dd>
<p>[in] A UINT value that specifies the maximum texture height that the display miniport driver supports, which is computed as:</p>
<p>maximum supported texture height = 2 ^ (<b>MaxTextureHeightShift</b> + 11) texels.</p>
<p>For example, if <b>MaxTextureHeightShift</b> = 0, the maximum supported texture height is 2 ^ 11 = 2048.</p>
<p>Setting this member is equivalent to setting the thirteenth bit of the 32-bit <b>Value</b> member (0x00001000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>SupportAllBltRops</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver supports all GDI ROP3 raster operations with solid color as a pattern in BitBlt and ColorFill commands. If <b>SupportAllBltRops</b> is set, the driver supports such raster operations.</p>
<p>Setting this member is equivalent to setting the fourteenth bit of the 32-bit <b>Value</b> member (0x00002000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>SupportMirrorStretchBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver supports Stretch Blt operations (using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561089">DXGK_GDIARG_STRETCHBLT</a> structure) in mirror mode. If <b>SupportMirrorStretchBlt </b>is set, the driver supports such operations.</p>
<p>Setting this member is equivalent to setting the fifteenth bit of the 32-bit <b>Value</b> member (0x00004000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>SupportMonoStretchBltModes</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver supports Stretch Blt operations (using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561089">DXGK_GDIARG_STRETCHBLT</a> structure) in BLACKONWHITE or WHITEONBLACK monochromatic rendering modes. If <b>SupportMonoStretchBltModes</b> is set, the driver supports such operations.</p>
<p>Setting this member is equivalent to setting the sixteenth bit of the 32-bit <b>Value</b> member (0x00008000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>StagingRectStartPitchAligned</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver requires the starting point (upper-left point) in the rectangle on a CPU-visible staging surface to be pitch-aligned, which means that the left coordinate is 0. If <b>AlignmentShift</b> is set, the upper-left point of the rectangle is pitch-aligned.</p>
<p>Setting this member is equivalent to setting the seventeenth bit of the 32-bit <b>Value</b> member (0x00010000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapBitBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a bit-block transfer operation when the source and destination allocations are the same. If <b>NoSameBitmapBitBlt</b> is set, the driver cannot perform such an operation. Therefore, the DirectX graphics kernel subsystem will not request that the driver perform such an operation.</p>
<p>Setting this member is equivalent to setting the eighteenth bit of the 32-bit <b>Value</b> member (0x00020000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoSameBitmapOverlappedBitBlt</b>

<dd>
<p>[in] A UINT value that specifies whether the display miniport driver can perform a bit-block transfer operation when the source and destination allocations are the same and source and destination rectangles overlap. If <b>NoSameBitmapOverlappedBitBlt</b> is set, the driver cannot perform such an operation and the DirectX graphics kernel subsystem will not request it.</p>
<p>Setting this member is equivalent to setting the nineteenth bit of the 32-bit <b>Value</b> member (0x00040000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>[in] This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the twentieth bit of the 32-bit <b>Value</b> member (0x00080000). </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NoTempSurfaceForClearTypeBlend</b>

<dd>
<p>[in] A UINT value that specifies whether the driver needs a temporary surface during processing of commands that are specified by the <b>ClearTypeBlend</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562026">DXGK_RENDERKM_COMMAND</a> structure. If <b>NoTempSurfaceForClearTypeBlend</b> is set, the driver does not need a temporary surface. In this case, the driver will use less video memory.</p>
<p>Setting this member to zero is equivalent to setting the twenty-first bit of the 32-bit <b>Value</b> member (0x00100000).</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>SupportSoftwareDeviceBitmaps</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
<p>Setting this member is equivalent to setting the twenty-second bit of the 32-bit <b>Value</b> member (0x00200000).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>NoCacheCoherentApertureMemory</b>

<dd>
<p>[in] </p>
<p>A UINT value that specifies that the driver does not support cache-coherent aperture memory.</p>
<p>Setting this member is equivalent to setting the twenty-third bit of the 32-bit <b>Value</b> member (0x00400000).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportLinearHeap</b>

<dd>
<p>[in] The driver supports linear heap allocation from staging surfaces. </p>
<p>Setting this member is equivalent to setting the twenty-fourth bit of the 32-bit <b>Value</b> member (0x00800000).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
<p>Setting this member is equivalent to setting the twenty-fifth bit of the 32-bit <b>Value</b> member (0x01000000).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
<p>Setting this member is equivalent to setting the twenty-fifth bit of the 32-bit <b>Value</b> member (0x02000000).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that identifies the driver's presentation capabilities.</p>
</dd>
</dl>

## -remarks
<p>A display miniport driver can specify presentation capabilities by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_PRESENTATIONCAPS contains.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546039">D3DKMDT_GDISURFACETYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a>
</dt>
<dt>
<a href="display.dxgkddirenderkm">DxgkDdiRenderKm</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_PRESENTATIONCAPS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
