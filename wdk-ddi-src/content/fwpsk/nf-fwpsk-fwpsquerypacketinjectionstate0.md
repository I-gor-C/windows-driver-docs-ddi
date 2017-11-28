---
UID: NF.fwpsk.FwpsQueryPacketInjectionState0
title: FwpsQueryPacketInjectionState0
author: windows-driver-content
description: The FwpsQueryPacketInjectionState0 function is called by a callout to query the injection state of packet data.Note  FwpsQueryPacketInjectionState0 is a specific version of FwpsQueryPacketInjectionState.
old-location: netvista\fwpsquerypacketinjectionstate0.htm
old-project: netvista
ms.assetid: 785d99a5-a8c9-4763-bdd4-e26f604f6be7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsQueryPacketInjectionState0
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
req.alt-api: FwpsQueryPacketInjectionState0
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FwpsQueryPacketInjectionState0 function



## -description
<p>The 
  <b>FwpsQueryPacketInjectionState0</b> function is called by a callout to query the injection state of packet
  data.</p>


## -syntax

````
FWPS_PACKET_INJECTION_STATE NTAPI FwpsQueryPacketInjectionState0(
  _In_            HANDLE          injectionHandle,
  _In_      const NET_BUFFER_LIST *netBufferList,
  _Out_opt_       HANDLE          *injectionContext
);
````


## -parameters
<dl>

### -param <i>injectionHandle</i> [in]

<dd>
<p>An injection handle that was previously created by a call to the 
     <a href="..\fwpsk\nf-fwpsk-fwpsinjectionhandlecreate0.md">
     FwpsInjectionHandleCreate0</a> function.</p>
</dd>

### -param <i>netBufferList</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that describes
     the packet data that is being classified. The packet can originate from the network stack, or it can be
     injected into the network stack by a WFP callout driver.</p>
</dd>

### -param <i>injectionContext</i> [out, optional]

<dd>
<p>An optional handle to the injection context. If the pointer is specified, and if the packet
     injection state 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> associated with the injection handle is FWPS_PACKET_INJECTED_BY_SELF
     or FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF, the injection context supplied when the packet was injected
     will be returned.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsQueryPacketInjectionState0</b> function returns one of the constant values of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> enumeration.</p>

## -remarks
<p>Because injected packet data can be reclassified against the callout that injected it, this function
    allows a callout to inspect the injection history of packet data when necessary, thereby avoiding the
    need to make repeated inspections of packet data that has already been inspected.</p>

<p>A callout can track other callout-specific information by specifying the optional 
    <i>injectionContext</i> handle in one of the 
    <a href="NULL">packet injection functions</a> at the
    time of packet data injection. If the 
    <b>FwpsQueryPacketInjectionState0</b> function returns <b>FWPS_PACKET_INJECTED_BY_SELF</b> or
    <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>, the supplied 
    <i>injectionContext</i> will be returned as the 
    <i>completionContext</i> parameter of the function that performed the injection.</p>

<p>If the return value is <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>, the
    network buffer list pointed to by 
    <i>netBufferList</i> should not be further modified or pended as part of a cloning and injection
    procedure. In this case, the callout should set the 
    <b>actionType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure pointed to
    by the 
    <i>classifyOut</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function to one of the following
    values.</p>

<p></p><dl>
<dt><a id="FWP_ACTION_BLOCK"></a><a id="fwp_action_block"></a>FWP_ACTION_BLOCK</dt>
<dd>
<p>Specifies that subsequent modification of the clone network buffer list is not allowed.</p>
</dd>
<dt><a id="FWP_ACTION_PERMIT"></a><a id="fwp_action_permit"></a>FWP_ACTION_PERMIT</dt>
<dd>
<p>Specifies that the injection function has not modified the clone network buffer list, or modification
      is allowed.</p>
</dd>
</dl><p>Specifies that subsequent modification of the clone network buffer list is not allowed.</p>

<p>Specifies that the injection function has not modified the clone network buffer list, or modification
      is allowed.</p>

<p>Because injected packet data can be reclassified against the callout that injected it, this function
    allows a callout to inspect the injection history of packet data when necessary, thereby avoiding the
    need to make repeated inspections of packet data that has already been inspected.</p>

<p>A callout can track other callout-specific information by specifying the optional 
    <i>injectionContext</i> handle in one of the 
    <a href="NULL">packet injection functions</a> at the
    time of packet data injection. If the 
    <b>FwpsQueryPacketInjectionState0</b> function returns <b>FWPS_PACKET_INJECTED_BY_SELF</b> or
    <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>, the supplied 
    <i>injectionContext</i> will be returned as the 
    <i>completionContext</i> parameter of the function that performed the injection.</p>

<p>If the return value is <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>, the
    network buffer list pointed to by 
    <i>netBufferList</i> should not be further modified or pended as part of a cloning and injection
    procedure. In this case, the callout should set the 
    <b>actionType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure pointed to
    by the 
    <i>classifyOut</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function to one of the following
    values.</p>

<p></p><dl>
<dt><a id="FWP_ACTION_BLOCK"></a><a id="fwp_action_block"></a>FWP_ACTION_BLOCK</dt>
<dd>
<p>Specifies that subsequent modification of the clone network buffer list is not allowed.</p>
</dd>
<dt><a id="FWP_ACTION_PERMIT"></a><a id="fwp_action_permit"></a>FWP_ACTION_PERMIT</dt>
<dd>
<p>Specifies that the injection function has not modified the clone network buffer list, or modification
      is allowed.</p>
</dd>
</dl><p>Specifies that subsequent modification of the clone network buffer list is not allowed.</p>

<p>Specifies that the injection function has not modified the clone network buffer list, or modification
      is allowed.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsQueryPacketInjectionState0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
