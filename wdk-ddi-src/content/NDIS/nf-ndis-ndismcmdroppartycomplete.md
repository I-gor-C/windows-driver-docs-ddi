---
UID: NF.ndis.NdisMCmDropPartyComplete
title: NdisMCmDropPartyComplete
author: windows-driver-content
description: NdisMCmDropPartyComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to remove a party from a multipoint VC.
old-location: netvista\ndismcmdroppartycomplete.htm
ms.assetid: ba0e11d9-3bb1-412c-9b33-9362d774adee
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMCmDropPartyComplete (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMCmDropPartyComplete (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmDropPartyComplete
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
ms.keywords: NdisMCmDropPartyComplete
req.iface: 
---

# NdisMCmDropPartyComplete function



## -description
<p><b>NdisMCmDropPartyComplete</b> returns the final status of a client's request, for which the MCM driver
  previously returned NDIS_STATUS_PENDING, to remove a party from a multipoint VC.</p>


## -syntax

````
VOID NdisMCmDropPartyComplete(
  _In_ NDIS_STATUS Status,
  _In_ NDIS_HANDLE NdisPartyHandle
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the requested operation, either NDIS_STATUS_SUCCESS or any
     caller-determined NDIS_STATUS_
     <i>XXX</i> except NDIS_STATUS_PENDING.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in]

<dd>
<p>Specifies the handle to the party that the client requested be dropped. The MCM driver obtained
     this handle from its per-party state area designated by 
     <i>CallMgrPartyContext</i> that was passed as an input parameter to its 
     <a href="https://msdn.microsoft.com/be0fce3e-7308-42fa-b63a-4d5cfec7ea6c">
     ProtocolCmDropParty</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>An MCM driver must call 
    <b>NdisMCmDropPartyComplete</b> if its 
    <i>ProtocolCmDropParty</i> function previously returned NDIS_STATUS_PENDING for the given 
    <i>NdisPartyHandle</i> . Neither NDIS nor the client, which initiated the pended drop-party operation with
    a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>, can release the
    resources they allocated to maintain per-party state until the MCM driver's call to 
    <b>NdisMCmDropPartyComplete</b> causes a call to that client's 
    <a href="https://msdn.microsoft.com/c916f379-393c-41d7-ab30-2f3181c3ada6">
    ProtocolClDropPartyComplete</a> function.</p>

<p>If it passes NDIS_STATUS_SUCCESS for the 
    <i>Status</i>, the MCM driver must consider the 
    <i>NdisPartyHandle</i> invalid when 
    <b>NdisMCmDropPartyComplete</b> returns control. The MCM driver can release (or reinitialize for reuse)
    any resources that it allocated to maintain state for this party after 
    <b>NdisMCmDropPartyComplete</b> returns control.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDropPartyComplete</b>. Stand-alone call managers, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCmDropPartyComplete</b> instead.</p>

<p>An MCM driver must call 
    <b>NdisMCmDropPartyComplete</b> if its 
    <i>ProtocolCmDropParty</i> function previously returned NDIS_STATUS_PENDING for the given 
    <i>NdisPartyHandle</i> . Neither NDIS nor the client, which initiated the pended drop-party operation with
    a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>, can release the
    resources they allocated to maintain per-party state until the MCM driver's call to 
    <b>NdisMCmDropPartyComplete</b> causes a call to that client's 
    <a href="https://msdn.microsoft.com/c916f379-393c-41d7-ab30-2f3181c3ada6">
    ProtocolClDropPartyComplete</a> function.</p>

<p>If it passes NDIS_STATUS_SUCCESS for the 
    <i>Status</i>, the MCM driver must consider the 
    <i>NdisPartyHandle</i> invalid when 
    <b>NdisMCmDropPartyComplete</b> returns control. The MCM driver can release (or reinitialize for reuse)
    any resources that it allocated to maintain state for this party after 
    <b>NdisMCmDropPartyComplete</b> returns control.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDropPartyComplete</b>. Stand-alone call managers, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCmDropPartyComplete</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/bfd74e96-2b71-4e33-ae8a-6141954e0c93">NdisMCmDropPartyComplete (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMCmDropPartyComplete (NDIS
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547967">Irql_MCM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561674">NdisCmDropPartyComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c916f379-393c-41d7-ab30-2f3181c3ada6">ProtocolClDropPartyComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/be0fce3e-7308-42fa-b63a-4d5cfec7ea6c">ProtocolCmDropParty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmDropPartyComplete function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
