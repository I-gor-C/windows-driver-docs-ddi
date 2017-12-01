---
UID: NC.ntddk.EXPAND_STACK_CALLOUT
title: EXPAND_STACK_CALLOUT
author: windows-driver-content
description: The ExpandedStackCall routine executes with a guaranteed stack size.
old-location: kernel\expandedstackcall.htm
old-project: kernel
ms.assetid: ca9af049-f183-458c-b43f-891678a7be5e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Drivers can implement ExpandedStackCall routines on Windows Server 2003 for an x64-based processor, and on Windows Vista and later versions of Windows for all processors.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExpandedStackCall
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# EXPAND_STACK_CALLOUT callback



## -description
<p>The <i>ExpandedStackCall</i> routine executes with a guaranteed stack size.</p>


## -prototype

````
EXPAND_STACK_CALLOUT ExpandedStackCall;

VOID ExpandedStackCall(
  _In_opt_ PVOID Parameter
)
{ ... }
````


## -parameters
<dl>

### -param <i>Parameter</i> [in, optional]

<dd>
<p>The value passed to the <a href="..\ntddk\nf-ntddk-keexpandkernelstackandcallout.md">KeExpandKernelStackAndCallout</a> routine that executed <i>ExpandedStackCall</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <i>ExpandedStackCall</i> routine must handle all exceptions. Any unhandled exception causes the system to bug check with <a href="https://msdn.microsoft.com/library/windows/hardware/ff557408">Bug Check 0x1E: KMODE_EXCEPTION_NOT_HANDLED</a>.</p>

<p>If the <i>ExpandedStackCall</i> changes the current IRQL, it must restore the original value before returning. </p>

<p>To define an <i>ExpandedStackCall</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>ExpandedStackCall</i> callback routine that is named <code>MyExpandedStackCall</code>, use the EXPAND_STACK_CALLOUT type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The EXPAND_STACK_CALLOUT function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EXPAND_STACK_CALLOUT function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Drivers can implement <i>ExpandedStackCall</i> routines on Windows Server 2003 for an x64-based processor, and on Windows Vista and later versions of Windows for all processors.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-keexpandkernelstackandcallout.md">KeExpandKernelStackAndCallout</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExpandedStackCall routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
