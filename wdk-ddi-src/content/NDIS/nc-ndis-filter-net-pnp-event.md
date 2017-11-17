---
UID: NC.ndis.FILTER_NET_PNP_EVENT
title: FILTER_NET_PNP_EVENT
author: windows-driver-content
description: NDIS calls a filter driver's FilterNetPnPEvent function to notify the driver of network Plug and Play (PnP) and Power Management events.Note  You must declare the function by using the FILTER_NET_PNP_EVENT type.
old-location: netvista\filternetpnpevent.htm
ms.assetid: 5c52b2d2-3fba-4d28-8172-7b6854386061
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FilterNetPnPEvent
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# FILTER_NET_PNP_EVENT callback



## -description
<p>NDIS calls a filter driver's 
  <i>FilterNetPnPEvent</i> function to notify the driver of network Plug and Play (PnP)
  and Power Management events.</p>


## -prototype

````
FILTER_NET_PNP_EVENT FilterNetPnPEvent;

NDIS_STATUS FilterNetPnPEvent(
  _In_ NDIS_HANDLE                 FilterModuleContext,
  _In_ PNET_PNP_EVENT_NOTIFICATION NetPnPEvent
)
{ ... }
````


## -parameters
<dl>

### -param <i>FilterModuleContext</i> [in]

<dd>
<p>A handle to the context area for the filter module. The filter driver created and initialized this
     context area in the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -param <i>NetPnPEvent</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/58d3baf3-a1fa-42ae-b795-2774a148aeda">
     NET_PNP_EVENT_NOTIFICATION</a> structure, which describes the PnP event or Power Management event
     being indicated to the filter driver.</p>
</dd>
</dl>

## -returns
<p><i>FilterNetPnPEvent</i> can return either of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The driver successfully processed the PnP event.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The driver failed the PnP event.</p>

<p> </p>

<p>The return value is significant only when the propagated event is a 
     <b>NetEventQueryPower</b> or a 
     <b>NetEventQueryRemove</b> event. For all other propagated events, the return
     value is always NDIS_STATUS_SUCCESS.</p>

## -remarks
<p><i>FilterNetPnPEvent</i> is an optional function. If a filter driver does not handle
    network PnP events, it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="https://msdn.microsoft.com/14381de2-36d9-4ec8-9d4e-7af3e6d8ecf3">
    NdisFRegisterFilterDriver</a> function.</p>

<p><i>FilterNetPnPEvent</i> is similar to a protocol driver's 
    <a href="https://msdn.microsoft.com/3f50bcba-c7d2-4d81-bd8b-6080e08fbe74">ProtocolNetPnPEvent</a> function. A
    filter driver can forward these notifications to overlying drivers or it can handle them itself and not
    forward them. To forward a notification, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561828">NdisFNetPnPEvent</a> function. Do not confuse
    this function with the 
    <a href="https://msdn.microsoft.com/dea4ab30-ba1d-4c9c-9f00-e48cc3cc0b46">
    FilterDevicePnPEventNotify</a> function, which filters notifications that are directed down the stack
    to underlying drivers.</p>

<p>NDIS calls 
    <i>FilterNetPnPEvent</i> to notify a filter driver of a PnP or Power Management event
    that was issued for an underlying NIC. NDIS calls the 
    <i>FilterNetPnPEvent</i> function of each filter driver overlying a NIC, and then
    calls the 
    <i>ProtocolNetPnPEvent</i> function of each overlying protocol driver.</p>

<p>When a filter module is inserted into or deleted from a driver stack, the characteristics of the stack
    might change. NDIS sends a PnP event to all affected protocol bindings and filter modules to notify them
    about this change. Filter drivers should handle such changes appropriately.</p>

<p>NDIS calls 
    <i>FilterNetPnPEvent</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>FilterNetPnPEvent</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterNetPnPEvent</i> function that is named "MyNetPnPEvent", use the <b>FILTER_NET_PNP_EVENT</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_NET_PNP_EVENT</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_NET_PNP_EVENT</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>FilterNetPnPEvent</i> is an optional function. If a filter driver does not handle
    network PnP events, it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="https://msdn.microsoft.com/14381de2-36d9-4ec8-9d4e-7af3e6d8ecf3">
    NdisFRegisterFilterDriver</a> function.</p>

<p><i>FilterNetPnPEvent</i> is similar to a protocol driver's 
    <a href="https://msdn.microsoft.com/3f50bcba-c7d2-4d81-bd8b-6080e08fbe74">ProtocolNetPnPEvent</a> function. A
    filter driver can forward these notifications to overlying drivers or it can handle them itself and not
    forward them. To forward a notification, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561828">NdisFNetPnPEvent</a> function. Do not confuse
    this function with the 
    <a href="https://msdn.microsoft.com/dea4ab30-ba1d-4c9c-9f00-e48cc3cc0b46">
    FilterDevicePnPEventNotify</a> function, which filters notifications that are directed down the stack
    to underlying drivers.</p>

<p>NDIS calls 
    <i>FilterNetPnPEvent</i> to notify a filter driver of a PnP or Power Management event
    that was issued for an underlying NIC. NDIS calls the 
    <i>FilterNetPnPEvent</i> function of each filter driver overlying a NIC, and then
    calls the 
    <i>ProtocolNetPnPEvent</i> function of each overlying protocol driver.</p>

<p>When a filter module is inserted into or deleted from a driver stack, the characteristics of the stack
    might change. NDIS sends a PnP event to all affected protocol bindings and filter modules to notify them
    about this change. Filter drivers should handle such changes appropriately.</p>

<p>NDIS calls 
    <i>FilterNetPnPEvent</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>FilterNetPnPEvent</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterNetPnPEvent</i> function that is named "MyNetPnPEvent", use the <b>FILTER_NET_PNP_EVENT</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_NET_PNP_EVENT</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_NET_PNP_EVENT</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/dea4ab30-ba1d-4c9c-9f00-e48cc3cc0b46">FilterDevicePnPEventNotify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561828">NdisFNetPnPEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568752">NET_PNP_EVENT_NOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3f50bcba-c7d2-4d81-bd8b-6080e08fbe74">ProtocolNetPnPEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_NET_PNP_EVENT callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
