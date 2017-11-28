---
UID: NS.d3dkmddi._DXGKARG_ESCAPE
title: DXGKARG_ESCAPE
author: windows-driver-content
description: The DXGKARG_ESCAPE structure describes information that the user-mode display driver shares with the display miniport driver.
old-location: display\dxgkarg_escape.htm
old-project: display
ms.assetid: 73a1afa6-e156-4733-b204-a9cae4e18563
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_ESCAPE, DXGKARG_ESCAPE
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
req.alt-api: DXGKARG_ESCAPE
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

# DXGKARG_ESCAPE structure



## -description
<p>The DXGKARG_ESCAPE structure describes information that the user-mode display driver shares with the display miniport driver.</p>


## -syntax

````
typedef struct _DXGKARG_ESCAPE {
  HANDLE             hDevice;
  D3DDDI_ESCAPEFLAGS Flags;
  VOID               *pPrivateDriverData;
  UINT               PrivateDriverDataSize;
  HANDLE             hContext;
} DXGKARG_ESCAPE;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the display device (graphics context) that was originally passed to the display miniport driver's <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a> function.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544541">D3DDDI_ESCAPEFLAGS</a> structure that indicates, in bit-field flags, how to share information.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in/out] A pointer to a buffer that contains the information that the display miniport driver and the user-mode display driver share.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in/out] The size, in bytes, of the buffer that <b>pPrivateDriverData</b> points to.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] A handle to the context that was originally passed to the display miniport driver's <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> function.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544541">D3DDDI_ESCAPEFLAGS</a>
</dt>
<dt>
<a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a>
</dt>
<dt>
<a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a>
</dt>
<dt>
<a href="display.dxgkddiescape">DxgkDdiEscape</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_ESCAPE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
