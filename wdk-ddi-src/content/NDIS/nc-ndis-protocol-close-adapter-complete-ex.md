---
UID: NC.ndis.PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX
title: PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX
author: windows-driver-content
description: NDIS calls a protocol driver's ProtocolCloseAdapterCompleteEx function to complete a close adapter operation for which the NdisCloseAdapterEx function returned NDIS_STATUS_PENDING.Note  You must declare the function by using the PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX type. For more information, see the following Examples section.
old-location: netvista\protocolcloseadaptercompleteex.htm
ms.assetid: 62cc047a-bc91-4e1e-817e-7fd509d4d90e
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
req.alt-api: ProtocolCloseAdapterCompleteEx
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

# PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX callback



## -description
<p>NDIS calls a protocol driver's 
  <i>ProtocolCloseAdapterCompleteEx</i> function to complete a close adapter operation for which the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a> function returned
  NDIS_STATUS_PENDING.</p>


## -prototype

````
PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX ProtocolCloseAdapterCompleteEx;

VOID ProtocolCloseAdapterCompleteEx(
  _In_ NDIS_HANDLE ProtocolBindingContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolBindingContext</i> [in]

<dd>
<p>A handle to a context area allocated by the protocol driver. The protocol driver maintains the
     per-binding context information in this context area. The driver supplied this handle to NDIS when the
     driver called the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>ProtocolCloseAdapterCompleteEx</i> is a required function.</p>

<p>If 
    <i>ProtocolUnbindAdapterEx</i> is waiting for NDIS to call 
    <i>ProtocolCloseAdapterCompleteEx</i>, this function can simply indicate that it has been called and
    return (for example, it updates the 
    <i>ProtocolBindingContext</i> context area). This allows the 
    <i>ProtocolCloseAdapterCompleteEx</i> function to complete the unbind operation.</p>

<p>After the protocol driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a> function, the 
    <i>NdisBindingHandle</i> handle that the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function returned is
    no longer valid. Therefore, 
    <i>ProtocolCloseAdapterCompleteEx</i> cannot call any 
    <b>Ndis<i>Xxx</i></b> functions that require this handle as a parameter.</p>

<p>If the 
    <a href="https://msdn.microsoft.com/19fa7be2-acb9-42f6-bd9f-5be3e3c8b5fa">
    ProtocolUnbindAdapterEx</a> function has not already done so,
    <i>ProtocolCloseAdapterCompleteEx</i> can release the resources that the protocol driver allocated for
    per-binding network I/O operations.</p>

<p>If 
    <i>ProtocolUnbindAdapterEx</i> returned NDIS_STATUS_PENDING and saved the 
    <i>UnbindContext</i> handle in the context area at 
    <i>ProtocolBindingContext</i>, 
    <i>ProtocolCloseAdapterCompleteEx</i> can call the 
    <a href="https://msdn.microsoft.com/3a1daad4-d4b7-4950-be58-73612949fba9">
    NdisCompleteUnbindAdapterEx</a> function to complete the unbinding operation. Consequently, 
    <i>ProtocolCloseAdapterCompleteEx</i> should not release the context area until after it calls 
    <b>NdisCompleteUnbindAdapterEx</b>.</p>

<p>NDIS calls 
    <i>ProtocolCloseAdapterCompleteEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>ProtocolCloseAdapterCompleteEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCloseAdapterCompleteEx</i> function that is named "MyCloseAdapterCompleteEx", use the <b>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>ProtocolCloseAdapterCompleteEx</i> is a required function.</p>

<p>If 
    <i>ProtocolUnbindAdapterEx</i> is waiting for NDIS to call 
    <i>ProtocolCloseAdapterCompleteEx</i>, this function can simply indicate that it has been called and
    return (for example, it updates the 
    <i>ProtocolBindingContext</i> context area). This allows the 
    <i>ProtocolCloseAdapterCompleteEx</i> function to complete the unbind operation.</p>

<p>After the protocol driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a> function, the 
    <i>NdisBindingHandle</i> handle that the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function returned is
    no longer valid. Therefore, 
    <i>ProtocolCloseAdapterCompleteEx</i> cannot call any 
    <b>Ndis<i>Xxx</i></b> functions that require this handle as a parameter.</p>

<p>If the 
    <a href="https://msdn.microsoft.com/19fa7be2-acb9-42f6-bd9f-5be3e3c8b5fa">
    ProtocolUnbindAdapterEx</a> function has not already done so,
    <i>ProtocolCloseAdapterCompleteEx</i> can release the resources that the protocol driver allocated for
    per-binding network I/O operations.</p>

<p>If 
    <i>ProtocolUnbindAdapterEx</i> returned NDIS_STATUS_PENDING and saved the 
    <i>UnbindContext</i> handle in the context area at 
    <i>ProtocolBindingContext</i>, 
    <i>ProtocolCloseAdapterCompleteEx</i> can call the 
    <a href="https://msdn.microsoft.com/3a1daad4-d4b7-4950-be58-73612949fba9">
    NdisCompleteUnbindAdapterEx</a> function to complete the unbinding operation. Consequently, 
    <i>ProtocolCloseAdapterCompleteEx</i> should not release the context area until after it calls 
    <b>NdisCompleteUnbindAdapterEx</b>.</p>

<p>NDIS calls 
    <i>ProtocolCloseAdapterCompleteEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>ProtocolCloseAdapterCompleteEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCloseAdapterCompleteEx</i> function that is named "MyCloseAdapterCompleteEx", use the <b>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561640">NdisCloseAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561708">NdisCompleteUnbindAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/19fa7be2-acb9-42f6-bd9f-5be3e3c8b5fa">ProtocolUnbindAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
