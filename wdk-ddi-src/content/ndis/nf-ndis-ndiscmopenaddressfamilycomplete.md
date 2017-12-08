---
UID: NF.ndis.NdisCmOpenAddressFamilyComplete
title: NdisCmOpenAddressFamilyComplete function
author: windows-driver-content
description: NdisCmOpenAddressFamilyComplete returns the final status of a stand-alone call manager's open of a given AF for a particular client after the call manager returned NDIS_STATUS_PENDING in response to that client's original open-AF request.
old-location: netvista\ndiscmopenaddressfamilycomplete.htm
old-project: netvista
ms.assetid: eed57341-0b1a-4697-b05d-680bc17da796
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisCmOpenAddressFamilyComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisCmOpenAddressFamilyComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisCmOpenAddressFamilyComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCmOpenAddressFamilyComplete
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
---

# NdisCmOpenAddressFamilyComplete function



## -description
<b>NdisCmOpenAddressFamilyComplete</b> returns the final status of a stand-alone call manager's open of a
  given AF for a particular client after the call manager returned NDIS_STATUS_PENDING in response to that
  client's original open-AF request.


## -syntax

````
VOID NdisCmOpenAddressFamilyComplete(
  _In_ NDIS_STATUS Status,
  _In_ NDIS_HANDLE NdisAfHandle,
  _In_ NDIS_HANDLE CallMgrAfContext
);
````


## -parameters

### -param Status [in]

Specifies the final status of the open-AF operation, either NDIS_STATUS_SUCCESS or any
     CM-determined error NDIS_STATUS_
     <i>XXX</i> except NDIS_STATUS_PENDING.

### -param NdisAfHandle [in]

Specifies the NDIS-supplied handle that was input to the call manager's 
     <a href="..\ndis\nc-ndis-protocol_cm_open_af.md">ProtocolCmOpenAf</a> function, which
     returned NDIS_STATUS_PENDING.

### -param CallMgrAfContext [in]

Specifies the handle to a caller-allocated resident context area in which the call manager
     maintains state about this client's open of the address family, including the 
     <i>NdisAfHandle</i>, if the open succeeded. If 
     <i>Status</i> is not NDIS_STATUS_SUCCESS, NDIS ignores this parameter.

## -returns
None

## -remarks
A stand-alone call manager must call 
    <b>NdisCmOpenAddressFamilyComplete</b> if its 
    <a href="..\ndis\nc-ndis-protocol_cm_open_af.md">ProtocolCmOpenAf</a> function previously
    returned NDIS_STATUS_PENDING for the given 
    <i>NdisAfHandle</i> . The client, which initiated the pended open-AF operation with a call to 
    <a href="netvista.ndisclopenaddressfamilyex">NdisClOpenAddressFamilyEx</a>,
    cannot carry out further connection-oriented operations on the same binding until 
    <b>NdisCmOpenAddressFamilyComplete</b> causes a call to that client's 
    <a href="..\ndis\nc-ndis-protocol_cl_open_af_complete_ex.md">
    ProtocolClOpenAfCompleteEx</a> function.

If the caller of 
    <b>NdisCmOpenAddressFamilyComplete</b> sets 
    <i>Status</i> to NDIS_STATUS_SUCCESS, NDIS subsequently passes the given 
    <i>CallMgrAfContext</i> handle as an input parameter to all CM-supplied ProtocolCm<i>Xxx</i> and ProtocolCo<i>Xxx</i> functions that concern the client's open of the address family until the client closes the AF.
    The call manager should release or reuse any AF context area that it allocated before it passes a failure
    status to 
    <b>NdisCmOpenAddressFamilyComplete</b>.

For a successful open, the NDIS-supplied 
    <i>NdisAfHandle</i> represents an association between the call manager and client for the opened AF on a
    particular miniport driver to which the call manager and client are bound. Both protocol drivers must
    treat 
    <i>NdisAfHandle</i> as an opaque variable to be passed, unmodified and uninterpreted, in subsequent calls
    to NdisCl/Cm/CoXxx functions for which this handle is a required parameter. For a failed open, the call
    manager should consider the 
    <i>NdisAfHandle</i> invalid when 
    <b>NdisMCmOpenAddressFamilyComplete</b> returns control.

Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmOpenAddressFamilyComplete</b>. Connection-oriented miniport drivers that provide integrated
    call-management support must call 
    <a href="netvista.ndismcmopenaddressfamilycomplete">
    NdisMCmOpenAddressFamilyComplete</a> instead.

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
   <a href="https://msdn.microsoft.com/77680fd1-94f2-41f7-a926-061c652f3a3e">
   NdisCmOpenAddressFamilyComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisCmOpenAddressFamilyComplete (NDIS 5.1)</b>) in Windows XP.
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
<a href="devtest.ndis_irql_callmanager_function">Irql_CallManager_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisallocatefromnpagedlookasidelist">
   NdisAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="netvista.ndisclopenaddressfamilyex">NdisClOpenAddressFamilyEx</a>
</dt>
<dt>
<a href="netvista.ndismcmopenaddressfamilycomplete">
   NdisMCmOpenAddressFamilyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_open_af_complete_ex.md">ProtocolClOpenAfCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cm_open_af.md">ProtocolCmOpenAf</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCmOpenAddressFamilyComplete function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>