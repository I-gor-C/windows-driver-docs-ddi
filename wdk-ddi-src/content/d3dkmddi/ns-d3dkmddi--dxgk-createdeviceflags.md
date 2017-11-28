---
UID: NS.d3dkmddi._DXGK_CREATEDEVICEFLAGS
title: DXGK_CREATEDEVICEFLAGS
author: windows-driver-content
description: The DXGK_CREATEDEVICEFLAGS structure identifies how to create devices.
old-location: display\dxgk_createdeviceflags.htm
old-project: display
ms.assetid: 31dc1493-a7c9-4ca0-b718-98224d9c5675
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CREATEDEVICEFLAGS, DXGK_CREATEDEVICEFLAGS
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
req.alt-api: DXGK_CREATEDEVICEFLAGS
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

# DXGK_CREATEDEVICEFLAGS structure



## -description
<p>The DXGK_CREATEDEVICEFLAGS structure identifies how to create devices.</p>


## -syntax

````
typedef struct _DXGK_CREATEDEVICEFLAGS {
  union {
    struct {
      UINT SystemDevice  :1;
      UINT GdiDevice  :1;
      UINT Reserved  :29;
      UINT DXGK_DEVICE_RESERVED0  :1;
    };
    UINT Value;
  };
} DXGK_CREATEDEVICEFLAGS;
````


## -struct-fields
<dl>

### -field <b>SystemDevice</b>

<dd>
<p>A UINT value that specifies whether devices that the driver's <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a> function creates are system devices.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>GdiDevice</b>

<dd>
<p>A UINT value that specifies whether the devices that the driver's <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a> function creates are GDI-specific devices.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit Value member (0x00000002).</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting bits 3 through 31 (0x7FFFFFFC) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>DXGK_DEVICE_RESERVED0</b>

<dd>
<p>Supported beginning with Windows 8.</p>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the last bit (0x80000000) of the 32-bit <b>Value</b> member to zero.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that DXGK_CREATEDEVICEFLAGS contains that can hold a 32-bit value that identifies how to create devices.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557570">DXGKARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CREATEDEVICEFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
