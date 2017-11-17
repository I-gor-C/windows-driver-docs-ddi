---
UID: NC.fwpsk.FWPS_INJECT_COMPLETE0
title: FWPS_INJECT_COMPLETE0
author: windows-driver-content
description: The filter engine calls a callout's completionFn callout function whenever packet data, described by the netBufferList parameter in one of the packet injection functions, has been injected into the network stack.
old-location: netvista\completionfn.htm
ms.assetid: c03656ec-f0fe-49f5-8a04-2d26ef23c50a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: completionFn
req.alt-loc: Fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpmEngineOpen0
req.iface: 
---

# FWPS_INJECT_COMPLETE0 callback



## -description
<p>The filter engine calls a callout's 
  <i>completionFn</i> callout function whenever packet data, described by the 
  <i>netBufferList</i> parameter in one of the 
  <a href="NULL">packet injection functions</a>, has been
  injected into the network stack.</p>


## -prototype

````
FWPS_INJECT_COMPLETE0 completionFn;

void NTAPI completionFn(
  _In_    VOID            *context,
  _Inout_ NET_BUFFER_LIST *netBufferList,
  _In_    BOOLEAN         dispatchLevel
)
{ ... }
````


## -parameters
<dl>

### -param <i>context</i> [in]

<dd>
<p>A pointer to the 
     <i>completionContext</i> parameter of one of the 
     <a href="NULL">packet injection functions</a> called
     by the callout driver.</p>
</dd>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>The pointer passed in the 
     <i>netBufferList</i> parameter of one of the 
     <a href="NULL">packet injection functions</a> called
     by the callout driver.</p>
</dd>

### -param <i>dispatchLevel</i> [in]

<dd>
<p>A value that indicates the IRQL at which the 
     <i>completionFn</i> callout function is being called. If this parameter is <b>TRUE</b>, the 
     <i>completionFn</i> callout function is being called at IRQL = DISPATCH_LEVEL. If this parameter is
     <b>FALSE</b>, the 
     <i>completionFn</i> callout function is being called at an IRQL &lt; DISPATCH_LEVEL.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The FWPS_INJECT_COMPLETE0 type is defined as a pointer to the 
    <i>completionFn</i> function as follows:</p>

<p>The 
    <b>Status</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure pointed to by 
    <i>NetBufferList</i> indicates the result of the injection operation.</p>

<p>After packet data in a cloned or created <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure chain has successfully been
    injected into the network stack by one of the 
    <a href="NULL">packet injection functions</a>, 
    <i>completionFn</i> is called.</p>

<p>If the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a> function is
    called to inject a chain of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures, 
    <i>completionFn</i> will be called once for each <b>NET_BUFFER_LIST</b> in the chain, each time using the same 
    <i>completionContext</i> parameter specified in 
    <b>FwpsStreamInjectAsync0</b>. In this case, the callout driver's 
    <i>completionFn</i> implementation should call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a> to
    free the currently indicated <b>NET_BUFFER_LIST</b>.</p>

<p>The filter engine calls a callout's 
    <i>completionFn</i> callout function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>The FWPS_INJECT_COMPLETE0 type is defined as a pointer to the 
    <i>completionFn</i> function as follows:</p>

<p>The 
    <b>Status</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure pointed to by 
    <i>NetBufferList</i> indicates the result of the injection operation.</p>

<p>After packet data in a cloned or created <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure chain has successfully been
    injected into the network stack by one of the 
    <a href="NULL">packet injection functions</a>, 
    <i>completionFn</i> is called.</p>

<p>If the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a> function is
    called to inject a chain of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures, 
    <i>completionFn</i> will be called once for each <b>NET_BUFFER_LIST</b> in the chain, each time using the same 
    <i>completionContext</i> parameter specified in 
    <b>FwpsStreamInjectAsync0</b>. In this case, the callout driver's 
    <i>completionFn</i> implementation should call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a> to
    free the currently indicated <b>NET_BUFFER_LIST</b>.</p>

<p>The filter engine calls a callout's 
    <i>completionFn</i> callout function at IRQL &lt;= DISPATCH_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
<dt>
<a href="NULL">Packet Injection Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_INJECT_COMPLETE0 callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
