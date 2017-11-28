---
UID: NF.fwpsk.FwpsInjectionHandleDestroy0
title: FwpsInjectionHandleDestroy0
author: windows-driver-content
description: The FwpsInjectionHandleDestroy0 function destroys an injection handle that was previously created by calling the FwpsInjectionHandleCreate0 function.Note  FwpsInjectionHandleDestroy0 is a specific version of FwpsInjectionHandleDestroy.
old-location: netvista\fwpsinjectionhandledestroy0.htm
old-project: netvista
ms.assetid: 5a00917b-36e8-4e06-a001-d8e6ac2e3573
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsInjectionHandleDestroy0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsInjectionHandleDestroy0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FwpsInjectionHandleDestroy0 function



## -description
<p>The 
  <b>FwpsInjectionHandleDestroy0</b> function destroys an injection handle that was previously created by
  calling the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a> function.</p>


## -syntax

````
NTSTATUS FwpsInjectionHandleDestroy0(
  _In_ HANDLE injectionHandle
);
````


## -parameters
<dl>

### -param <i>injectionHandle</i> [in]

<dd>
<p>The injection handle being destroyed.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsInjectionHandleDestroy0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The injection handle was successfully destroyed.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsInjectionHandleDestroy0</b> function to destroy an injection handle that was previously created by
    calling the 
    <a href="..\fwpsk\nf-fwpsk-fwpsinjectionhandlecreate0.md">
    FwpsInjectionHandleCreate0</a> function. The 
    <b>FwpsInjectionHandleDestroy0</b> function will not return to the caller until all pending injections are
    completed.</p>

<p>A callout driver calls the 
    <b>FwpsInjectionHandleDestroy0</b> function to destroy an injection handle that was previously created by
    calling the 
    <a href="..\fwpsk\nf-fwpsk-fwpsinjectionhandlecreate0.md">
    FwpsInjectionHandleCreate0</a> function. The 
    <b>FwpsInjectionHandleDestroy0</b> function will not return to the caller until all pending injections are
    completed.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsInjectionHandleDestroy0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
