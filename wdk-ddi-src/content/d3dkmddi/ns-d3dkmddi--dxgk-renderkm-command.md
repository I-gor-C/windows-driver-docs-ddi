---
UID: NS.d3dkmddi._DXGK_RENDERKM_COMMAND
title: DXGK_RENDERKM_COMMAND
author: windows-driver-content
description: The DXGK_RENDERKM_COMMAND structure is used to construct a command buffer to control GDI hardware-accelerated rendering.
old-location: display\dxgk_renderkm_command.htm
old-project: display
ms.assetid: 998bf0ca-c08d-41d9-ba3e-74a620ed51ae
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_RENDERKM_COMMAND, DXGK_RENDERKM_COMMAND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_RENDERKM_COMMAND
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

# DXGK_RENDERKM_COMMAND structure



## -description
<p>The DXGK_RENDERKM_COMMAND structure is used to construct a command buffer to control GDI hardware-accelerated rendering.</p>


## -syntax

````
typedef struct _DXGK_RENDERKM_COMMAND {
  DXGK_RENDERKM_OPERATION OpCode;
  UINT                    CommandSize;
  union {
    DXGK_GDIARG_BITBLT         BitBlt;
    DXGK_GDIARG_COLORFILL      ColorFill;
    DXGK_GDIARG_ALPHABLEND     AlphaBlend;
    DXGK_GDIARG_STRETCHBLT     StretchBlt;
    DXGK_GDIARG_TRANSPARENTBLT TransparentBlt;
    DXGK_GDIARG_CLEARTYPEBLEND ClearTypeBlend;
  } Command;
} DXGK_RENDERKM_COMMAND;
````


## -struct-fields
<dl>

### -field <b>OpCode</b>

<dd>
<p>
      [in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562029">DXGK_RENDERKM_OPERATION</a>-type operation code that identifies the GDI hardware-accelerated rendering operation to process. For more information about GDI hardware acceleration, see the Remarks section.
     </p>
</dd>

### -field <b>CommandSize</b>

<dd>
<p>
      [in] The size of the current command, in bytes. This is equal to the number of bytes from the beginning of DXGK_RENDERKM_COMMAND up to the next command.
     </p>
</dd>

### -field <b>Command</b>

<dd>
<dl>

### -field <b>BitBlt</b>

<dd>
<p>
       [in] A bit-block transfer (bitblt) that is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561079">DXGK_GDIARG_BITBLT</a> structure.
      </p>
</dd>

### -field <b>ColorFill</b>

<dd>
<p>
       [in] A color fill that is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561083">DXGK_GDIARG_COLORFILL</a> structure.
      </p>
</dd>

### -field <b>AlphaBlend</b>

<dd>
<p>
       [in] An alpha blend that is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561074">DXGK_GDIARG_ALPHABLEND</a> structure.
      </p>
</dd>

### -field <b>StretchBlt</b>

<dd>
<p>
       [in] A stretch bit-block transfer that is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561089">DXGK_GDIARG_STRETCHBLT</a> structure.
      </p>
</dd>

### -field <b>TransparentBlt</b>

<dd>
<p>
       [in] A transparent bit-block transfer that is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561091">DXGK_GDIARG_TRANSPARENTBLT</a> structure.
      </p>
</dd>

### -field <b>ClearTypeBlend</b>

<dd>
<p>
       [in] A ClearType blend that is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561082">DXGK_GDIARG_CLEARTYPEBLEND</a> structure.
      </p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>An array of variable-size DXGK_RENDERKM_COMMAND structures defines a command buffer that is used to control GDI hardware-accelerated rendering.</p>

<p>A display miniport driver should report that it supports command buffer processing for GDI hardware acceleration by setting <a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>-&gt;<b>PresentationCaps</b>.<b>SupportKernelModeCommandBuffer</b> to <b>TRUE</b>.</p>

<p>Each command varies in length depending on the value of the <b>OpCode</b> member and the number of sub-rectangles in the command.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561074">DXGK_GDIARG_ALPHABLEND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561079">DXGK_GDIARG_BITBLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561082">DXGK_GDIARG_CLEARTYPEBLEND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561083">DXGK_GDIARG_COLORFILL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561089">DXGK_GDIARG_STRETCHBLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561091">DXGK_GDIARG_TRANSPARENTBLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562029">DXGK_RENDERKM_OPERATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_RENDERKM_COMMAND structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
