---
UID: NF.ndis.NdisCmAddPartyComplete
title: NdisCmAddPartyComplete
author: windows-driver-content
description: NdisCmAddPartyComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to add a party on an established multipoint VC.
old-location: netvista\ndiscmaddpartycomplete.htm
old-project: netvista
ms.assetid: 00833038-1fff-4103-9508-07cb8cbfa846
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisCmAddPartyComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisCmAddPartyComplete (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisCmAddPartyComplete (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCmAddPartyComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_CallManager_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisCmAddPartyComplete function



## -description
<p><b>NdisCmAddPartyComplete</b> returns the final status of a client's request, for which the call manager
  previously returned NDIS_STATUS_PENDING, to add a party on an established multipoint VC.</p>


## -syntax

````
VOID NdisCmAddPartyComplete(
  _In_     NDIS_STATUS         Status,
  _In_     NDIS_HANDLE         NdisPartyHandle,
  _In_opt_ NDIS_HANDLE         CallMgrPartyContext,
  _In_     PCO_CALL_PARAMETERS CallParameters
);
````


## -parameters
<dl>

### -param Status [in]

<dd>
<p>Specifies the final status of the call manager's add-party operation, either NDIS_STATUS_SUCCESS
     or any NDIS_STATUS_<i>XXX</i> except NDIS_STATUS_PENDING.</p>
</dd>

### -param NdisPartyHandle [in]

<dd>
<p>Specifies the handle identifying the party. This handle was input to the call manager's 
     <a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a> function.</p>
</dd>

### -param CallMgrPartyContext [in, optional]

<dd>
<p>Specifies the handle to a caller-allocated resident context area in which the call manager will
     maintain party-specific state information if the add-party operation succeeded. Otherwise, this
     parameter can be <b>NULL</b> because it is ignored.</p>
</dd>

### -param CallParameters [in]

<dd>
<p>Pointer to a structure of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a> that contains the call
     parameters, originally supplied by the client, for the party to be added.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a stand-alone call manager's 
    <a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a> function returns
    NDIS_STATUS_PENDING, the CM subsequently must call 
    <b>NdisCmAddPartyComplete</b> to notify the client and NDIS that its attempt to add a party on the
    multipoint VC has completed, whether successfully or with an error.</p>

<p>If the client passed in traffic parameters at 
    <i>CallParameters</i> that did not match those already established for the multipoint VC, the designer of
    the call manager must determine how to handle this condition, subject to any constraints imposed by the
    network medium. Possibilities include the following:</p>

<p>Set up the per-party traffic parameters if the underlying network medium supports this feature on
      multipoint VCs.</p>

<p>Reset the client-supplied traffic parameters to those established for the VC when the original
      outgoing call was made before the CM calls 
      <b>NdisCmAddPartyComplete</b> with NDIS_STATUS_SUCCESS as the 
      <i>Status</i> .</p>

<p>Change the traffic parameters for the VC and, for every party currently connected on it, to the
      client-supplied values before the CM calls 
      <b>NdisCmAddPartyComplete</b> with NDIS_STATUS_SUCCESS as the 
      <i>Status</i> .</p>

<p>Fail the client's attempt to add a party. (This alternative implicitly forces clients to set up
      their traffic parameters for a multipoint VC with 
      <a href="..\ndis\nf-ndis-ndisclmakecall.md">NdisClMakeCall</a> and to specify the same
      traffic parameters at each subsequent call to 
      <a href="..\ndis\nf-ndis-ndiscladdparty.md">NdisClAddParty</a> for the given multipoint
      VC.)</p>

<p>For some connection-oriented media , traffic parameters are per-VC in nature and, consequently,
    identical for all parties on a multipoint VC.</p>

<p>If the CM sets 
    <i>Status</i> to NDIS_STATUS_SUCCESS, it must supply an explicit handle, which is usually a pointer to the
    CM-allocated per-party state area, as 
    <i>CallMgrPartyContext</i> when it calls 
    <b>NdisCmAddPartyComplete</b>.</p>

<p>A call to 
    <b>NdisCmAddPartyComplete</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-add-party-complete.md">
    ProtocolClAddPartyComplete</a> function.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmAddPartyComplete</b>. Connection-oriented miniport drivers that provide integrated
    call-management support call 
    <b>NdisMCmAddPartyComplete</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/4a16b1bf-baac-4fa6-b0a8-60da7780e0a1">NdisCmAddPartyComplete (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisCmAddPartyComplete (NDIS
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
<a href="devtest.ndis_irql_callmanager_function">Irql_CallManager_Function</a>
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
<a href="..\ndis\nf-ndis-ndismcmaddpartycomplete.md">NdisMCmAddPartyComplete</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCmAddPartyComplete function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
