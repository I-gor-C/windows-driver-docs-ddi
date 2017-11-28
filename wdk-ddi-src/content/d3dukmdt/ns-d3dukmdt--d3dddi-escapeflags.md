---
UID: NS.d3dukmdt._D3DDDI_ESCAPEFLAGS
title: D3DDDI_ESCAPEFLAGS
author: windows-driver-content
description: The D3DDDI_ESCAPEFLAGS structure identifies how the user-mode display driver shares information with the display miniport driver.
old-location: display\d3dddi_escapeflags.htm
old-project: display
ms.assetid: 40648f6a-3393-4374-beff-e097c299f9e9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_ESCAPEFLAGS, D3DDDI_ESCAPEFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_ESCAPEFLAGS
req.alt-loc: d3dukmdt.h
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

# D3DDDI_ESCAPEFLAGS structure



## -description
<p>The D3DDDI_ESCAPEFLAGS structure identifies how the user-mode display driver shares information with the display miniport driver.</p>


## -syntax

````
typedef struct _D3DDDI_ESCAPEFLAGS {
  union {
    struct {
      UINT HardwareAccess  :1;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3))

      UINT DeviceStatusQuery  :1;
      UINT ChangeFrameLatency  :1;
      UINT Reserved  :29;
#else 
      UINT Reserved  :31;
#endif 
    };
    UINT   Value;
  };
} D3DDDI_ESCAPEFLAGS;
````


## -struct-fields
<dl>

### -field <b>HardwareAccess</b>

<dd>
<p>A <b>UINT</b> value that specifies whether the operating system performs the <a href="https://msdn.microsoft.com/2b7c1eae-6527-469e-a2fa-74d2a1246bd3">second level of synchronization</a> into the display miniport driver for the <a href="display.dxgkddiescape">DxgkDdiEscape</a> call. If the driver requires the second level of synchronization and the <b>HardwareAccess</b> flag is not set, the call to the driver's <i>DxgkDdiEscape</i> function should fail. </p>
<p>Starting in Windows 8.1,  if this member is set, <b>DeviceStatusQuery</b> and <b>ChangeFrameLatency</b> must be set to zero.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>DeviceStatusQuery</b>

<dd>
<p>
  
  If set, when the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a> function is called and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544190">D3DDDICB_ESCAPE</a>.<b>PrivateDriverDataSize</b> member is <code>sizeof(D3DDDI_EXECUTIONSTATEESCAPE)</code>, the Direct3D runtime interprets the <b>D3DDDICB_ESCAPE</b>.<b>pPrivateDriverData</b> member as a pointer to a buffer that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/dn482417">D3DDDI_EXECUTIONSTATEESCAPE</a> structure. In addition, the runtime processes the <i>pfnEscapeCb</i> as a status query by writing the requested info into the provided buffer instead of sending a <a href="display.dxgkddiescape">DxgkDdiEscape</a> call to the display miniport driver.</p>
<p>If this member is set, <b>HardwareAccess</b> and <b>ChangeFrameLatency</b> must be set to zero.</p>
<p>Supported starting with Windows 8.1.</p>
<p>The operating system ignores this member if it is prior to Windows 8.1, or if the user-mode driver was initialized with an <i>OpenAdapterXxx</i> call where the <i>pOpenData</i>-&gt;<b>Interface</b> member indicates Direct3D version 8 or earlier.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>ChangeFrameLatency</b>

<dd>
<p>
  
  If set, when the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a> function is called, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544190">D3DDDICB_ESCAPE</a>.<b>PrivateDriverDataSize</b> member is <code>sizeof(D3DDDI_FRAMELATENCYESCAPE)</code> and conditions in Remarks are also met, the Direct3D runtime interprets the <b>D3DDDICB_ESCAPE</b>.<b>pPrivateDriverData</b> member as a pointer to a buffer that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/dn482418">D3DDDI_FRAMELATENCYESCAPE</a> structure. In addition, the runtime processes the <i>pfnEscapeCb</i> as a request to change the DirectX graphics kernel subsystem's maximum frame latency by writing the requested info into the provided buffer instead of sending a <a href="display.dxgkddiescape">DxgkDdiEscape</a> call to the display miniport driver.</p>
<p>If this member is set, <b>HardwareAccess</b> and <b>DeviceStatusQuery</b> must be set to zero.</p>
<p>Supported starting with Windows 8.1.</p>
<p>The operating system ignores this member if it is prior to Windows 8.1, or if the user-mode driver was initialized with an <i>OpenAdapterXxx</i> call where the <i>pOpenData</i>-&gt;<b>Interface</b> member indicates Direct3D version 8 or earlier.</p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 29 bits (0xFFFFFFF8) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that is contained in D3DDDI_ESCAPEFLAGS that can hold one 32-bit value that identifies how to share information.</p>
</dd>
</dl>

## -remarks
<p>If <b>ChangeFrameLatency</b> is set, a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a> call will succeed only if:</p>

<p>If these conditions are not met, <i>pfnEscapeCb</i> call returns an <b>E_INVALIDARG</b> error code.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn482417">D3DDDI_EXECUTIONSTATEESCAPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn482418">D3DDDI_FRAMELATENCYESCAPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544190">D3DDDICB_ESCAPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557588">DXGKARG_ESCAPE</a>
</dt>
<dt>
<a href="display.dxgkddiescape">DxgkDdiEscape</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_ESCAPEFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
