---
UID: NC.dispmprt.DXGKDDI_MIRACAST_DESTROY_CONTEXT
title: DXGKDDI_MIRACAST_DESTROY_CONTEXT
author: windows-driver-content
description: Destroys an instance of a Miracast device.
old-location: display\dxgkddimiracastdestroycontext.htm
old-project: display
ms.assetid: 2DEEB379-C9E8-45E4-920D-D94F8C27A4EF
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiMiracastDestroyContext
req.alt-loc: Dispmprt.h
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
req.iface: IDebugSystemObjects4
---

# DXGKDDI_MIRACAST_DESTROY_CONTEXT callback



## -description
<p>Destroys an instance of a Miracast device.</p>


## -prototype

````
DXGKDDI_MIRACAST_DESTROY_CONTEXT DxgkDdiMiracastDestroyContext;

VOID* DxgkDdiMiracastDestroyContext(
  _In_ PVOID DriverContext,
  _In_ PVOID MiracastContext
)
{ ... }
````


## -parameters
<dl>

### -param DriverContext [in]

<dd>
<p>A handle to a context block that is associated with a display adapter. The display miniport driver's <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function previously provided this handle to the DirectX graphics kernel subsystem.</p>
</dd>

### -param MiracastContext [in]

<dd>
<p>The Miracast device context, supplied by the operating system. This context was previously provided by the driver in a call to the <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-create-context.md">DxgkDdiMiracastCreateContext</a> function.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>When this function is called, the display miniport driver should release all kernel-mode  resources that it allocated when it processed the <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-create-context.md">DxgkDdiMiracastCreateContext</a> function, and it should immediately send a monitor departure hot-plug detection (HPD) awareness value to the operating system.</p>

<p>The operating system guarantees that, after it calls this function, it will not make any more calls to the <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-handle-io-control.md">DxgkDdiMiracastIoControl</a> function.</p>

<p>If a Miracast device is disconnected before the <a href="display.dxgkddicommitvidpn">DxgkDdiCommitVidPn</a> function completes, while a present operation is still occurring on this Miracast target, the display miniport driver should not send any data to the user-mode Miracast driver.</p>

<p>If the user-mode <a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a> function takes too long to complete, the operating system calls <i>DxgkDdiMiracastDestroyContext</i> while the user-mode Miracast driver is still running. In this case, the operating system blocks any further calls to the user-mode <a href="..\netdispumdddi\nc-netdispumdddi-pfn-miracast-io-control.md">MiracastIoControl</a> function.</p>

<p>The operating system groups the <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-create-context.md">DxgkDdiMiracastCreateContext</a>, <i>DxgkDdiMiracastDestroyContext</i>, and <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-handle-io-control.md">DxgkDdiMiracastIoControl</a> functions as a <i>Miracast</i> class. The operating system guarantees that these functions follow the second-level synchronization mode as defined in <a href="https://msdn.microsoft.com/2b7c1eae-6527-469e-a2fa-74d2a1246bd3">Threading and Synchronization Second Level</a>. These functions can be called when other level 0, 1, or other classes of level 2 functions are being called on another thread context. However, only one of these level 2 Miracast-class functions can be called at a time.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="display.dxgkddicommitvidpn">DxgkDdiCommitVidPn</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-create-context.md">DxgkDdiMiracastCreateContext</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-handle-io-control.md">DxgkDdiMiracastIoControl</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-miracast-io-control.md">MiracastIoControl</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_MIRACAST_DESTROY_CONTEXT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
