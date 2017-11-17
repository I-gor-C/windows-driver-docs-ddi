---
UID: NC.wdfdevice.EVT_WDFDEVICE_WDM_IRP_PREPROCESS
title: EVT_WDFDEVICE_WDM_IRP_PREPROCESS
author: windows-driver-content
description: A driver's EvtDeviceWdmIrpPreprocess event callback function receives an IRP before the framework processes the IRP.
old-location: wdf\evtdevicewdmirppreprocess.htm
ms.assetid: aff9cb60-d61b-47a8-aae4-6ffd2a1b7a9a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtDeviceWdmIrpPreprocess
req.alt-loc: Wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDFDEVICE_WDM_IRP_PREPROCESS callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtDeviceWdmIrpPreprocess</i> event callback function receives an IRP before the framework processes the IRP.</p>


## -prototype

````
EVT_WDFDEVICE_WDM_IRP_PREPROCESS EvtDeviceWdmIrpPreprocess;

NTSTATUS EvtDeviceWdmIrpPreprocess(
  _In_    WDFDEVICE Device,
  _Inout_ PIRP      Irp
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> structure.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtDeviceWdmIrpPreprocess</i> callback function must:</p>

<p>
<ul>
<li>Set the <b>IoStatus.Status</b> member of the IRP to STATUS_SUCCESS or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(status) equals <b>TRUE</b>, and return the same value (after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>), if the callback function successfully completes the received IRP.</li>
<li>Set the <b>IoStatus.Status</b> member of the IRP to a status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(status) equals <b>FALSE</b>, and return the same value (after calling IoCompleteRequest), if the callback function detects an error. </li>
<li>Return STATUS_PENDING, if the callback function calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422">IoMarkIrpPending</a>. 
</li>
<li>Return the value that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546927">WdfDeviceWdmDispatchPreprocessedIrp</a> method returns, if the callback function calls that method. 
</li>
</ul>
</p>

## -remarks
<p>To register an <i>EvtDeviceWdmIrpPreprocess</i> callback function, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546043">WdfDeviceInitAssignWdmIrpPreprocessCallback</a>. </p>

<p>Your driver can use an <i>EvtDeviceWdmIrpPreprocess</i> callback function to do any, or all, of the following:</p>

<p> Handle an IRP that the framework does not support, by following the <a href="https://msdn.microsoft.com/5fb6d2b9-17ee-4e76-95e9-dd5a7d1e79de">WDM rules for handling IRPs</a>. </p>

<p> Preprocess an IRP before the framework handles it. </p>

<p> Set a completion routine so that the driver can postprocess an IRP after the framework handles it. </p>

<p>For more information about how to implement an <i>EvtDeviceWdmIrpPreprocess</i> callback function, see <a href="wdf.handling_wdm_irps_outside_of_the_framework">Handling WDM IRPs Outside of the Framework</a>.</p>

<p>If you want the framework to subsequently handle the IRP as it would if the <i>EvtDeviceWdmIrpPreprocess</i> callback function had not been called, the callback function must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546927">WdfDeviceWdmDispatchPreprocessedIrp</a> to return the IRP to the framework.</p>

<p>If your driver registers an <i>EvtDeviceWdmIrpPreprocess</i> callback function, the framework adds an additional <a href="https://msdn.microsoft.com/62c8ee00-c7cb-4aa1-90ab-b8bedbd818ee">I/O stack location</a> to IRPs that the callback function receives. The additional I/O stack location allows the callback function to set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546927">WdfDeviceWdmDispatchPreprocessedIrp</a>.</p>

<p>The <i>EvtDeviceWdmIrpPreprocess</i> callback function is called at the IRQL of the calling thread. The IRQL is determined by the type of IRP that the framework is passing to <i>EvtDeviceWdmIrpPreprocess</i>. For example, if the PnP manager sends <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a> at IRQL = PASSIVE_LEVEL, the framework calls <i>EvtDeviceWdmIrpPreprocess</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define an <i>EvtDeviceWdmIrpPreprocess</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceWdmIrpPreprocess</i> callback function that is named <i>MyDeviceWdmIrpPreprocess</i>, use the <b>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>To register an <i>EvtDeviceWdmIrpPreprocess</i> callback function, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546043">WdfDeviceInitAssignWdmIrpPreprocessCallback</a>. </p>

<p>Your driver can use an <i>EvtDeviceWdmIrpPreprocess</i> callback function to do any, or all, of the following:</p>

<p> Handle an IRP that the framework does not support, by following the <a href="https://msdn.microsoft.com/5fb6d2b9-17ee-4e76-95e9-dd5a7d1e79de">WDM rules for handling IRPs</a>. </p>

<p> Preprocess an IRP before the framework handles it. </p>

<p> Set a completion routine so that the driver can postprocess an IRP after the framework handles it. </p>

<p>For more information about how to implement an <i>EvtDeviceWdmIrpPreprocess</i> callback function, see <a href="wdf.handling_wdm_irps_outside_of_the_framework">Handling WDM IRPs Outside of the Framework</a>.</p>

<p>If you want the framework to subsequently handle the IRP as it would if the <i>EvtDeviceWdmIrpPreprocess</i> callback function had not been called, the callback function must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546927">WdfDeviceWdmDispatchPreprocessedIrp</a> to return the IRP to the framework.</p>

<p>If your driver registers an <i>EvtDeviceWdmIrpPreprocess</i> callback function, the framework adds an additional <a href="https://msdn.microsoft.com/62c8ee00-c7cb-4aa1-90ab-b8bedbd818ee">I/O stack location</a> to IRPs that the callback function receives. The additional I/O stack location allows the callback function to set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546927">WdfDeviceWdmDispatchPreprocessedIrp</a>.</p>

<p>The <i>EvtDeviceWdmIrpPreprocess</i> callback function is called at the IRQL of the calling thread. The IRQL is determined by the type of IRP that the framework is passing to <i>EvtDeviceWdmIrpPreprocess</i>. For example, if the PnP manager sends <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a> at IRQL = PASSIVE_LEVEL, the framework calls <i>EvtDeviceWdmIrpPreprocess</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define an <i>EvtDeviceWdmIrpPreprocess</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceWdmIrpPreprocess</i> callback function that is named <i>MyDeviceWdmIrpPreprocess</i>, use the <b>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546043">WdfDeviceInitAssignWdmIrpPreprocessCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546927">WdfDeviceWdmDispatchPreprocessedIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDFDEVICE_WDM_IRP_PREPROCESS callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
