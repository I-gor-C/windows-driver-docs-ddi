---
UID: NC.netdispumdddi.PFN_DESTROY_MIRACAST_CONTEXT
title: PFN_DESTROY_MIRACAST_CONTEXT
author: windows-driver-content
description: Called by the operating system to destroy a user-mode Miracast context.
old-location: display\destroymiracastcontext.htm
old-project: display
ms.assetid: 1b155e15-1e4e-45bb-98cc-f1c19923ed2c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DestroyMiracastContext
req.alt-loc: Netdispumdddi.h
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

# PFN_DESTROY_MIRACAST_CONTEXT callback



## -description
<p>Called by the operating system to destroy a user-mode Miracast context.</p>


## -prototype

````
PFN_DESTROY_MIRACAST_CONTEXT DestroyMiracastContext;

VOID NTAPI* DestroyMiracastContext(
  _In_ PVOID pMiracastContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>pMiracastContext</i> [in]

<dd>
<p>A pointer to a context associated with a display adapter.</p>
<p>The operating system obtained the context when it called the Miracast user-mode driver's <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> function.</p>
</dd>
</dl>

## -returns
<p>Does not return a value.</p>

## -remarks
<p>When this function is called, the Miracast user-mode driver should release all resources it allocated when <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> was last called.</p>

<p>If the display miniport driver is still reporting the Miracast monitor for this Miracast instance, the Miracast user-mode driver can optionally call the display miniport driver to immediately send a monitor departure hot-plug detection (HPD) awareness value, or it can let the display miniport driver do so in its kernel-mode <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-destroy-context.md">DxgkDdiMiracastDestroyContext</a> function.</p>

<p>After this call completes, the operating system unloads the Miracast user-mode driver such that the driver leaves no resources still opened and no thread still running.</p>

<p>The operating system guarantees that only one of the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a>, <i>DestroyMiracastContext</i>, <a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a>, and <a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a> functions is called at a time.</p>

<p>When this function is called, the Miracast user-mode driver should release all resources it allocated when <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> was last called.</p>

<p>If the display miniport driver is still reporting the Miracast monitor for this Miracast instance, the Miracast user-mode driver can optionally call the display miniport driver to immediately send a monitor departure hot-plug detection (HPD) awareness value, or it can let the display miniport driver do so in its kernel-mode <a href="..\dispmprt\nc-dispmprt-dxgkddi-miracast-destroy-context.md">DxgkDdiMiracastDestroyContext</a> function.</p>

<p>After this call completes, the operating system unloads the Miracast user-mode driver such that the driver leaves no resources still opened and no thread still running.</p>

<p>The operating system guarantees that only one of the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a>, <i>DestroyMiracastContext</i>, <a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a>, and <a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a> functions is called at a time.</p>

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
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_DESTROY_MIRACAST_CONTEXT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
