---
UID: NF.ndis.NdisClIncomingCallComplete
title: NdisClIncomingCallComplete
author: windows-driver-content
description: NdisClIncomingCallComplete returns a client's acceptance or rejection of an offered incoming call, for which the client's ProtocolClIncomingCall function previously returned NDIS_STATUS_PENDING.
old-location: netvista\ndisclincomingcallcomplete.htm
ms.assetid: b3931dd7-319e-4ef8-9812-6dc3f2e41b2c
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisClIncomingCallComplete
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisClIncomingCallComplete
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClIncomingCallComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Protocol_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisClIncomingCallComplete
req.iface: 
---

# NdisClIncomingCallComplete function



## -description
<p><b>NdisClIncomingCallComplete</b> returns a client's acceptance or rejection of an offered incoming call,
  for which the client's 
  <a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">ProtocolClIncomingCall</a> function
  previously returned NDIS_STATUS_PENDING.</p>


## -syntax

````
VOID NdisClIncomingCallComplete(
  _In_ NDIS_STATUS         Status,
  _In_ NDIS_HANDLE         NdisVcHandle,
  _In_ PCO_CALL_PARAMETERS CallParameters
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Is set to NDIS_STATUS_SUCCESS if the client accepts the offered call. Otherwise, this parameter
     can be set to any NDIS_STATUS_<i>XXX</i> except NDIS_STATUS_PENDING to indicate the client-determined reason for rejecting the
     call.</p>
</dd>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Specifies the handle to the VC that was created by the call manager to represent the incoming
     call. The client obtained this handle from it per-VC state designated by the 
     <i>ProtocolVcContext</i> passed as an input parameter to its 
     <a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">
     ProtocolClIncomingCall</a> function.</p>
</dd>

### -param <i>CallParameters</i> [in]

<dd>
<p>Pointer to a structure of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>, specifying the call
     parameters for the incoming call.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a client's 
    <a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">ProtocolClIncomingCall</a> function
    returns NDIS_STATUS_PENDING for an offered call incoming on a particular SAP, previously registered by
    the client with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561648">NdisClRegisterSap</a>, the client
    subsequently must call 
    <b>NdisClIncomingCallComplete</b> to indicate whether it is accepting or rejecting the offered call.</p>

<p>Before it calls 
    <b>NdisClIncomingCallComplete</b>, such a client can negotiate with the call manager by calling 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a> one or more times
    until both drivers reach an agreement on an acceptable quality of service for the incoming call or the
    client determines it should reject the offered call because its attempts to modify the QoS reach some
    client-determined limit without resulting in an agreement.</p>

<p>If the client has changed the call parameters passed in to its 
    <a href="https://msdn.microsoft.com/9143a8aa-56e0-40ad-aecb-19a10de64269">ProtocolClIncomingCall</a> function, it must set
    the 
    <b>Flags</b> member in the 
    <b>CO_CALL_PARAMETERS</b> structure with
    CALL_PARAMETERS_CHANGED when it passes these changes to 
    <b>NdisClIncomingCallComplete</b>. Depending on whether the call manager accepts or rejects the client's
    proposed changes to the call parameters, NDIS subsequently calls either the client's
    <a href="https://msdn.microsoft.com/675b2066-6a65-47cf-bde7-3c843f97c960">
    ProtocolClCallConnected</a> function or its 
    <a href="https://msdn.microsoft.com/01c7d887-eb54-47c3-98f0-bc567b60fb4b">
    ProtocolClIncomingCloseCall</a> function, respectively.</p>

<p>A call to 
    <b>NdisClIncomingCallComplete</b> causes NDIS to call the CM's 
    <a href="https://msdn.microsoft.com/353e929b-17c8-47e8-82fd-b646e93a5b9a">
    ProtocolCmIncomingCallComplete</a> function. NDIS passes the client-supplied parameters of 
    <b>NdisClIncomingCallComplete</b> as input parameters to 
    <i>ProtocolCmIncomingCallComplete</i>.</p>

<p>If a client rejects an offered call by setting 
    <i>Status</i> to something other than NDIS_STATUS_SUCCESS, the client must consider the 
    <i>CallParameters</i> pointer invalid as soon as its call to 
    <b>NdisClIncomingCallComplete</b> occurs.</p>

<p>If a client's 
    <a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">ProtocolClIncomingCall</a> function
    returns NDIS_STATUS_PENDING for an offered call incoming on a particular SAP, previously registered by
    the client with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561648">NdisClRegisterSap</a>, the client
    subsequently must call 
    <b>NdisClIncomingCallComplete</b> to indicate whether it is accepting or rejecting the offered call.</p>

<p>Before it calls 
    <b>NdisClIncomingCallComplete</b>, such a client can negotiate with the call manager by calling 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a> one or more times
    until both drivers reach an agreement on an acceptable quality of service for the incoming call or the
    client determines it should reject the offered call because its attempts to modify the QoS reach some
    client-determined limit without resulting in an agreement.</p>

<p>If the client has changed the call parameters passed in to its 
    <a href="https://msdn.microsoft.com/9143a8aa-56e0-40ad-aecb-19a10de64269">ProtocolClIncomingCall</a> function, it must set
    the 
    <b>Flags</b> member in the 
    <b>CO_CALL_PARAMETERS</b> structure with
    CALL_PARAMETERS_CHANGED when it passes these changes to 
    <b>NdisClIncomingCallComplete</b>. Depending on whether the call manager accepts or rejects the client's
    proposed changes to the call parameters, NDIS subsequently calls either the client's
    <a href="https://msdn.microsoft.com/675b2066-6a65-47cf-bde7-3c843f97c960">
    ProtocolClCallConnected</a> function or its 
    <a href="https://msdn.microsoft.com/01c7d887-eb54-47c3-98f0-bc567b60fb4b">
    ProtocolClIncomingCloseCall</a> function, respectively.</p>

<p>A call to 
    <b>NdisClIncomingCallComplete</b> causes NDIS to call the CM's 
    <a href="https://msdn.microsoft.com/353e929b-17c8-47e8-82fd-b646e93a5b9a">
    ProtocolCmIncomingCallComplete</a> function. NDIS passes the client-supplied parameters of 
    <b>NdisClIncomingCallComplete</b> as input parameters to 
    <i>ProtocolCmIncomingCallComplete</i>.</p>

<p>If a client rejects an offered call by setting 
    <i>Status</i> to something other than NDIS_STATUS_SUCCESS, the client must consider the 
    <i>CallParameters</i> pointer invalid as soon as its call to 
    <b>NdisClIncomingCallComplete</b> occurs.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/992f742f-c300-48bb-859a-fadf923e1be5">NdisClIncomingCallComplete
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisClIncomingCallComplete
   (NDIS 5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547996">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561648">NdisClRegisterSap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561664">NdisCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/675b2066-6a65-47cf-bde7-3c843f97c960">ProtocolClCallConnected</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">ProtocolClIncomingCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/01c7d887-eb54-47c3-98f0-bc567b60fb4b">ProtocolClIncomingCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/353e929b-17c8-47e8-82fd-b646e93a5b9a">
   ProtocolCmIncomingCallComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClIncomingCallComplete function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
