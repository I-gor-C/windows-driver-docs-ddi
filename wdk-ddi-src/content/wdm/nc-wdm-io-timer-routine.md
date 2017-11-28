---
UID: NC.wdm.IO_TIMER_ROUTINE
title: IO_TIMER_ROUTINE
author: windows-driver-content
description: The IoTimer routine is a DPC that, if registered, is called once per second.
old-location: kernel\iotimer.htm
old-project: kernel
ms.assetid: c41b7489-afd2-4ddf-b296-6d42e3ff6cbf
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
req.alt-api: IoTimer
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
req.irql: Called at DISPATCH_LEVEL (see Remarks section).
req.iface: 
req.product: Windows 10 or later.
---

# IO_TIMER_ROUTINE callback



## -description
<p>The <i>IoTimer</i> routine is a DPC that, if registered, is called once per second.</p>


## -prototype

````
IO_TIMER_ROUTINE IoTimer;

VOID IoTimer(
  _In_     struct DEVICE_OBJECT *DeviceObject,
  _In_opt_ PVOID                Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure. This is the device object for the target device, previously created by the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Caller-supplied pointer to driver-defined context information, specified in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549344">IoInitializeTimer</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver's <i>IoTimer</i> routine executes in a DPC context, at IRQL = DISPATCH_LEVEL.</p>

<p>A driver can associate an <i>IoTimer</i> routine with each device object it creates. (You can use a single <i>IoTimer</i> routine with multiple device objects, or a separate routine with each device object.) To register an <i>IoTimer</i> routine, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549344">IoInitializeTimer</a>, supplying the <i>IoTimer</i> routine's address and a device object pointer.</p>

<p>To queue an <i>IoTimer</i> routine for execution, a driver routine must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550373">IoStartTimer</a>. The system calls the <i>IoTimer</i> routine once per second until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550377">IoStopTimer</a>.</p>

<p>For more information about <i>IoTimer</i> routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550386">IoTimer Routines</a>.</p>

<p>To define an <i>IoTimer</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>IoTimer</i> callback routine that is named <code>MyIoTimer</code>, use the IO_TIMER_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The IO_TIMER_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the IO_TIMER_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>A driver's <i>IoTimer</i> routine executes in a DPC context, at IRQL = DISPATCH_LEVEL.</p>

<p>A driver can associate an <i>IoTimer</i> routine with each device object it creates. (You can use a single <i>IoTimer</i> routine with multiple device objects, or a separate routine with each device object.) To register an <i>IoTimer</i> routine, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549344">IoInitializeTimer</a>, supplying the <i>IoTimer</i> routine's address and a device object pointer.</p>

<p>To queue an <i>IoTimer</i> routine for execution, a driver routine must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550373">IoStartTimer</a>. The system calls the <i>IoTimer</i> routine once per second until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550377">IoStopTimer</a>.</p>

<p>For more information about <i>IoTimer</i> routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550386">IoTimer Routines</a>.</p>

<p>To define an <i>IoTimer</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>IoTimer</i> callback routine that is named <code>MyIoTimer</code>, use the IO_TIMER_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The IO_TIMER_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the IO_TIMER_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Called at DISPATCH_LEVEL (see Remarks section).</p>
</td>
</tr>
</table>