---
UID: NF.ndis.NdisMCmAddPartyComplete
title: NdisMCmAddPartyComplete
author: windows-driver-content
description: NdisMCmAddPartyComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to add a party on an established multipoint VC.
old-location: netvista\ndismcmaddpartycomplete.htm
old-project: netvista
ms.assetid: 5bbcd552-00c2-4085-8222-c514eb92e654
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMCmAddPartyComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCmAddPartyComplete (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCmAddPartyComplete (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmAddPartyComplete
req.alt-loc: ndis.h
req.ddi-compliance: Irql_MCM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisMCmAddPartyComplete function



## -description
<p><b>NdisMCmAddPartyComplete</b> returns the final status of a client's request, for which the MCM driver
  previously returned NDIS_STATUS_PENDING, to add a party on an established multipoint VC.</p>


## -syntax

````
VOID NdisMCmAddPartyComplete(
  _In_     NDIS_STATUS         Status,
  _In_     NDIS_HANDLE         NdisPartyHandle,
  _In_opt_ NDIS_HANDLE         CallMgrPartyContext,
  _In_     PCO_CALL_PARAMETERS CallParameters
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the MCM driver's add-party operation, either NDIS_STATUS_SUCCESS or
     any NDIS_STATUS_<i>XXX</i><u>except</u> NDIS_STATUS_PENDING.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in]

<dd>
<p>Specifies the handle identifying the party. The MCM driver obtained this handle as input parameter
     to its 
     <a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a> function.</p>
</dd>

### -param <i>CallMgrPartyContext</i> [in, optional]

<dd>
<p>Specifies the handle to a caller-allocated resident context area in which the MCM driver will
     maintain party-specific state information if the add-party operation succeeded. Otherwise, this
     parameter can be <b>NULL</b> because it is ignored by NDIS if 
     <i>Status</i> is anything other than NDIS_STATUS_SUCCESS.</p>
</dd>

### -param <i>CallParameters</i> [in]

<dd>
<p>Pointer to a structure of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a> that contains the call
     parameters, originally supplied by the client, for the party to be added.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If an MCM driver's 
    <a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a> function returns
    NDIS_STATUS_PENDING, the driver must call 
    <b>NdisMCmAddPartyComplete</b> subsequently to notify the client and NDIS that its attempt to add a party
    on the multipoint VC has completed, whether successfully or with an MCM driver-determined error
    status.</p>

<p>The underlying network medium determines whether a client can specify per-party traffic parameters on
    a multipoint VC.</p>

<p>If the underlying network medium does not support per-party traffic parameters on multipoint VCs, an
    MCM driver can do one of the following whenever a client attempts to add a party with a specification at 
    <i>CallParameters</i> that does not match the already established traffic parameters for that VC:</p>

<p>Reset the traffic parameters to those already established for the multipoint VC when it successfully
      adds the party on that VC.</p>

<p>Change the traffic parameters for every party already on the VC when it successfully adds the new
      party.</p>

<p>Reject the request to add a new party. (This alternative implicitly forces clients to set up their
      traffic parameters for a multipoint VC with 
      <a href="..\ndis\nf-ndis-ndisclmakecall.md">NdisClMakeCall</a> and to specify the same
      traffic parameters at each subsequent call to 
      <a href="..\ndis\nf-ndis-ndiscladdparty.md">NdisClAddParty</a> for the given multipoint
      VC.)</p>

<p>If the MCM driver sets 
    <i>Status</i> to NDIS_STATUS_SUCCESS, it must supply an explicit handle, which is usually a pointer to the
    driver-allocated per-party state area, as 
    <i>CallMgrPartyContext</i> when it calls 
    <b>NdisMCmAddPartyComplete</b>.</p>

<p>A call to 
    <b>NdisMCmAddPartyComplete</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-add-party-complete.md">
    ProtocolClAddPartyComplete</a> function.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmAddPartyComplete</b>. Stand-alone call managers, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCmAddPartyComplete</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/e7fa7259-fde3-4dcd-b876-0c10876045f5">NdisMCmAddPartyComplete (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMCmAddPartyComplete (NDIS
   5.1)</b>) in Windows XP.</p>
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
<a href="devtest.ndis_irql_mcm_function">Irql_MCM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatefromnpagedlookasidelist.md">
   NdisAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscladdparty.md">NdisClAddParty</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmaddpartycomplete.md">NdisCmAddPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmdroppartycomplete.md">NdisMCmDropPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-add-party-complete.md">ProtocolClAddPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmAddPartyComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
