---
UID: NF.ntddk.IoReportResourceForDetection
title: IoReportResourceForDetection
author: windows-driver-content
description: The IoReportResourceForDetection routine claims hardware resources in the configuration registry for a legacy device.
old-location: kernel\ioreportresourcefordetection.htm
old-project: kernel
ms.assetid: 83b8e0b0-112c-4263-91f8-0c2e20dd76a4
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoReportResourceForDetection
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReportResourceForDetection
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
---

# IoReportResourceForDetection function



## -description
<p>The <b>IoReportResourceForDetection</b> routine claims hardware resources in the configuration registry for a legacy device.</p>


## -syntax

````
NTSTATUS IoReportResourceForDetection(
  _In_     PDRIVER_OBJECT    DriverObject,
  _In_opt_ PCM_RESOURCE_LIST DriverList,
  _In_opt_ ULONG             DriverListSize,
  _In_opt_ PDEVICE_OBJECT    DeviceObject,
  _In_opt_ PCM_RESOURCE_LIST DeviceList,
  _In_opt_ ULONG             DeviceListSize,
  _Out_    PBOOLEAN          ConflictDetected
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Pointer to the driver object that was input to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine.</p>
</dd>

### -param <i>DriverList</i> [in, optional]

<dd>
<p>Optionally points to a caller-supplied buffer that contains the driver's resource list, if the driver claims the same resources for all its devices. If the caller specifies a <i>DeviceList</i>, this parameter is ignored.</p>
</dd>

### -param <i>DriverListSize</i> [in, optional]

<dd>
<p>Specifies the size in bytes of an optional <i>DriverList</i>. If <i>DriverList</i> is <b>NULL</b>, this parameter should be zero.</p>
</dd>

### -param <i>DeviceObject</i> [in, optional]

<dd>
<p>Optionally points to the device object representing device for which the driver is attempting to claim resources. </p>
</dd>

### -param <i>DeviceList</i> [in, optional]

<dd>
<p>Optionally points to a caller-supplied buffer containing the device's resource list. If the driver claims the same resources for all its devices, the caller can specify a <i>DriverList</i> instead. </p>
</dd>

### -param <i>DeviceListSize</i> [in, optional]

<dd>
<p>Specifies the size in bytes of an optional <i>DeviceList</i>. If <i>DeviceList</i> is <b>NULL</b>, this parameter should be zero. </p>
</dd>

### -param <i>ConflictDetected</i> [out]

<dd>
<p>Pointer to a caller-supplied Boolean value that is set to <b>TRUE</b> on return if the resources are not available. </p>
</dd>
</dl>

## -returns
<p><b>IoReportResourceForDetection</b> returns STATUS_SUCCESS if the resources are claimed. Possible error return values include the following.</p><dl>
<dt><b>STATUS_CONFLICTING_ADDRESSES</b></dt>
</dl><p>The resources could not be claimed because they are already in use or are needed for a PnP-enumerable device.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The <i>DeviceList</i> or <i>DriverList</i> is invalid.</p>

<p> </p>

## -remarks
<p>This routine is for drivers that detect earlier hardware which cannot be enumerated by Plug and Play (PnP).</p>

<p>If a driver supports only PnP hardware, it does no detection and therefore does not call <b>IoReportResourceForDetection</b>. The PnP system enumerates each PnP device, assigns resources to the device, and passes those resources to the device's drivers in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request.</p>

<p>If a PnP driver supports legacy hardware, however, it must call <b>IoReportResourceForDetection</b> to claim hardware resources before it attempts to detect the device.</p>

<p>Callers of this routine specify a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541994">CM_RESOURCE_LIST</a> in either a <i>DeviceList</i> or a <i>DriverList</i> that is allocated from paged memory and that consists of raw, untranslated resources. The caller is responsible for freeing the memory. </p>

<p>A driver that can control more than one legacy card at the same time should claim the resources for each device against the device object for the respective device (using the <i>DeviceObject</i>, <i>DeviceList</i>, and <i>DeviceListSize</i> parameters). Such a driver must not claim these resources against their driver object.</p>

<p>A <b>CM_RESOURCE_LIST</b> contains two variable-sized arrays. Each array has a default size of one. If either array has more than one element, the caller must allocate memory dynamically to contain the additional elements. Only one <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> can be part of each <a href="https://msdn.microsoft.com/library/windows/hardware/ff541954">CM_FULL_RESOURCE_DESCRIPTOR</a> in the list, except for the last full resource descriptor in the <b>CM_RESOURCE_LIST</b>, which can have additional partial resource descriptors in its array.</p>

<p><b>IoReportResourceForDetection</b>, with the help of the PnP manager, determines whether the resources being requested conflict with resources that have already been claimed.</p>

<p>If a conflict is detected, this routine sets the BOOLEAN at <i>ConflictDetected</i> to <b>TRUE</b> and returns STATUS_CONFLICTING_ADDRESSES. </p>

<p>If no conflict is detected, this routine claims the resources, sets the BOOLEAN at <i>ConflictDetected</i> to <b>FALSE</b>, and returns STATUS_SUCCESS.</p>

<p>If this routine succeeds and the driver detects a legacy device, the driver reports the device to the PnP manager by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549597">IoReportDetectedDevice</a>. In that call, the driver sets <i>ResourceAssigned</i> to <b>TRUE</b> so the PnP manager does not attempt to claim the resources again.</p>

<p>When a driver no longer requires the resources claimed by a call to this routine, the driver calls this routine again with a <i>DriverList</i> or <i>DeviceList</i> with a <b>Count</b> of zero.</p>

<p>If a driver claims resources on a device-specific basis for more than one device, the driver must call this routine for each such device.</p>

<p>A driver can call this routine more than once for a given device. If one set of resources fails, the driver can call the routine again for the same device with a different set of resources. If a set of resources succeeds, the driver can call this routine again with a new list; the new list replaces the previous list.</p>

<p>Callers of <b>IoReportResourceForDetection</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

<p>This routine is for drivers that detect earlier hardware which cannot be enumerated by Plug and Play (PnP).</p>

<p>If a driver supports only PnP hardware, it does no detection and therefore does not call <b>IoReportResourceForDetection</b>. The PnP system enumerates each PnP device, assigns resources to the device, and passes those resources to the device's drivers in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request.</p>

<p>If a PnP driver supports legacy hardware, however, it must call <b>IoReportResourceForDetection</b> to claim hardware resources before it attempts to detect the device.</p>

<p>Callers of this routine specify a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541994">CM_RESOURCE_LIST</a> in either a <i>DeviceList</i> or a <i>DriverList</i> that is allocated from paged memory and that consists of raw, untranslated resources. The caller is responsible for freeing the memory. </p>

<p>A driver that can control more than one legacy card at the same time should claim the resources for each device against the device object for the respective device (using the <i>DeviceObject</i>, <i>DeviceList</i>, and <i>DeviceListSize</i> parameters). Such a driver must not claim these resources against their driver object.</p>

<p>A <b>CM_RESOURCE_LIST</b> contains two variable-sized arrays. Each array has a default size of one. If either array has more than one element, the caller must allocate memory dynamically to contain the additional elements. Only one <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> can be part of each <a href="https://msdn.microsoft.com/library/windows/hardware/ff541954">CM_FULL_RESOURCE_DESCRIPTOR</a> in the list, except for the last full resource descriptor in the <b>CM_RESOURCE_LIST</b>, which can have additional partial resource descriptors in its array.</p>

<p><b>IoReportResourceForDetection</b>, with the help of the PnP manager, determines whether the resources being requested conflict with resources that have already been claimed.</p>

<p>If a conflict is detected, this routine sets the BOOLEAN at <i>ConflictDetected</i> to <b>TRUE</b> and returns STATUS_CONFLICTING_ADDRESSES. </p>

<p>If no conflict is detected, this routine claims the resources, sets the BOOLEAN at <i>ConflictDetected</i> to <b>FALSE</b>, and returns STATUS_SUCCESS.</p>

<p>If this routine succeeds and the driver detects a legacy device, the driver reports the device to the PnP manager by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549597">IoReportDetectedDevice</a>. In that call, the driver sets <i>ResourceAssigned</i> to <b>TRUE</b> so the PnP manager does not attempt to claim the resources again.</p>

<p>When a driver no longer requires the resources claimed by a call to this routine, the driver calls this routine again with a <i>DriverList</i> or <i>DeviceList</i> with a <b>Count</b> of zero.</p>

<p>If a driver claims resources on a device-specific basis for more than one device, the driver must call this routine for each such device.</p>

<p>A driver can call this routine more than once for a given device. If one set of resources fails, the driver can call the routine again for the same device with a different set of resources. If a set of resources succeeds, the driver can call this routine again with a new list; the new list replaces the previous list.</p>

<p>Callers of <b>IoReportResourceForDetection</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541994">CM_RESOURCE_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549597">IoReportDetectedDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoReportResourceForDetection routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
