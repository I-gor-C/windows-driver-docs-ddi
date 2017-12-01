---
UID: NF.ndis.NdisMCmOpenAddressFamilyComplete
title: NdisMCmOpenAddressFamilyComplete
author: windows-driver-content
description: NdisMCmOpenAddressFamilyComplete returns the final status of a client's request, for which the MCM driver's ProtocolCmOpenAf function returned NDIS_STATUS_PENDING, to open the MCM driver's address family.
old-location: netvista\ndismcmopenaddressfamilycomplete.htm
old-project: netvista
ms.assetid: e2d6c7db-09b3-4e5a-a6da-607c67e03054
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMCmOpenAddressFamilyComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisMCmOpenAddressFamilyComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisMCmOpenAddressFamilyComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmOpenAddressFamilyComplete
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

# NdisMCmOpenAddressFamilyComplete function



## -description
<p><b>NdisMCmOpenAddressFamilyComplete</b> returns the final status of a client's request, for which the MCM
  driver's 
  <a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a> function returned
  NDIS_STATUS_PENDING, to open the MCM driver's address family.</p>


## -syntax

````
VOID NdisMCmOpenAddressFamilyComplete(
  _In_ NDIS_STATUS Status,
  _In_ NDIS_HANDLE NdisAfHandle,
  _In_ NDIS_HANDLE CallMgrAfContext
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the client's request to open the AF, either NDIS_STATUS_SUCCESS or
     any caller-determined NDIS_STATUS_
     <i>XXX</i> except NDIS_STATUS_PENDING.</p>
</dd>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>Specifies the NDIS-supplied handle that was input to the MCM driver's 
     <i>ProtocolCmOpenAf</i> function, which returned NDIS_STATUS_PENDING.</p>
</dd>

### -param <i>CallMgrAfContext</i> [in]

<dd>
<p>Specifies the handle to a caller-allocated resident context area, in which the MCM driver
     maintains state about this client's open of the address family, including the 
     <i>NdisAfHandle</i>, if the open succeeded. Otherwise, NDIS ignores this parameter.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>An MCM driver must call 
    <b>NdisMCmOpenAddressFamilyComplete</b> if its 
    <a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a> function previously
    returned NDIS_STATUS_PENDING for the given 
    <i>NdisAfHandle</i> . The client, which initiated the pended open-AF operation with a call to 
    <a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">NdisClOpenAddressFamilyEx</a>,
    cannot carry out further connection-oriented operations on the same binding until 
    <b>NdisMCmOpenAddressFamilyComplete</b> causes a call to that client's 
    <a href="..\ndis\nc-ndis-protocol-cl-open-af-complete-ex.md">
    ProtocolClOpenAfCompleteEx</a> function.</p>

<p>If the caller of 
    <b>NdisMCmOpenAddressFamilyComplete</b> sets 
    <i>Status</i> to NDIS_STATUS_SUCCESS, NDIS subsequently passes the given 
    <i>CallMgrAfContext</i> handle as an input parameter to all MCM driver-supplied ProtocolCm<i>Xxx</i> and ProtocolCo<i>Xxx</i> functions that concern the client's open of the address family until the client closes the AF.
    The MCM driver should release or reuse any AF context area that it allocated before it passes a failure
    status to 
    <b>NdisMCmOpenAddressFamilyComplete</b>.</p>

<p>For a successful open, the NDIS-supplied 
    <i>NdisAfHandle</i> represents an association between the MCM driver and client for the opened AF. Both
    NDIS drivers must treat 
    <i>NdisAfHandle</i> as an opaque variable to be passed, unmodified and uninterpreted, in subsequent calls
    to NdisCl/Co/MCm/MCoXxx functions for which this handle is a required parameter. For a failed open, the
    MCM driver should consider the 
    <i>NdisAfHandle</i> invalid when 
    <b>NdisMCmOpenAddressFamilyComplete</b> returns control.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmOpenAddressFamilyComplete</b>. Stand-alone call managers, which register themselves with NDIS
    as protocol drivers, call 
    <b>NdisCmOpenAddressFamilyComplete</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/785e5a8b-9524-4ae1-99cc-b53f296a6341">
   NdisMCmOpenAddressFamilyComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisMCmOpenAddressFamilyComplete (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="..\ndis\nf-ndis-ndisallocatefromnpagedlookasidelist.md">
   NdisAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">NdisClOpenAddressFamilyEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmopenaddressfamilycomplete.md">
   NdisCmOpenAddressFamilyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-open-af-complete-ex.md">ProtocolClOpenAfCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmOpenAddressFamilyComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
