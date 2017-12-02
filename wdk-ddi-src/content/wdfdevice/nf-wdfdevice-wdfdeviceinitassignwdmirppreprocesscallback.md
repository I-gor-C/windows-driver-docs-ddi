---
UID: NF.wdfdevice.WdfDeviceInitAssignWdmIrpPreprocessCallback
title: WdfDeviceInitAssignWdmIrpPreprocessCallback
author: windows-driver-content
description: The WdfDeviceInitAssignWdmIrpPreprocessCallback method registers a callback function to handle an IRP major function code and, optionally, one or more minor function codes that are associated with the major function code.
old-location: wdf\wdfdeviceinitassignwdmirppreprocesscallback.htm
old-project: wdf
ms.assetid: 9c17a5e2-dcf2-493a-9851-11d47adbfc82
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceInitAssignWdmIrpPreprocessCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceInitAssignWdmIrpPreprocessCallback
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, ControlDeviceInitAPI, DeviceInitAPI, DriverCreate, InitFreeDeviceCallback, InitFreeDeviceCreate, InitFreeNull, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI, PdoInitFreeDeviceCallback, PdoInitFreeDeviceCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitAssignWdmIrpPreprocessCallback function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b> method registers a callback function to handle an IRP major function code and, optionally, one or more minor function codes that are associated with the major function code. </p>


## -syntax

````
NTSTATUS WdfDeviceInitAssignWdmIrpPreprocessCallback(
  _In_     PWDFDEVICE_INIT                  DeviceInit,
  _In_     PFN_WDFDEVICE_WDM_IRP_PREPROCESS EvtDeviceWdmIrpPreprocess,
  _In_     UCHAR                            MajorFunction,
  _In_opt_ PUCHAR                           MinorFunctions,
  _In_     ULONG                            NumMinorFunctions
);
````


## -parameters
<dl>

### -param DeviceInit [in]

<dd>
<p>A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.</p>
</dd>

### -param EvtDeviceWdmIrpPreprocess [in]

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function.</p>
</dd>

### -param MajorFunction [in]

<dd>
<p>One of the IRP major function codes that are defined in <i>wdm.h</i>. </p>
</dd>

### -param MinorFunctions [in, optional]

<dd>
<p>A pointer to an array of one or more IRP minor function codes that are associated with the specified major function code. This parameter is optional and can be <b>NULL</b>. For more information, see the following Remarks section.</p>
</dd>

### -param NumMinorFunctions [in]

<dd>
<p>The number of minor function codes that are contained in the <i>MinorFunctions</i> array.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>MajorFunction</i> value is invalid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is insufficient memory.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p> The driver previously registered a <i>MinorFunctions</i> array for this major function and is attempting to specify minor functions again for the specified <i>MajorFunction</i> code.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Drivers can call the <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b> method for either of two reasons:</p>

<p>To handle an IRP major or minor function code that the framework does not support. </p>

<p>For example, the framework does not support <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a>. If your driver must support this IRP, it must register an <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function that handles the IRP. The driver must follow WDM rules for processing IRPs.</p>

<p>To preprocess an IRP before the framework handles it.</p>

<p>In rare cases, it might be necessary for a driver to process an IRP before the framework processes it. In such cases, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function can process the IRP and then call <a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp.md">WdfDeviceWdmDispatchPreprocessedIrp</a> to return the IRP to the framework. Depending on the IRP's function code, the framework might process the IRP itself or it might deliver the IRP to the driver again in a framework request object.</p>

<p>The framework calls the <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function whenever it receives an I/O request packet (IRP) that contains an IRP major function code that matches the <i>MajorFunction</i> parameter and a minor function code that matches one of the minor function codes that are in the <i>MinorFunctions</i> array. </p>

<p>If the <i>MinorFunctions</i> array pointer is <b>NULL</b>, the framework calls the callback function for all minor function codes that are associated with the specified major function code. If the <i>MinorFunctions</i> array pointer is not <b>NULL</b>, the framework makes a copy of the array so that the driver does not have to permanently keep its array.</p>

<p>If the driver received <i>DeviceInit</i> pointer from <a href="..\wdfpdo\nf-wdfpdo-wdfpdoinitallocate.md">WdfPdoInitAllocate</a> or an <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a> event callback function, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function cannot set a completion routine for IRPs that contain a major function code of IRP_MJ_PNP. Otherwise, <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> will report an error.</p>

<p>If your driver calls <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b> one or more times, the framework increments the <b>StackSize</b> member of the driver's WDM <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure one time. As a result, the I/O manager adds an additional <a href="https://msdn.microsoft.com/62c8ee00-c7cb-4aa1-90ab-b8bedbd818ee">I/O stack location</a> to all IRPs  so that the <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function can set an <a href="..\wdm\nc-wdm-io-completion-routine.md">IoCompletion</a> routine. Note that this extra I/O stack location is added to all IRPs, not just the ones that contain an IRP major function code that you specify in a call to <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b>. Therefore, to avoid unnecessarily increasing your driver's use of  the nonpaged memory pool, you should avoid using <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b> unless there is no alternative.</p>

<p>If your driver calls <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b> more than once for the same major code, the framework retains only the most recently set <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function for this major code.  (Your driver can’t register multiple preprocess callbacks for a single major code.)</p>

<p>For more information about the <b>WdfDeviceInitAssignWdmIrpPreprocessCallback</b> method, see <a href="wdf.handling_wdm_irps_outside_of_the_framework">Handling WDM IRPs Outside of the Framework</a>.</p>

<p>The following code example defines an <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> event callback function, and then registers the callback function to handle <a href="https://msdn.microsoft.com/library/windows/hardware/ff549283">IRP_MJ_QUERY_INFORMATION</a> IRPs.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_controldeviceinitapi">ControlDeviceInitAPI</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_initfreedevicecallback">InitFreeDeviceCallback</a>, <a href="devtest.kmdf_initfreedevicecreate">InitFreeDeviceCreate</a>, <a href="devtest.kmdf_initfreenull">InitFreeNull</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>, <a href="devtest.kmdf_pdoinitfreedevicecallback">PdoInitFreeDeviceCallback</a>, <a href="devtest.kmdf_pdoinitfreedevicecreate">PdoInitFreeDeviceCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp.md">WdfDeviceWdmDispatchPreprocessedIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitAssignWdmIrpPreprocessCallback method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
