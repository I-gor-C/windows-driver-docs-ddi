---
UID: NC.ndis.NDIS_TIMER_FUNCTION
title: NDIS_TIMER_FUNCTION
author: windows-driver-content
description: The NetTimerCallback function is called by NDIS after a driver sets a one-shot or periodic timer when a timer fires.Note  You must declare the function by using the NDIS_TIMER_FUNCTION type.
old-location: netvista\nettimercallback.htm
old-project: netvista
ms.assetid: 76e59376-58a4-4e35-bac4-ec5938c88cd7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetTimerCallback
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
req.irql: DISPATCH_LEVEL
req.iface: 
---

# NDIS_TIMER_FUNCTION callback



## -description
<p>The 
  <i>NetTimerCallback</i> function is called by NDIS after a driver sets a one-shot or periodic timer when a
  timer fires.</p>


## -prototype

````
NDIS_TIMER_FUNCTION NetTimerCallback;

VOID NetTimerCallback(
  _In_ PVOID SystemSpecific1,
  _In_ PVOID FunctionContext,
  _In_ PVOID SystemSpecific2,
  _In_ PVOID SystemSpecific3
)
{ ... }
````


## -parameters
<dl>

### -param <i>SystemSpecific1</i> [in]

<dd>
<p>A pointer to a system-specific value that is reserved for system use.</p>
</dd>

### -param <i>FunctionContext</i> [in]

<dd>
<p>A pointer to a driver-supplied context area that the driver passed to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function. If the 
     <i>FunctionContext</i> parameter of 
     <b>NdisSetTimerObject</b> was <b>NULL</b>, NDIS uses the default value that the driver specified in the 
     <a href="..\ndis\ns-ndis--ndis-timer-characteristics.md">
     NDIS_TIMER_CHARACTERISTICS</a> structure. The driver passed the structure to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a> function
     to initialize the associated timer object.</p>
</dd>

### -param <i>SystemSpecific2</i> [in]

<dd>
<p>A pointer to a system-specific value that is reserved for system use.</p>
</dd>

### -param <i>SystemSpecific3</i> [in]

<dd>
<p>A pointer to a system-specific value that is reserved for system use.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Any NDIS driver can have one or more 
    <i>NetTimerCallback</i> functions. Each such 
    <i>NetTimerCallback</i> function must be associated with a different driver-allocated and initialized
    timer object.</p>

<p>The driver initializes a driver-allocated timer object by calling the 
    <a href="..\ndis\nf-ndis-ndisallocatetimerobject.md">
    NdisAllocateTimerObject</a> function.</p>

<p>A subsequent call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function causes the 
    <i>NetTimerCallback</i> function that is associated with the timer object to be run after a specified
    interval or periodically.</p>

<p>To cancel calls to 
    <i>NetTimerCallback</i>, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a> function. NDIS
    might still call 
    <i>NetTimerCallback</i> if the timeout has already expired before the call to 
    <b>NdisCancelTimerObject</b>.</p>

<p>If a 
    <i>NetTimerCallback</i> function shares resources with other driver functions, the driver should
    synchronize access to those resources with a spin lock.</p>

<p>To define a <i>NetTimerCallback</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NetTimerCallback</i> function that is named "MyTimerCallback", use the <b>NDIS_TIMER_FUNCTION</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_TIMER_FUNCTION</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_TIMER_FUNCTION</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>Any NDIS driver can have one or more 
    <i>NetTimerCallback</i> functions. Each such 
    <i>NetTimerCallback</i> function must be associated with a different driver-allocated and initialized
    timer object.</p>

<p>The driver initializes a driver-allocated timer object by calling the 
    <a href="..\ndis\nf-ndis-ndisallocatetimerobject.md">
    NdisAllocateTimerObject</a> function.</p>

<p>A subsequent call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function causes the 
    <i>NetTimerCallback</i> function that is associated with the timer object to be run after a specified
    interval or periodically.</p>

<p>To cancel calls to 
    <i>NetTimerCallback</i>, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a> function. NDIS
    might still call 
    <i>NetTimerCallback</i> if the timeout has already expired before the call to 
    <b>NdisCancelTimerObject</b>.</p>

<p>If a 
    <i>NetTimerCallback</i> function shares resources with other driver functions, the driver should
    synchronize access to those resources with a spin lock.</p>

<p>To define a <i>NetTimerCallback</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NetTimerCallback</i> function that is named "MyTimerCallback", use the <b>NDIS_TIMER_FUNCTION</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_TIMER_FUNCTION</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_TIMER_FUNCTION</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567886">NDIS_TIMER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a>
</dt>
<dt>
<a href="NULL">Initializing NDIS Timers</a>
</dt>
<dt>
<a href="NULL">Servicing Timers</a>
</dt>
<dt>
<a href="NULL">Setting and Clearing Timers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TIMER_FUNCTION callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
