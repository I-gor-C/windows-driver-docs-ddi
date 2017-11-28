---
UID: NC.wdm.IO_COMPLETION_ROUTINE
title: IO_COMPLETION_ROUTINE
author: windows-driver-content
description: The IoCompletion routine completes the processing of I/O operations.
old-location: kernel\iocompletion.htm
old-project: kernel
ms.assetid: 53fc5265-5d8e-4794-942b-de81b93e81da
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoCompletion
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at IRQL <= DISPATCH_LEVEL (see Remarks section).
req.iface: 
req.product: Windows 10 or later.
---

# IO_COMPLETION_ROUTINE callback



## -description
<p>The <i>IoCompletion</i> routine completes the processing of I/O operations.</p>


## -prototype

````
IO_COMPLETION_ROUTINE IoCompletion;

NTSTATUS IoCompletion(
  _In_     PDEVICE_OBJECT DeviceObject,
  _In_     PIRP           Irp,
  _In_opt_ PVOID          Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure. This is the device object for the target device, previously created by the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> structure that describes the I/O operation.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Caller-supplied pointer to driver-specific context information, previously supplied when calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549679">IoSetCompletionRoutine</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549686">IoSetCompletionRoutineEx</a>. Context information must be stored in nonpaged memory, since an <i>IoCompletion</i> routine can be called at DISPATCH_LEVEL. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>If the <i>IoCompletion</i> routine determines that additional processing is required for the IRP, it must return STATUS_MORE_PROCESSING_REQUIRED. For more information, see the following Remarks section. Otherwise, it should return STATUS_SUCCESS. (The I/O manager only checks for the presence or absence of STATUS_MORE_PROCESSING_REQUIRED.)</p>

## -remarks
<p>A driver's <i>IoCompletion</i> routine executes in an arbitrary thread or DPC context, and at an IRQL that is less than or equal to DISPATCH_LEVEL. Because code written to execute at DISPATCH_LEVEL will also execute at lower levels, <i>IoCompletion</i> routines should be designed for execution at DISPATCH_LEVEL. However, because these routines are not guaranteed to run at DISPATCH_LEVEL, they must not call system routines that actually require execution at DISPATCH_LEVEL. (For more information about IRQLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554368">Managing Hardware Priorities</a>.)</p>

<p>To register an <i>IoCompletion</i> routine for a specific IRP, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549679">IoSetCompletionRoutine</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549686">IoSetCompletionRoutineEx</a>, which stores the <i>IoCompletion</i> routine's address in the next-lower driver's I/O stack location. (Thus, a lowest-level driver <u>cannot</u> register an <i>IoCompletion</i> routine.) A driver typically calls <b>IoSetCompletionRoutine</b> or <b>IoSetCompletionRoutineEx</b> from one of its dispatch routines, each time an IRP is received. Most drivers, including all PnP drivers, can use<b> IoSetCompletionRoutine</b> to register their <i>IoCompletion</i> routine. Non-PnP drivers that may be unloaded before their <i>IoCompletion</i> routine executes should use <b>IoSetCompletionRoutineEx</b> instead.</p>

<p>When any driver completes an IRP, it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>, which in turn calls the <i>IoCompletion</i> routine of each higher-level driver, from the next-highest to the highest, until all higher <i>IoCompletion</i> routines have been called or until one routine returns STATUS_MORE_PROCESSING_REQUIRED.</p>

<p>When you create the IRP, allocate a stack location for the current driver as well as any lower drivers. If you do not allocate sufficient stack locations, the <i>DeviceObject</i> pointer might be set to <b>NULL</b> when the completion routine is called. You can avoid allocating extra stack location for the current driver if you use the <i>Context</i> field to pass information to <i>IoCompletion</i> rather then relying on the <i>DeviceObject</i> parameter.</p>

<p>If an <i>IoCompletion</i> routine returns STATUS_MORE_PROCESSING_REQUIRED, the lower driver's call to <b>IoCompleteRequest</b> immediately returns. In this case, a higher-level driver will have to call <b>IoCompleteRequest</b> to complete the IRP.</p>

<p>For more information about implementing <i>IoCompletion</i> routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542018">Completing IRPs</a>.</p>

<p>To define an <i>IoCompletion</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>IoCompletion</i> callback routine that is named <code>MyIoCompletion</code>, use the IO_COMPLETION_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The IO_COMPLETION_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the IO_COMPLETION_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>A driver's <i>IoCompletion</i> routine executes in an arbitrary thread or DPC context, and at an IRQL that is less than or equal to DISPATCH_LEVEL. Because code written to execute at DISPATCH_LEVEL will also execute at lower levels, <i>IoCompletion</i> routines should be designed for execution at DISPATCH_LEVEL. However, because these routines are not guaranteed to run at DISPATCH_LEVEL, they must not call system routines that actually require execution at DISPATCH_LEVEL. (For more information about IRQLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554368">Managing Hardware Priorities</a>.)</p>

<p>To register an <i>IoCompletion</i> routine for a specific IRP, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549679">IoSetCompletionRoutine</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549686">IoSetCompletionRoutineEx</a>, which stores the <i>IoCompletion</i> routine's address in the next-lower driver's I/O stack location. (Thus, a lowest-level driver <u>cannot</u> register an <i>IoCompletion</i> routine.) A driver typically calls <b>IoSetCompletionRoutine</b> or <b>IoSetCompletionRoutineEx</b> from one of its dispatch routines, each time an IRP is received. Most drivers, including all PnP drivers, can use<b> IoSetCompletionRoutine</b> to register their <i>IoCompletion</i> routine. Non-PnP drivers that may be unloaded before their <i>IoCompletion</i> routine executes should use <b>IoSetCompletionRoutineEx</b> instead.</p>

<p>When any driver completes an IRP, it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>, which in turn calls the <i>IoCompletion</i> routine of each higher-level driver, from the next-highest to the highest, until all higher <i>IoCompletion</i> routines have been called or until one routine returns STATUS_MORE_PROCESSING_REQUIRED.</p>

<p>When you create the IRP, allocate a stack location for the current driver as well as any lower drivers. If you do not allocate sufficient stack locations, the <i>DeviceObject</i> pointer might be set to <b>NULL</b> when the completion routine is called. You can avoid allocating extra stack location for the current driver if you use the <i>Context</i> field to pass information to <i>IoCompletion</i> rather then relying on the <i>DeviceObject</i> parameter.</p>

<p>If an <i>IoCompletion</i> routine returns STATUS_MORE_PROCESSING_REQUIRED, the lower driver's call to <b>IoCompleteRequest</b> immediately returns. In this case, a higher-level driver will have to call <b>IoCompleteRequest</b> to complete the IRP.</p>

<p>For more information about implementing <i>IoCompletion</i> routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542018">Completing IRPs</a>.</p>

<p>To define an <i>IoCompletion</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>IoCompletion</i> callback routine that is named <code>MyIoCompletion</code>, use the IO_COMPLETION_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The IO_COMPLETION_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the IO_COMPLETION_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at IRQL &lt;= DISPATCH_LEVEL (see Remarks section).</p>
</td>
</tr>
</table>