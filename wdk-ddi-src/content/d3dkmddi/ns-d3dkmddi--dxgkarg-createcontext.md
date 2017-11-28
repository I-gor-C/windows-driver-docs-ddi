---
UID: NS.d3dkmddi._DXGKARG_CREATECONTEXT
title: DXGKARG_CREATECONTEXT
author: windows-driver-content
description: The DXGKARG_CREATECONTEXT structure describes parameters to create a device context.
old-location: display\dxgkarg_createcontext.htm
old-project: display
ms.assetid: 94239501-2eeb-479a-851a-14ae665c5887
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CREATECONTEXT, DXGKARG_CREATECONTEXT
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
req.alt-api: DXGKARG_CREATECONTEXT
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

# DXGKARG_CREATECONTEXT structure



## -description
<p>The DXGKARG_CREATECONTEXT structure describes parameters to create a device context.</p>


## -syntax

````
typedef struct _DXGKARG_CREATECONTEXT {
  HANDLE                  hContext;
  UINT                    NodeOrdinal;
  UINT                    EngineAffinity;
  DXGK_CREATECONTEXTFLAGS Flags;
  VOID                    *pPrivateDriverData;
  UINT                    PrivateDriverDataSize;
  DXGK_CONTEXTINFO        ContextInfo;
} DXGKARG_CREATECONTEXT;
````


## -struct-fields
<dl>

### -field <b>hContext</b>

<dd>
<p>[out] A handle to the context that a display miniport driver returns from a call to its <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> function. This handle represents the context in subsequent calls to the driver's <a href="display.dxgkddipresent">DxgkDdiPresent</a>, <a href="display.dxgkddirender">DxgkDdiRender</a>, and <a href="display.dxgkddidestroycontext">DxgkDdiDestroyContext</a> functions.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>[in] The node that the context is created for.</p>
</dd>

### -field <b>EngineAffinity</b>

<dd>
<p>[in] The engine within the node that <b>NodeOrdinal</b> specifies that the context is created for. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561037">DXGK_CREATECONTEXTFLAGS</a> structure that identifies how to create the context.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in] A pointer to a block of private data that is passed from the user-mode display driver to the display miniport driver. </p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in] The size, in bytes, of the private data that <b>pPrivateDriverData</b> points to.</p>
</dd>

### -field <b>ContextInfo</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a> structure that the display miniport driver populates to describe the device context.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561037">DXGK_CREATECONTEXTFLAGS</a>
</dt>
<dt>
<a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a>
</dt>
<dt>
<a href="display.dxgkddidestroycontext">DxgkDdiDestroyContext</a>
</dt>
<dt>
<a href="display.dxgkddipresent">DxgkDdiPresent</a>
</dt>
<dt>
<a href="display.dxgkddirender">DxgkDdiRender</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_CREATECONTEXT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
