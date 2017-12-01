---
UID: NC.wdm.DRIVER_CONTROL
title: DRIVER_CONTROL
author: windows-driver-content
description: The ControllerControl routine starts a data transfer operation.
old-location: kernel\controllercontrol.htm
old-project: kernel
ms.assetid: 8cd081ba-c28a-41c9-8f20-43cef0dbdaa4
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: ControllerControl
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

# DRIVER_CONTROL callback



## -description
<p>The <i>ControllerControl</i> routine starts a data transfer operation.</p>


## -prototype

````
DRIVER_CONTROL ControllerControl;

IO_ALLOCATION_ACTION ControllerControl(
  _In_    struct _DEVICE_OBJECT *DeviceObject,
  _Inout_ struct _IRP           *Irp,
  _In_    PVOID                 MapRegisterBase,
  _In_    PVOID                 Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Caller-supplied pointer to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure. This is the device object for the target device, previously created by the driver's <a href="kernel.adddevice">AddDevice</a> routine.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>Caller-supplied pointer to an <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> structure that describes the I/O operation, if the driver has a <a href="kernel.startio">StartIo</a> routine. Otherwise, not used.</p>
</dd>

### -param <i>MapRegisterBase</i> [in]

<dd>
<p>Not used.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Caller-supplied pointer to driver-defined context information, specified in a previous call to <a href="..\ntddk\nf-ntddk-ioallocatecontroller.md">IoAllocateController</a>.</p>
</dd>
</dl>

## -returns
<p>The routine must return one of the enumerated values defined by <a href="..\wdm\ne-wdm--io-allocation-action.md">IO_ALLOCATION_ACTION</a>.</p>

## -remarks
<p>A driver's <i>ControllerControl</i> routine executes in an arbitrary thread context at IRQL = DISPATCH_LEVEL.</p>

<p>To register a <i>ControllerControl</i> routine for a specific device object, a driver must call <a href="..\ntddk\nf-ntddk-iocreatecontroller.md">IoCreateController</a> to obtain a controller object, then call <a href="..\ntddk\nf-ntddk-ioallocatecontroller.md">IoAllocateController</a> to request use of the controller and to supply the <i>ControllerControl</i> routine's address. When the controller is free, the system calls the <i>ControllerControl</i> routine.</p>

<p>For detailed information about implementing a <i>ControllerControl</i> routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566405">Writing ControllerControl Routines</a>. Also see <a href="https://msdn.microsoft.com/74b6685a-018f-4cb1-9332-424631aad85c">Controller Objects</a>.</p>

<p>To define a <i>ControllerControl</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ControllerControl</i> callback routine that is named <code>MyControllerControl</code>, use the DRIVER_CONTROL type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The DRIVER_CONTROL function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the DRIVER_CONTROL function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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