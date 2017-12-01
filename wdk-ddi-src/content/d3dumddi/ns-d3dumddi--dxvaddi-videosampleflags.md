---
UID: NS.d3dumddi._DXVADDI_VIDEOSAMPLEFLAGS
title: DXVADDI_VIDEOSAMPLEFLAGS
author: windows-driver-content
description: The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame.
old-location: display\dxvaddi_videosampleflags.htm
old-project: display
ms.assetid: 1dca2b12-0542-43a9-abff-203ea34cff90
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_VIDEOSAMPLEFLAGS, DXVADDI_VIDEOSAMPLEFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEOSAMPLEFLAGS
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
req.iface: 
---

# DXVADDI_VIDEOSAMPLEFLAGS structure



## -description
<p>The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame.</p>


## -syntax

````
typedef struct _DXVADDI_VIDEOSAMPLEFLAGS {
  union {
    struct {
      UINT PaletteChanged  :1;
      UINT SrcRectChanged  :1;
      UINT DstRectChanged  :1;
      UINT ColorDataChanged  :1;
      UINT PlanarAlphaChanged  :1;
      UINT Reserved  :11;
      UINT SampleData  :16;
    };
    UINT   Value;
  };
} DXVADDI_VIDEOSAMPLEFLAGS;
````


## -struct-fields
<dl>

### -field <b>PaletteChanged</b>

<dd>
<p>A UINT value that specifies whether the palette of the sample frame changed. Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>SrcRectChanged</b>

<dd>
<p>A UINT value that specifies whether the source rectangle of the sample frame changed. Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>DstRectChanged</b>

<dd>
<p>A UINT value that specifies whether the destination rectangle of the sample frame changed. Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>ColorDataChanged</b>

<dd>
<p>A UINT value that specifies whether the color data of the sample frame changed. Setting this member is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x00000008).</p>
</dd>

### -field <b>PlanarAlphaChanged</b>

<dd>
<p>A UINT value that specifies whether the alpha (transparency) data of the sample frame changed. Setting this member is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x00000008).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the sixth through sixteenth bits (0x0000FFE0) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>SampleData</b>

<dd>
<p>A UINT value that contains video sample data. Setting this member is equivalent to setting the seventeenth through thirty-second bits (0xFFFF0000) of the 32-bit <b>Value</b> member. The following bits can be set:</p>
<p>DXVADDI_SAMPLEDATA_RFF (0x0001)</p>
<p>DXVADDI_SAMPLEDATA_TFF (0x0002)</p>
<p>DXVADDI_SAMPLEDATA_RFF_TFF_PRESENT (0x0004) </p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that is contained in DXVADDI_VIDEOSAMPLEFLAGS that can hold one 32-bit value that identifies changes in the current sample frame from the previous sample frame.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videosample.md">DXVADDI_VIDEOSAMPLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOSAMPLEFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
