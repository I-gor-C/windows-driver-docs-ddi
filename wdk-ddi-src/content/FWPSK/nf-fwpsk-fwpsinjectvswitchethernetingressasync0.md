---
UID: NF.fwpsk.FwpsInjectvSwitchEthernetIngressAsync0
title: FwpsInjectvSwitchEthernetIngressAsync0
author: windows-driver-content
description: The FwpsInjectvSwitchEthernetIngressAsync0 (was FwpsInjectvSwitchIngressAsync0) function reinjects a previously absorbed virtual switch packet (unmodified) back to the virtual switch ingress data path where it was intercepted.
old-location: netvista\fwpsinjectvswitchingressasync0.htm
ms.assetid: ccb22035-08fe-44a6-88d5-bf9db7c2f499
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsInjectvSwitchEthernetIngressAsync0
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
ms.keywords: FwpsInjectvSwitchEthernetIngressAsync0
req.iface: 
---

# FwpsInjectvSwitchEthernetIngressAsync0 function



## -description
<p>The <b>FwpsInjectvSwitchEthernetIngressAsync0</b> (was <b>FwpsInjectvSwitchIngressAsync0</b>) function reinjects a previously absorbed virtual switch packet (unmodified) back to the virtual switch ingress data path where it was intercepted. This function can also inject a packet created with  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a>  function.</p>


## -syntax

````
NTSTATUS NTAPI FwpsInjectvSwitchEthernetIngressAsync0(
  _In_           HANDLE                  injectionHandle,
  _In_opt_       HANDLE                  injectionContext,
  _In_           _Reserved_ UINT32       flags,
  _In_opt_       _Reserved_ void         *reserved,
  _In_     const FWP_BYTE_BLOB           *vSwitchId,
  _In_           NDIS_SWITCH_PORT_ID     vSwitchSourcePortId,
  _In_           NDIS_SWITCH_NIC_INDEX   vSwitchSourceNicIndex,
                 _Inout_ NET_BUFFER_LIST *netBufferLists,
  _In_           FWPS_INJECT_COMPLETE    completionFn,
  _In_opt_       HANDLE                  completionContext
);
````


## -parameters
<dl>

### -param <i>injectionHandle</i> [in]

<dd>
<p>An injection handle that was previously created by a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a> function with the <i>flags</i> parameter set to <b>FWPS_INJECTION_TYPE_VSWITCH</b>.


The <i>addressFamily</i> parameter is not used and should be set to <b>AF_UNSPEC</b>.
</p>
</dd>

### -param <i>injectionContext</i> [in, optional]

<dd>
<p>An optional handle to the injection context that can be  retrieved with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>Reserved. Must be set to zero.</p>
</dd>

### -param <i>reserved</i> [in, optional]

<dd>
<p>Reserved. Must be set to NULL.</p>
</dd>

### -param <i>vSwitchId</i> [in]

<dd>
<p>The virtual  switch identifier that the filtering engine passed in the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a> structure to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function. This is the  <b>GUID</b> of the virtual switch that is provided in an xxx_VSWITCH_ID field. </p>
</dd>

### -param <i>vSwitchSourcePortId</i> [in]

<dd>
<p>The virtual  switch source port identifier. </p>
</dd>

### -param <i>vSwitchSourceNicIndex</i> [in]

<dd>
<p>The virtual  switch source NIC  index.</p>
</dd>

### -param <i>netBufferLists</i> 

<dd>
<p>A chain of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to be injected into the virtual switch egress data path.</p>
</dd>

### -param <i>completionFn</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a> callout function that is provided by
     the callout driver. The filter engine calls this function after the packet data, at the 
     <i>netBufferLists</i> parameter, has been injected into the virtual switch egress data path. The 
     <i>completionFn</i> function will be called once for each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> in the chain. <i>completionFn</i> must be specified when injecting cloned or created <b>NET_BUFFER_LIST</b> structures. This parameter can be NULL when injecting original unaltered <b>NET_BUFFER_LIST</b> structures that were received from the filter engine. </p>
</dd>

### -param <i>completionContext</i> [in, optional]

<dd>
<p>A pointer to a callout driver–provided context that is passed to the callout function pointed to
     by the 
     <i>completionFn</i> parameter. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsInjectvSwitchEthernetIngressAsync0</b> function returns one of the following <b>NTSTATUS</b> codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The virtual switch <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> chain was successfully injected.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>

When a callout injects packets with <b>FwpsInjectvSwitchEthernetIngressAsync0</b>, the injected packets could be classified again if the packets match the same filter as they were originally classified. Therefore, like callouts at IP layers, virtual switch callouts must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function to protect against infinite packet inspections.</p>

<p>

When a callout injects packets with <b>FwpsInjectvSwitchEthernetIngressAsync0</b>, the injected packets could be classified again if the packets match the same filter as they were originally classified. Therefore, like callouts at IP layers, virtual switch callouts must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function to protect against infinite packet inspections.</p>

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
<p>Available starting with Windows 8.</p>
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
<a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsInjectvSwitchEthernetIngressAsync0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
