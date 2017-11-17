---
UID: NC.wdfdevice.EVT_WDF_DEVICE_RELATIONS_QUERY
title: EVT_WDF_DEVICE_RELATIONS_QUERY
author: windows-driver-content
description: A driver's EvtDeviceRelationsQuery event callback reports changes in the relationships among devices that are supported by the driver.
old-location: wdf\evtdevicerelationsquery.htm
ms.assetid: 3a156696-1dd5-4383-a0cc-8d07ec92bdbf
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
req.umdf-ver: 2.0
req.alt-api: EvtDeviceRelationsQuery
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
req.irql: PASSIVE_LEVEL
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_DEVICE_RELATIONS_QUERY callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDeviceRelationsQuery</i> event callback reports changes in the relationships among devices that are supported by the driver.</p>


## -prototype

````
EVT_WDF_DEVICE_RELATIONS_QUERY EvtDeviceRelationsQuery;

VOID EvtDeviceRelationsQuery(
  _In_ WDFDEVICE            Device,
  _In_ DEVICE_RELATION_TYPE RelationType
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>RelationType</i> [in]

<dd>
<p>A DEVICE_RELATION_TYPE-typed enumerator value. The DEVICE_RELATION_TYPE enumeration is defined in <i>wdm.h</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To register the <i>EvtDeviceRelationsQuery</i> callback function, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>.</p>

<p>Most framework-based drivers do not need to provide this callback function.</p>

<p>During system initialization, the Plug and Play manager enumerates all of the devices on the system by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a> request to the driver stack. If a framework-based driver has registered an <i>EvtDeviceRelationsQuery</i> callback function, the framework calls it. The function driver for the bus must report all of the child devices that are attached to the bus.</p>

<p>Additionally, after the framework calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549353">IoInvalidateDeviceRelations</a> routine to report a changed relationship among the devices on the driver's bus, the Plug and Play manager sends another IRP_MN_QUERY_DEVICE_RELATIONS request to the driver stack. The framework then calls the driver's <i>EvtDeviceRelationsQuery</i> callback function so that the driver can provide details about the change. </p>

<p>The type of work that a driver must do depends on the value received for the <i>RelationType</i> parameter. The value can be one of the following:</p>

<p></p><dl>
<dt><a id="BusRelations"></a><a id="busrelations"></a><a id="BUSRELATIONS"></a><b>BusRelations</b></dt>
<dd>
<p>Most framework-based drivers do not report bus relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers follow the guidelines that are described in <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>
</dd>
<dt><a id="EjectionRelations"></a><a id="ejectionrelations"></a><a id="EJECTIONRELATIONS"></a><b>EjectionRelations</b></dt>
<dd>
<p>Most framework-based drivers do not report ejection relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the driver for the device's bus calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548770">WdfPdoAddEjectionRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548814">WdfPdoRemoveEjectionRelationsPhysicalDevice</a><i>.</i></p>
</dd>
<dt><a id="RemovalRelations"></a><a id="removalrelations"></a><a id="REMOVALRELATIONS"></a><b>RemovalRelations</b></dt>
<dd>
<p>Most framework-based drivers do not report removal relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545875">WdfDeviceAddRemovalRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546834">WdfDeviceRemoveRemovalRelationsPhysicalDevice</a>.</p>
</dd>
<dt><a id="TargetDeviceRelation"></a><a id="targetdevicerelation"></a><a id="TARGETDEVICERELATION"></a><b>TargetDeviceRelation</b></dt>
<dd>
<p>Framework-based drivers do not have to report a device's target relation. Instead, the framework handles this request.</p>
</dd>
</dl><p>Most framework-based drivers do not report bus relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers follow the guidelines that are described in <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>Most framework-based drivers do not report ejection relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the driver for the device's bus calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548770">WdfPdoAddEjectionRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548814">WdfPdoRemoveEjectionRelationsPhysicalDevice</a><i>.</i></p>

<p>Most framework-based drivers do not report removal relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545875">WdfDeviceAddRemovalRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546834">WdfDeviceRemoveRemovalRelationsPhysicalDevice</a>.</p>

<p>Framework-based drivers do not have to report a device's target relation. Instead, the framework handles this request.</p>

<p>The framework can call the <i>EvtDeviceRelationsQuery</i> callback function with a <i>RelationType</i> value of <b>EjectionRelations</b> or <b>RemovalRelations</b> even if the device is being removed. </p>

<p>To define an <i>EvtDeviceRelationsQuery</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceRelationsQuery</i> callback function that is named <i>MyDeviceRelationsQuery</i>, use the <b>EVT_WDF_DEVICE_RELATIONS_QUERY</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_RELATIONS_QUERY</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_RELATIONS_QUERY</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>To register the <i>EvtDeviceRelationsQuery</i> callback function, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>.</p>

<p>Most framework-based drivers do not need to provide this callback function.</p>

<p>During system initialization, the Plug and Play manager enumerates all of the devices on the system by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a> request to the driver stack. If a framework-based driver has registered an <i>EvtDeviceRelationsQuery</i> callback function, the framework calls it. The function driver for the bus must report all of the child devices that are attached to the bus.</p>

<p>Additionally, after the framework calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549353">IoInvalidateDeviceRelations</a> routine to report a changed relationship among the devices on the driver's bus, the Plug and Play manager sends another IRP_MN_QUERY_DEVICE_RELATIONS request to the driver stack. The framework then calls the driver's <i>EvtDeviceRelationsQuery</i> callback function so that the driver can provide details about the change. </p>

<p>The type of work that a driver must do depends on the value received for the <i>RelationType</i> parameter. The value can be one of the following:</p>

<p></p><dl>
<dt><a id="BusRelations"></a><a id="busrelations"></a><a id="BUSRELATIONS"></a><b>BusRelations</b></dt>
<dd>
<p>Most framework-based drivers do not report bus relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers follow the guidelines that are described in <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>
</dd>
<dt><a id="EjectionRelations"></a><a id="ejectionrelations"></a><a id="EJECTIONRELATIONS"></a><b>EjectionRelations</b></dt>
<dd>
<p>Most framework-based drivers do not report ejection relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the driver for the device's bus calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548770">WdfPdoAddEjectionRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548814">WdfPdoRemoveEjectionRelationsPhysicalDevice</a><i>.</i></p>
</dd>
<dt><a id="RemovalRelations"></a><a id="removalrelations"></a><a id="REMOVALRELATIONS"></a><b>RemovalRelations</b></dt>
<dd>
<p>Most framework-based drivers do not report removal relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545875">WdfDeviceAddRemovalRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546834">WdfDeviceRemoveRemovalRelationsPhysicalDevice</a>.</p>
</dd>
<dt><a id="TargetDeviceRelation"></a><a id="targetdevicerelation"></a><a id="TARGETDEVICERELATION"></a><b>TargetDeviceRelation</b></dt>
<dd>
<p>Framework-based drivers do not have to report a device's target relation. Instead, the framework handles this request.</p>
</dd>
</dl><p>Most framework-based drivers do not report bus relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers follow the guidelines that are described in <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>Most framework-based drivers do not report ejection relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the driver for the device's bus calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548770">WdfPdoAddEjectionRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548814">WdfPdoRemoveEjectionRelationsPhysicalDevice</a><i>.</i></p>

<p>Most framework-based drivers do not report removal relations in an <i>EvtDeviceRelationsQuery</i> callback function. Instead, the drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545875">WdfDeviceAddRemovalRelationsPhysicalDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546834">WdfDeviceRemoveRemovalRelationsPhysicalDevice</a>.</p>

<p>Framework-based drivers do not have to report a device's target relation. Instead, the framework handles this request.</p>

<p>The framework can call the <i>EvtDeviceRelationsQuery</i> callback function with a <i>RelationType</i> value of <b>EjectionRelations</b> or <b>RemovalRelations</b> even if the device is being removed. </p>

<p>To define an <i>EvtDeviceRelationsQuery</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceRelationsQuery</i> callback function that is named <i>MyDeviceRelationsQuery</i>, use the <b>EVT_WDF_DEVICE_RELATIONS_QUERY</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_RELATIONS_QUERY</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_RELATIONS_QUERY</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>Wdfdevice.h (include Wdf.h)</dt>
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