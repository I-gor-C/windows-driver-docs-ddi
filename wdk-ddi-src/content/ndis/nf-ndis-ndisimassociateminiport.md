---
UID: NF.ndis.NdisIMAssociateMiniport
title: NdisIMAssociateMiniport
author: windows-driver-content
description: The NdisIMAssociateMiniport function informs NDIS that the specified lower and upper interfaces for miniport and protocol drivers respectively belong to the same intermediate driver.
old-location: netvista\ndisimassociateminiport.htm
old-project: netvista
ms.assetid: b2c46419-644b-4ad4-aa50-7c6e541638aa
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisIMAssociateMiniport
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisIMAssociateMiniport (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisIMAssociateMiniport (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIMAssociateMiniport
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_IM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisIMAssociateMiniport function



## -description
<p>The
  <b>NdisIMAssociateMiniport</b> function informs NDIS that the specified lower and upper interfaces for
  miniport and protocol drivers respectively belong to the same intermediate driver.</p>


## -syntax

````
VOID NdisIMAssociateMiniport(
  _In_ NDIS_HANDLE DriverHandle,
  _In_ NDIS_HANDLE ProtocolHandle
);
````


## -parameters
<dl>

### -param <i>DriverHandle</i> [in]

<dd>
<p>The handle to the miniport driver interface that the 
     <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
     NdisMRegisterMiniportDriver</a> function returns.</p>
</dd>

### -param <i>ProtocolHandle</i> [in]

<dd>
<p>The handle to the protocol interface that the 
     <a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">
     NdisRegisterProtocolDriver</a> function returns.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Any NDIS intermediate driver that exports both 
    <i>MiniportXxx</i> and 
    <i>ProtocolXxx</i> functions calls 
    <b>NdisIMAssociateMiniport</b> to inform the NDIS library about its miniport upper edge and its protocol
    lower edge. Such an intermediate driver calls 
    <b>NdisIMAssociateMiniport</b> during its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. For more information about 
    <b>DriverEntry</b>, see 
    <a href="netvista.driverentry_of_ndis_intermediate_drivers">DriverEntry of NDIS
    Intermediate Drivers</a>.</p>

<p>Any NDIS intermediate driver that exports both 
    <i>MiniportXxx</i> and 
    <i>ProtocolXxx</i> functions calls 
    <b>NdisIMAssociateMiniport</b> to inform the NDIS library about its miniport upper edge and its protocol
    lower edge. Such an intermediate driver calls 
    <b>NdisIMAssociateMiniport</b> during its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. For more information about 
    <b>DriverEntry</b>, see 
    <a href="netvista.driverentry_of_ndis_intermediate_drivers">DriverEntry of NDIS
    Intermediate Drivers</a>.</p>

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
   <a href="https://msdn.microsoft.com/5c271865-3cc5-47ad-ab58-b5260056a698">NdisIMAssociateMiniport (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisIMAssociateMiniport (NDIS
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547941">Irql_IM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564520">NdisRegisterProtocolDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIMAssociateMiniport function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
