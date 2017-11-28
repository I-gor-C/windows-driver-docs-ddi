---
UID: NF.ndis.NdisMCmCloseAddressFamilyComplete
title: NdisMCmCloseAddressFamilyComplete
author: windows-driver-content
description: NdisMCmCloseAddressFamilyComplete returns the final status of a client's request, for which the MCM driver returned NDIS_STATUS_PENDING, to close the AF.
old-location: netvista\ndismcmcloseaddressfamilycomplete.htm
old-project: netvista
ms.assetid: be551557-06db-4fc9-bdcb-030e621e205a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMCmCloseAddressFamilyComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   
   NdisMCmCloseAddressFamilyComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see
   
   
   NdisMCmCloseAddressFamilyComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmCloseAddressFamilyComplete
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

# NdisMCmCloseAddressFamilyComplete function



## -description
<p><b>NdisMCmCloseAddressFamilyComplete</b> returns the final status of a client's request, for which the MCM
  driver returned NDIS_STATUS_PENDING, to close the AF.</p>


## -syntax

````
VOID NdisMCmCloseAddressFamilyComplete(
  _In_ NDIS_STATUS Status,
  _In_ NDIS_HANDLE NdisAfHandle
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>The caller sets this to NDIS_STATUS_SUCCESS.</p>
</dd>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>Specifies the NDIS-supplied handle passed to the MCM driver's 
     <a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a> function when this
     client originally opened the address family.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>An MCM driver must call 
    <b>NdisMCmCloseAddressFamilyComplete</b> if its 
    <a href="..\ndis\nc-ndis-protocol-cm-close-af.md">ProtocolCmCloseAf</a> function previously
    returned NDIS_STATUS_PENDING for the given 
    <i>NdisAfHandle</i> . The client, which initiated the pended close-AF operation with a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561626">NdisClCloseAddressFamily</a>, cannot
    release the resources it allocated to track communications on the AF until the MCM driver's call to 
    <b>NdisMCmCloseAddressFamilyComplete</b>.</p>

<p>A call to 
    <b>NdisMCmCloseAddressFamilyComplete</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-close-af-complete.md">
    ProtocolClCloseAfComplete</a> function.</p>

<p>The MCM driver cannot subsequently use the 
    <i>NdisAfHandle</i>, which is invalid for the MCM driver when 
    <b>NdisMCmCloseAddressFamilyComplete</b> returns control.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmCloseAddressFamilyComplete</b>. Stand-alone call managers, which register themselves with NDIS
    as protocol drivers, call 
    <b>NdisCmCloseAddressFamilyComplete</b> instead.</p>

<p>An MCM driver must call 
    <b>NdisMCmCloseAddressFamilyComplete</b> if its 
    <a href="..\ndis\nc-ndis-protocol-cm-close-af.md">ProtocolCmCloseAf</a> function previously
    returned NDIS_STATUS_PENDING for the given 
    <i>NdisAfHandle</i> . The client, which initiated the pended close-AF operation with a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561626">NdisClCloseAddressFamily</a>, cannot
    release the resources it allocated to track communications on the AF until the MCM driver's call to 
    <b>NdisMCmCloseAddressFamilyComplete</b>.</p>

<p>A call to 
    <b>NdisMCmCloseAddressFamilyComplete</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-close-af-complete.md">
    ProtocolClCloseAfComplete</a> function.</p>

<p>The MCM driver cannot subsequently use the 
    <i>NdisAfHandle</i>, which is invalid for the MCM driver when 
    <b>NdisMCmCloseAddressFamilyComplete</b> returns control.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmCloseAddressFamilyComplete</b>. Stand-alone call managers, which register themselves with NDIS
    as protocol drivers, call 
    <b>NdisCmCloseAddressFamilyComplete</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/0399f140-c2df-4a1b-bb42-df5146df0123">
   NdisMCmCloseAddressFamilyComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see
   
   <b>
   NdisMCmCloseAddressFamilyComplete (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561626">NdisClCloseAddressFamily</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmcloseaddressfamilycomplete.md">
   NdisCmCloseAddressFamilyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-close-af-complete.md">ProtocolClCloseAfComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-close-af.md">ProtocolCmCloseAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmCloseAddressFamilyComplete function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
