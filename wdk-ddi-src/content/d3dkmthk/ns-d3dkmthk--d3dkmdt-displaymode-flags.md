---
UID: NS.d3dkmthk._D3DKMDT_DISPLAYMODE_FLAGS
title: D3DKMDT_DISPLAYMODE_FLAGS
author: windows-driver-content
description: The D3DKMDT_DISPLAYMODE_FLAGS structure identifies attributes of a display mode.
old-location: display\d3dkmdt_displaymode_flags.htm
old-project: display
ms.assetid: 0b45cd69-5c9e-4772-a68f-d604806e7789
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_DISPLAYMODE_FLAGS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_DISPLAYMODE_FLAGS
req.alt-loc: d3dkmthk.h
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

# D3DKMDT_DISPLAYMODE_FLAGS structure



## -description
<p>The D3DKMDT_DISPLAYMODE_FLAGS structure identifies attributes of a display mode.</p>


## -syntax

````
typedef struct _D3DKMDT_DISPLAYMODE_FLAGS {
#if (DXGKDDI_INTERFACE_VERSION < DXGKDDI_INTERFACE_VERSION_WIN8)
  BOOLEAN                     ValidatedAgainstMonitorCaps  :1;
  BOOLEAN                     RoundedFakeMode  :1;
  D3DKMDT_MODE_PRUNING_REASON ModePruningReason  :4;
  UINT                        Reserved  :28;
#else 
  UINT                        ValidatedAgainstMonitorCaps  :1;
  UINT                        RoundedFakeMode  :1;
  UINT                          :0;
  D3DKMDT_MODE_PRUNING_REASON ModePruningReason  :4;
  UINT                        Stereo  :1;
  UINT                        AdvancedScanCapable  :1;
  UINT                        Reserved  :26;
#endif 
} D3DKMDT_DISPLAYMODE_FLAGS;
````


## -struct-fields
<dl>

### -field <b>ValidatedAgainstMonitorCaps</b>

<dd>
<p>A Boolean value that specifies whether the display mode is supported by the monitor that the display mode will be displayed on.</p>
<p>Setting this member is equivalent to setting the first bit of a 32-bit value (0x00000001).</p>
</dd>

### -field <b>RoundedFakeMode</b>

<dd>
<p>A Boolean value that specifies whether the display mode is rounded.</p>
<p>Setting this member is equivalent to setting the second bit of a 32-bit value (0x00000002).</p>
</dd>

### -field <b>ModePruningReason</b>

<dd>
<p>[in] A value of type <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmdt-mode-pruning-reason.md">D3DKMDT_MODE_PRUNING_REASON</a> that identifies the reason why the monitor either supports the display mode or does not support the display mode. The four bits are defined by one of the values in the <b>D3DKMDT_MODE_PRUNING_REASON</b> enumeration type and depend on the setting of the <b>ValidatedAgainstMonitorCaps</b> member. For more information about how the <b>ModePruningReason</b> value is set, see <b>D3DKMDT_MODE_PRUNING_REASON</b>.</p>
<p>Setting this member is equivalent to setting bits 4 through 7 of a 32-bit value (0x0000003C).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member is equivalent to setting the remaining 28 bits (0xFFFFFFF0) of a 32-bit value to zeros.</p>
</dd>

### -field <b>ValidatedAgainstMonitorCaps</b>

<dd>
<p>A UINT value that specifies whether the display mode is supported by the monitor that the display mode will be displayed on.</p>
<p>Setting this member is equivalent to setting the first bit of a 32-bit value (0x00000001).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>RoundedFakeMode</b>

<dd>
<p>A UINT value that specifies whether the display mode is rounded.</p>
<p>Setting this member is equivalent to setting the second bit of a 32-bit value (0x00000002).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>ModePruningReason</b>

<dd>
<p>[in] A value of type <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmdt-mode-pruning-reason.md">D3DKMDT_MODE_PRUNING_REASON</a> that identifies the reason why the monitor either supports the display mode or does not support the display mode. The four bits are defined by one of the values in the <b>D3DKMDT_MODE_PRUNING_REASON</b> enumeration type and depend on the setting of the <b>ValidatedAgainstMonitorCaps</b> member. For more information about how the <b>ModePruningReason</b> value is set, see <b>D3DKMDT_MODE_PRUNING_REASON</b>.</p>
<p>This member is equivalent to bits 4 through 7 of a 32-bit value (0x0000003C). </p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Stereo</b>

<dd>
<p>[in] </p>
<p>A UINT value that specifies whether stereo is supported by the monitor that the display mode will be displayed on.</p>
<p>Setting this member is equivalent to setting the eighth bit of a 32-bit value (0x00000080).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>AdvancedScanCapable</b>

<dd>
<p>[in] A UINT value that specifies whether the driver supports the advanced scan capability.</p>
<p>The driver reports support for this option in the current display mode by setting the <b>Type</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-source-mode.md">D3DKMDT_VIDPN_SOURCE_MODE</a> structure to <b>D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN</b>.</p>
<p>Setting this member is equivalent to setting the ninth bit of a 32-bit value (0x00000100).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Setting this member is equivalent to setting the remaining 26 bits (0xFFFFFFC0) of a 32-bit value to zeros.</p>
<p>Supported starting with Windows 8.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-displaymode.md">D3DKMT_DISPLAYMODE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ne-d3dkmthk--d3dkmdt-mode-pruning-reason.md">D3DKMDT_MODE_PRUNING_REASON</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_DISPLAYMODE_FLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
