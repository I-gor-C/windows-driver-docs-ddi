---
UID: NC.wdfdriver.EVT_WDF_DRIVER_UNLOAD
title: EVT_WDF_DRIVER_UNLOAD
author: windows-driver-content
description: A driver's EvtDriverUnload event callback function performs operations that must take place before the driver is unloaded.
old-location: wdf\evtdriverunload.htm
old-project: wdf
ms.assetid: 2a2ed215-1b62-4ff1-bea6-e38fafbcf7d0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_DPC_CONFIG, WDF_DPC_CONFIG, *PWDF_DPC_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtDriverUnload
req.alt-loc: Wdfdriver.h
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
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_DRIVER_UNLOAD callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDriverUnload</i> event callback function performs operations that must take place before the driver is unloaded.</p>


## -prototype

````
EVT_WDF_DRIVER_UNLOAD EvtDriverUnload;

VOID EvtDriverUnload(
  _In_ WDFDRIVER Driver
)
{ ... }
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A handle to a framework driver object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <i>EvtDriverUnload</i> callback function must deallocate any non-device-specific system resources that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine allocated.</p>

<p>The framework does not call a driver's 
    <i>EvtDriverUnload</i> callback function if the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine returns an error status value.</p>

<p>You must declare the function by using the EVT_WDF_DRIVER_UNLOAD type. For more information, see the following Example section.</p>

<p>To define an <i>EvtDriverUnload</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDriverUnload</i> callback function that is named <i>MyDriverUnload</i>, use the <b>EVT_WDF_DRIVER_UNLOAD</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DRIVER_UNLOAD</b> function type is defined in the WdfDriver.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DRIVER_UNLOAD</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>The <i>EvtDriverUnload</i> callback function must deallocate any non-device-specific system resources that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine allocated.</p>

<p>The framework does not call a driver's 
    <i>EvtDriverUnload</i> callback function if the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine returns an error status value.</p>

<p>You must declare the function by using the EVT_WDF_DRIVER_UNLOAD type. For more information, see the following Example section.</p>

<p>To define an <i>EvtDriverUnload</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDriverUnload</i> callback function that is named <i>MyDriverUnload</i>, use the <b>EVT_WDF_DRIVER_UNLOAD</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DRIVER_UNLOAD</b> function type is defined in the WdfDriver.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DRIVER_UNLOAD</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdriver.h (include Wdf.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DRIVER_UNLOAD callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
