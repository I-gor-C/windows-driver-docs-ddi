---
UID: NC.netdispumdddi.PFN_CREATE_MIRACAST_CONTEXT
title: PFN_CREATE_MIRACAST_CONTEXT
author: windows-driver-content
description: Called by the operating system to create a user-mode Miracast context.
old-location: display\createmiracastcontext.htm
ms.assetid: 3b10ddd9-a48d-4f96-b35e-db017d1f9583
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreateMiracastContext
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
ms.keywords: NDK_SRQ, NDK_SRQ
req.iface: 
---

# PFN_CREATE_MIRACAST_CONTEXT callback



## -description
<p>Called by the operating system to create a user-mode Miracast context.</p>


## -prototype

````
PFN_CREATE_MIRACAST_CONTEXT CreateMiracastContext;

NTSTATUS NTAPI* CreateMiracastContext(
  _In_  HANDLE             hMiracastDeviceHandle,
  _In_  MIRACAST_CALLBACKS *pMiracastCallbacks,
  _Out_ PVOID              *ppMiracastContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMiracastDeviceHandle</i> [in]

<dd>
<p>A handle to the current Miracast display device, supplied by the operating system.</p>
</dd>

### -param <i>pMiracastCallbacks</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn265470">MIRACAST_CALLBACKS</a> structure that has pointers to callback functions, supplied by the operating system,  that the Miracast user-mode driver can call.</p>
</dd>

### -param <i>ppMiracastContext</i> [out]

<dd>
<p>A pointer to a buffer, supplied by the operating system, that holds the Miracast context that the Miracast user-mode driver returns.</p>
</dd>
</dl>

## -returns
<p>On success, this function returns <b>STATUS_SUCCESS</b>. Otherwise, the function returns an error code defined in the Ntstatus.h header.</p>

## -remarks
<p>When this function is called, the Miracast user-mode driver should prepare all resources that it needs for a new Miracast connected session.</p>

<p>The driver can call the callback functions pointed to by <i>pMiracastCallbacks</i> only during the lifetime of the current Miracast context.</p>

<p>The operating system guarantees that only one of the <i>CreateMiracastContext</i>, <a href="https://msdn.microsoft.com/1b155e15-1e4e-45bb-98cc-f1c19923ed2c">DestroyMiracastContext</a>, <a href="https://msdn.microsoft.com/2778d9d0-7f97-416f-a5ae-3754b17e8a29">StartMiracastSession</a>, and <a href="https://msdn.microsoft.com/ab9ad8ee-9390-41a4-9a69-2e98579b2b77">StopMiracastSession</a> functions is called at a time.</p>

<p>When this function is called, the Miracast user-mode driver should prepare all resources that it needs for a new Miracast connected session.</p>

<p>The driver can call the callback functions pointed to by <i>pMiracastCallbacks</i> only during the lifetime of the current Miracast context.</p>

<p>The operating system guarantees that only one of the <i>CreateMiracastContext</i>, <a href="https://msdn.microsoft.com/1b155e15-1e4e-45bb-98cc-f1c19923ed2c">DestroyMiracastContext</a>, <a href="https://msdn.microsoft.com/2778d9d0-7f97-416f-a5ae-3754b17e8a29">StartMiracastSession</a>, and <a href="https://msdn.microsoft.com/ab9ad8ee-9390-41a4-9a69-2e98579b2b77">StopMiracastSession</a> functions is called at a time.</p>

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
<a href="https://msdn.microsoft.com/1b155e15-1e4e-45bb-98cc-f1c19923ed2c">DestroyMiracastContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265470">MIRACAST_CALLBACKS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2778d9d0-7f97-416f-a5ae-3754b17e8a29">StartMiracastSession</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ab9ad8ee-9390-41a4-9a69-2e98579b2b77">StopMiracastSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_CREATE_MIRACAST_CONTEXT callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
