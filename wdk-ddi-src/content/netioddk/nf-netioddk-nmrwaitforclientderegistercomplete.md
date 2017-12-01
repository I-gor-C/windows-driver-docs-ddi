---
UID: NF.netioddk.NmrWaitForClientDeregisterComplete
title: NmrWaitForClientDeregisterComplete
author: windows-driver-content
description: The NmrWaitForClientDeregisterComplete function waits for the deregistration of a client module to complete.
old-location: netvista\nmrwaitforclientderegistercomplete.htm
old-project: netvista
ms.assetid: aed0a69e-868c-4c7d-b601-003ff357da38
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NmrWaitForClientDeregisterComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: netioddk.h
req.include-header: Wsk.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NmrWaitForClientDeregisterComplete
req.alt-loc: netio.lib,netio.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Netio.lib
req.dll: 
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# NmrWaitForClientDeregisterComplete function



## -description
<p>The 
  <b>NmrWaitForClientDeregisterComplete</b> function waits for the deregistration of a client module to
  complete.</p>


## -syntax

````
NTSTATUS NmrWaitForClientDeregisterComplete(
  _In_ HANDLE NmrClientHandle
);
````


## -parameters
<dl>

### -param <i>NmrClientHandle</i> [in]

<dd>
<p>A handle used by the NMR to represent the registration of the client module. The NMR returns this
     handle to the client module when the client module calls the 
     <a href="..\netioddk\nf-netioddk-nmrregisterclient.md">NmrRegisterClient</a> function.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NmrWaitForClientDeregisterComplete</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The NMR completed deregistering the client module.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The client module called the 
       <b>NmrWaitForClientDeregisterComplete</b> function before calling the 
       <a href="..\netioddk\nf-netioddk-nmrderegisterclient.md">NmrDeregisterClient</a> function, or
       the handle specified in the NmrClientHandle parameter is not a valid client handle.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A client module calls the 
    <b>NmrWaitForClientDeregisterComplete</b> function to wait for the deregistration of the client module to
    complete. A client module calls the 
    <b>NmrWaitForClientDeregisterComplete</b> function only after calling the 
    <a href="..\netioddk\nf-netioddk-nmrderegisterclient.md">NmrDeregisterClient</a> function.</p>

<p>A client module typically calls the 
    <b>NmrWaitForClientDeregisterComplete</b> function from its 
    <a href="kernel.unload">Unload</a> function to wait until it is completely
    deregistered from the NMR before the client module is unloaded from the system. A client module must not
    return from a call to its 
    <b>Unload</b> function until after deregistration is
    complete.</p>

<p>
<div class="alert"><b>Note</b>  If a client module uses the Windows Driver Framework, it will typically call the 
     <b>NmrWaitForClientDeregisterComplete</b> function from its 
     <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-unload.md">EvtDriverUnload</a> event callback function. In
     this situation, the client module must not return from a call to its 
     <i>EvtDriverUnload</i> function until after
     deregistration is complete.</div>
<div> </div>
</p>

## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netioddk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Netio.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netioddk\nf-netioddk-nmrderegisterclient.md">NmrDeregisterClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NmrWaitForClientDeregisterComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
