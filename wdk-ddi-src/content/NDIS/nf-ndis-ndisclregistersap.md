---
UID: NF.ndis.NdisClRegisterSap
title: NdisClRegisterSap
author: windows-driver-content
description: NdisClRegisterSap registers a SAP on which the client can receive incoming calls from a remote node.
old-location: netvista\ndisclregistersap.htm
ms.assetid: 33ed0839-d1e3-4872-baa8-ead7e97f8c53
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisClRegisterSap (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisClRegisterSap (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClRegisterSap
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
ms.keywords: NdisClRegisterSap
req.iface: 
---

# NdisClRegisterSap function



## -description
<p><b>NdisClRegisterSap</b> registers a SAP on which the client can receive incoming calls from a remote
  node.</p>


## -syntax

````
NDIS_STATUS NdisClRegisterSap(
  _In_  NDIS_HANDLE  NdisAfHandle,
  _In_  NDIS_HANDLE  ProtocolSapContext,
  _In_  PCO_SAP      Sap,
  _Out_ PNDIS_HANDLE NdisSapHandle
);
````


## -parameters
<dl>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>Specifies the handle returned by 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a>,
     which implicitly identifies the call manager with which to register the SAP.</p>
</dd>

### -param <i>ProtocolSapContext</i> [in]

<dd>
<p>Specifies the handle to a caller-supplied resident context area in which the client maintains
     state for this SAP after it has been opened. NDIS passes this handle back to the client in all
     subsequent calls concerning this SAP if the call to 
     <b>NdisClRegisterSap</b> succeeds.</p>
</dd>

### -param <i>Sap</i> [in]

<dd>
<p>Pointer to a client-supplied specification for the SAP to be opened, formatted as a structure of
     type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545392">CO_SAP</a>.</p>
</dd>

### -param <i>NdisSapHandle</i> [out]

<dd>
<p>Pointer to a variable in which a handle to the newly registered SAP is returned if this call
     succeeds.</p>
</dd>
</dl>

## -returns
<p>When 
     <b>NdisClRegisterSap</b> returns anything other than NDIS_STATUS_PENDING, the client should make an
     internal call to its 
     <a href="https://msdn.microsoft.com/b0a2a224-3353-4f20-b14f-ed5d633a6ead">
     ProtocolClRegisterSapComplete</a> function. Otherwise, NDIS calls the client's 
     <i>ProtocolClRegisterSapComplete</i> function when this operation is completed.</p>

## -remarks
<p>With a call to 
    <b>NdisClRegisterSap</b>, a client requests notifications of incoming calls on a particular SAP. NDIS
    forwards the given SAP information to the call manager's 
    <a href="https://msdn.microsoft.com/3e3e7a0e-a8d2-40b2-895b-187d24867080">ProtocolCmRegisterSap</a> function
    for validation. If the given SAP is already in use or if the call manager does not recognize the
    client-supplied specification at 
    <i>Sap</i>, the call manager fails this request.</p>

<p>SAP format is medium-dependent and specific to the address family supported by the call manager, which
    uses registered SAPs subsequently to route incoming calls to the appropriate client. A call manager can
    register SAPs for established PVCs without contacting other network components, depending on the
    underlying medium.</p>

<p>If its call to 
    <b>NdisClRegisterSap</b> succeeds, the client must save the handle returned at 
    <i>NdisSapHandle</i> because it is a required parameter to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561628">NdisClDeregisterSap</a>. Callers of 
    <b>NdisClRegisterSap</b> usually pass a pointer to a variable in the client-allocated state area at 
    <i>ProtocolSapContext</i> so that NDIS can set it to the 
    <i>NdisSapHandle</i> if this call succeeds. NDIS passes the given 
    <i>ProtocolSapContext</i> to the client's registered ProtocolCl/Co<i>Xxx</i> functions in all subsequent calls concerning this SAP until the client calls 
    <b>NdisClDeregisterSap</b>.</p>

<p>Usually, a client calls 
    <b>NdisClRegisterSap</b> from its 
    <i>ProtocolAfRegisterNotify</i> function following its successful call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a>.
    Registering one or more SAPs allows the client to receive its incoming call(s) as soon as the call
    manager receives them over the network.</p>

<p>By contrast with client-initiated outgoing calls, a client does not call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> before it calls 
    <b>NdisClRegisterSap</b>. For incoming calls, the call manager initiates the creation of the VC, as
    follows:</p>

<p>On receipt of an incoming call on a registered SAP, the call manager first calls 
      <b>NdisCoCreateVc</b>, causing NDIS to call the client's 
      <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> function.</p>

<p>When the VC has been set up and activated, the call manager calls 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561664">NdisCmDispatchIncomingCall</a>,
      causing NDIS to call the client's 
      <a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">
      ProtocolClIncomingCall</a> function.</p>

<p>With a call to 
    <b>NdisClRegisterSap</b>, a client requests notifications of incoming calls on a particular SAP. NDIS
    forwards the given SAP information to the call manager's 
    <a href="https://msdn.microsoft.com/3e3e7a0e-a8d2-40b2-895b-187d24867080">ProtocolCmRegisterSap</a> function
    for validation. If the given SAP is already in use or if the call manager does not recognize the
    client-supplied specification at 
    <i>Sap</i>, the call manager fails this request.</p>

<p>SAP format is medium-dependent and specific to the address family supported by the call manager, which
    uses registered SAPs subsequently to route incoming calls to the appropriate client. A call manager can
    register SAPs for established PVCs without contacting other network components, depending on the
    underlying medium.</p>

<p>If its call to 
    <b>NdisClRegisterSap</b> succeeds, the client must save the handle returned at 
    <i>NdisSapHandle</i> because it is a required parameter to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561628">NdisClDeregisterSap</a>. Callers of 
    <b>NdisClRegisterSap</b> usually pass a pointer to a variable in the client-allocated state area at 
    <i>ProtocolSapContext</i> so that NDIS can set it to the 
    <i>NdisSapHandle</i> if this call succeeds. NDIS passes the given 
    <i>ProtocolSapContext</i> to the client's registered ProtocolCl/Co<i>Xxx</i> functions in all subsequent calls concerning this SAP until the client calls 
    <b>NdisClDeregisterSap</b>.</p>

<p>Usually, a client calls 
    <b>NdisClRegisterSap</b> from its 
    <i>ProtocolAfRegisterNotify</i> function following its successful call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a>.
    Registering one or more SAPs allows the client to receive its incoming call(s) as soon as the call
    manager receives them over the network.</p>

<p>By contrast with client-initiated outgoing calls, a client does not call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> before it calls 
    <b>NdisClRegisterSap</b>. For incoming calls, the call manager initiates the creation of the VC, as
    follows:</p>

<p>On receipt of an incoming call on a registered SAP, the call manager first calls 
      <b>NdisCoCreateVc</b>, causing NDIS to call the client's 
      <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> function.</p>

<p>When the VC has been set up and activated, the call manager calls 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561664">NdisCmDispatchIncomingCall</a>,
      causing NDIS to call the client's 
      <a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">
      ProtocolClIncomingCall</a> function.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff550916">NdisClRegisterSap (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisClRegisterSap (NDIS 5.1)</b>) in
   Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545392">CO_SAP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561628">NdisClDeregisterSap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561664">NdisCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8a5922ac-b22b-444e-9ea0-3bb56e71ef33">ProtocolClIncomingCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b0a2a224-3353-4f20-b14f-ed5d633a6ead">
   ProtocolClRegisterSapComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3e3e7a0e-a8d2-40b2-895b-187d24867080">ProtocolCmRegisterSap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/272d99da-ef08-4ebd-90e7-74e99410b3f5">ProtocolCoAfRegisterNotify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClRegisterSap function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
