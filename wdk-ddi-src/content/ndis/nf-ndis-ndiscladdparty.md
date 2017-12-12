---
UID: NF.ndis.NdisClAddParty
title: NdisClAddParty function
author: windows-driver-content
description: NdisClAddParty adds a party on the client's multipoint VC.
old-location: netvista\ndiscladdparty.htm
old-project: netvista
ms.assetid: e48357b2-52dc-48af-aeb1-8d84ea107579
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisClAddParty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisClAddParty (NDIS 5.1)) in   Windows Vista. Supported for NDIS 5.1 drivers (see    NdisClAddParty (NDIS 5.1)) in   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClAddParty
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
---

# NdisClAddParty function



## -description
<b>NdisClAddParty</b> adds a party on the client's multipoint VC.



## -syntax

````
NDIS_STATUS NdisClAddParty(
  _In_    NDIS_HANDLE         NdisVcHandle,
  _In_    NDIS_HANDLE         ProtocolPartyContext,
  _Inout_ PCO_CALL_PARAMETERS CallParameters,
  _Out_   PNDIS_HANDLE        NdisPartyHandle
);
````


## -parameters

### -param NdisVcHandle [in]

Pointer to the VC handle returned by 
     <a href="netvista.ndiscocreatevc">NdisCoCreateVc</a>.


### -param ProtocolPartyContext [in]

Specifies the handle to a caller-allocated resident context area in which the client will maintain
     per-party state if its call succeeds.


### -param CallParameters [in, out]

Pointer to a structure of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a> in which the caller has
     specified the addressing information for the party to be added on its multipoint VC.


### -param NdisPartyHandle [out]

Pointer to a variable to be set by NDIS if the add-party operation succeeds.


## -returns
When 
     <b>NdisClAddParty</b> returns anything other than NDIS_STATUS_PENDING, the client should make an internal
     call to its 
     <a href="..\ndis\nc-ndis-protocol_cl_add_party_complete.md">
     ProtocolClAddPartyComplete</a> function. Otherwise, NDIS calls the client's 
     <i>ProtocolClAddPartyComplete</i> function when this operation is completed.


## -remarks
Before it calls 
    <b>NdisClAddParty</b>, a client must set up a multipoint connection on its VC with 
    <a href="netvista.ndisclmakecall">NdisClMakeCall</a>, as well as allocating and
    initializing its context area for the party to be added. Clients commonly pass a pointer to such a
    context area as the 
    <i>ProtocolPartyContext</i> and a pointer to a variable within that context area as the 
    <i>NdisPartyHandle</i> parameters when they call 
    <b>NdisClAddParty</b>.

A call to 
    <b>NdisClAddParty</b> causes NDIS to forward this request to the 
    <a href="..\ndis\nc-ndis-protocol_cm_add_party.md">ProtocolCmAddParty</a> function of the
    call manager with which the client shares the given 
    <i>NdisVcHandle</i> . The call manager either returns an error status immediately or, more commonly,
    NDIS_STATUS_PENDING if it attempts to satisfy this request. If its attempt is rejected on the remote
    endpoint or by the underlying miniport driver, the call manager returns a final error status, such as
    NDIS_STATUS_FAILURE, when it calls 
    <a href="netvista.ndiscmaddpartycomplete">NdisCmAddPartyComplete</a> or 
    <a href="netvista.ndismcmaddpartycomplete">NdisMCmAddPartyComplete</a>. The
    client's 
    <a href="..\ndis\nc-ndis-protocol_cl_add_party_complete.md">
    ProtocolClAddPartyComplete</a> function should check the input 
    <i>Status</i> argument for NDIS_STATUS_SUCCESS before proceeding further.

The underlying network medium determines whether a client can specify per-party traffic parameters on
    a multipoint VC.

If the underlying network medium does not support per-party traffic parameters on multipoint VCs, a
    call manager can do one of the following whenever a client attempts to add a party with a specification
    at 
    <i>CallParameters</i> that does not match the already established traffic parameters for that VC:

Reject the request to add a new party.

Reset the traffic parameters to those already established for the multipoint VC when it successfully
      adds the party on that VC.

Change the traffic parameters for every party already on the VC when it successfully adds the new
      party.

If the add-party operation succeeds, the variable at 
    <i>NdisPartyHandle</i> has been set by NDIS to a valid handle shared among NDIS, the client, and the call
    manager. The client must treat this NDIS-supplied handle as an opaque variable to be passed, unmodified
    and uninterpreted, in subsequent calls to 
    <b>NdisCl/Co<i>Xxx</i></b> functions concerning the newly added party.

In turn, NDIS passes the client-supplied 
    <i>ProtocolPartyContext</i> handle in subsequent calls to the client's ProtocolCl<i>Xxx</i> functions that concern this newly added party, including the call to 
    <a href="..\ndis\nc-ndis-protocol_cl_add_party_complete.md">
    ProtocolClAddPartyComplete</a>.

Whether a multipoint call permits transfers in both directions and/or per-party transfers with
    per-party traffic parameters depends on the medium of the underlying miniport driver to which the client
    is bound. The 
    <i>NdisPartyHandle</i> represents only the specific party added by a successful call to 
    <b>NdisClAddParty</b>, rather than the multipoint VC. Consequently, the client can use its 
    <i>ProtocolPartyContext</i> area only for subsequent party-specific call-management requests. For data
    transfers over network media that do not support per-party transfers or traffic parameters, the client
    must use the 
    <i>NdisVcHandle</i> instead.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff550843">NdisClAddParty (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisClAddParty (NDIS 5.1)</b>) in
   Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_protocol_driver_function">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndisallocatefromnpagedlookasidelist">
   NdisAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="netvista.ndisclclosecall">NdisClCloseCall</a>
</dt>
<dt>
<a href="netvista.ndisclmakecall">NdisClMakeCall</a>
</dt>
<dt>
<a href="netvista.ndiscldropparty">NdisClDropParty</a>
</dt>
<dt>
<a href="netvista.ndiscmaddpartycomplete">NdisCmAddPartyComplete</a>
</dt>
<dt>
<a href="netvista.ndiscocreatevc">NdisCoCreateVc</a>
</dt>
<dt>
<a href="netvista.ndiscooidrequest">NdisCoOidRequest</a>
</dt>
<dt>
<a href="netvista.ndiscooidrequestcomplete">NdisCoOidRequestComplete</a>
</dt>
<dt>
<a href="netvista.ndismcmaddpartycomplete">NdisMCmAddPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_add_party_complete.md">ProtocolClAddPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cm_add_party.md">ProtocolCmAddParty</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClAddParty function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

