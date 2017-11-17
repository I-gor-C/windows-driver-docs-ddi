---
UID: NC.ndis.MINIPORT_CHECK_FOR_HANG
title: MINIPORT_CHECK_FOR_HANG
author: windows-driver-content
description: NDIS calls a miniport driver's MiniportCheckForHangEx function to check the operational state of the miniport adapter that represents a network interface card (NIC).
old-location: netvista\miniportcheckforhangex.htm
ms.assetid: ead0af85-0584-49de-82cc-8a059ebfdf4f
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
req.alt-api: MiniportCheckForHangEx
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

# MINIPORT_CHECK_FOR_HANG callback



## -description
<p>NDIS calls a miniport driver's 
   <i>MiniportCheckForHangEx</i> function to check the operational state of the miniport adapter that represents a network interface card (NIC).</p>


## -prototype

````
MINIPORT_CHECK_FOR_HANG MiniportCheckForHangEx;

BOOLEAN MiniportCheckForHangEx(
  _In_ NDIS_HANDLE MiniportAdapterContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.</p>
</dd>
</dl>

## -returns
<p><i>MiniportCheckForHangEx</i> returns <b>TRUE</b> if the driver determines that a NIC is not
     operating and NDIS should call the driver's <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function. For more information, see the Remarks section.</p>

## -remarks
<p>A miniport driver specifies the 
    <i>MiniportCheckForHangEx</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p><i>MiniportCheckForHangEx</i> is not required for intermediate drivers.</p>

<p><i>MiniportCheckForHangEx</i> does nothing more than check the internal state of the
    NIC and return <b>TRUE</b> if it detects that the NIC is not operating correctly.</p>

<p>By default, NDIS calls 
    <i>MiniportCheckForHangEx</i> approximately every two seconds.  For this reason, your miniport driver's <i>MiniportCheckForHangEx</i> function should return as quickly as possible.</p>

<p>If 
    <i>MiniportCheckForHangEx</i> returns <b>TRUE</b>, NDIS calls the miniport driver's 
    <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function.</p>

<p>If a miniport driver does not complete an OID request within two successive calls to 
    <i>MiniportCheckForHangEx</i>, NDIS can call the driver's 
    <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function. However, to
    avoid unnecessary resets, the driver's 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function can extend the check-for-hang time-out interval
    by setting an appropriate <b>CheckForHangTimeInSeconds</b> value when it calls the 
    <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a> function.</p>

<p>For more information about setting the <b>CheckForHangTimeInSeconds</b> time-out value, see <a href="NULL">Miniport Adapter Check-for-Hang and Reset Operations</a>.</p>

<p><i>MiniportCheckForHangEx</i> can be preempted by an interrupt.</p>

<p>NDIS calls
    <i>MiniportCheckForHangEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportCheckForHangEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportCheckForHangEx</i> function that is named "MyCheckForHangEx", use the <b>MINIPORT_CHECK_FOR_HANG</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_CHECK_FOR_HANG</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_CHECK_FOR_HANG</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A miniport driver specifies the 
    <i>MiniportCheckForHangEx</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p><i>MiniportCheckForHangEx</i> is not required for intermediate drivers.</p>

<p><i>MiniportCheckForHangEx</i> does nothing more than check the internal state of the
    NIC and return <b>TRUE</b> if it detects that the NIC is not operating correctly.</p>

<p>By default, NDIS calls 
    <i>MiniportCheckForHangEx</i> approximately every two seconds.  For this reason, your miniport driver's <i>MiniportCheckForHangEx</i> function should return as quickly as possible.</p>

<p>If 
    <i>MiniportCheckForHangEx</i> returns <b>TRUE</b>, NDIS calls the miniport driver's 
    <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function.</p>

<p>If a miniport driver does not complete an OID request within two successive calls to 
    <i>MiniportCheckForHangEx</i>, NDIS can call the driver's 
    <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function. However, to
    avoid unnecessary resets, the driver's 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function can extend the check-for-hang time-out interval
    by setting an appropriate <b>CheckForHangTimeInSeconds</b> value when it calls the 
    <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a> function.</p>

<p>For more information about setting the <b>CheckForHangTimeInSeconds</b> time-out value, see <a href="NULL">Miniport Adapter Check-for-Hang and Reset Operations</a>.</p>

<p><i>MiniportCheckForHangEx</i> can be preempted by an interrupt.</p>

<p>NDIS calls
    <i>MiniportCheckForHangEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportCheckForHangEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportCheckForHangEx</i> function that is named "MyCheckForHangEx", use the <b>MINIPORT_CHECK_FOR_HANG</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_CHECK_FOR_HANG</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_CHECK_FOR_HANG</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="NULL">Miniport Adapter Check-for-Hang and Reset Operations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_CHECK_FOR_HANG callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
