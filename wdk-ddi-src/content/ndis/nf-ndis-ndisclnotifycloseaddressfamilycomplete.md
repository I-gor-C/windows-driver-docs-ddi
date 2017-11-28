---
UID: NF.ndis.NdisClNotifyCloseAddressFamilyComplete
title: NdisClNotifyCloseAddressFamilyComplete
author: windows-driver-content
description: The NdisClNotifyCloseAddressFamilyComplete function returns the final status of an address family (AF) close operation for which the caller's ProtocolClNotifyCloseAf function returned NDIS_STATUS_PENDING.
old-location: netvista\ndisclnotifycloseaddressfamilycomplete.htm
old-project: netvista
ms.assetid: 5d2bbf08-ea5c-4dad-8c30-9a655d25222a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisClNotifyCloseAddressFamilyComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClNotifyCloseAddressFamilyComplete
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
req.iface: 
---

# NdisClNotifyCloseAddressFamilyComplete function



## -description
<p>The 
  <b>NdisClNotifyCloseAddressFamilyComplete</b> function returns the final status of an address family (AF)
  close operation for which the caller's 
  <a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">ProtocolClNotifyCloseAf</a> function
  returned NDIS_STATUS_PENDING.</p>


## -syntax

````
VOID NdisClNotifyCloseAddressFamilyComplete(
  _In_ NDIS_HANDLE NdisAfHandle,
  _In_ NDIS_STATUS Status
);
````


## -parameters
<dl>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>An AF handle that NDIS supplied to the caller's 
     <a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">
     NdisClOpenAddressFamilyEx</a> function.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The completion status for close AF notification.
     </p>
<p><i>Status</i> can be one of the following:</p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The client successfully closed its address family.</p>
</dd>

### -param <a id="NDIS_STATUS_XXX"></a><a id="ndis_status_xxx"></a>NDIS_STATUS_<i>XXX</i>

<dd>
<p>The client failed the request for some driver-determined reason.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>CoNDIS clients call the 
    <b>NdisClNotifyCloseAddressFamilyComplete</b> function to complete a close AF notification. A client must
    call 
    <b>NdisClNotifyCloseAddressFamilyComplete</b> after its 
    <a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">
    ProtocolClNotifyCloseAf</a> function returns NDIS_STATUS_PENDING.</p>

<p>After the client calls 
    <b>NdisClNotifyCloseAddressFamilyComplete</b>, NDIS calls the call manager's 
    <a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
    ProtocolCmNotifyCloseAfComplete</a> function to complete operation for the call manager.</p>

<p>CoNDIS clients call the 
    <b>NdisClNotifyCloseAddressFamilyComplete</b> function to complete a close AF notification. A client must
    call 
    <b>NdisClNotifyCloseAddressFamilyComplete</b> after its 
    <a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">
    ProtocolClNotifyCloseAf</a> function returns NDIS_STATUS_PENDING.</p>

<p>After the client calls 
    <b>NdisClNotifyCloseAddressFamilyComplete</b>, NDIS calls the call manager's 
    <a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
    ProtocolCmNotifyCloseAfComplete</a> function to complete operation for the call manager.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">ProtocolClNotifyCloseAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
   ProtocolCmNotifyCloseAfComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClNotifyCloseAddressFamilyComplete function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
