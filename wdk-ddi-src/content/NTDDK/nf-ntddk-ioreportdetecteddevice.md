---
UID: NF.ntddk.IoReportDetectedDevice
title: IoReportDetectedDevice
author: windows-driver-content
description: The IoReportDetectedDevice routine reports a non-PnP device to the PnP manager.
old-location: kernel\ioreportdetecteddevice.htm
ms.assetid: b7756f69-feab-4a28-88d5-0262f86db54b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReportDetectedDevice
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: IoReportDetectedDevice
req.iface: 
---

# IoReportDetectedDevice function



## -description
<p>The <b>IoReportDetectedDevice</b> routine reports a non-PnP device to the PnP manager.</p>


## -syntax

````
NTSTATUS IoReportDetectedDevice(
  _In_     PDRIVER_OBJECT                 DriverObject,
  _In_     INTERFACE_TYPE                 LegacyBusType,
  _In_     ULONG                          BusNumber,
  _In_     ULONG                          SlotNumber,
  _In_opt_ PCM_RESOURCE_LIST              ResourceList,
  _In_opt_ PIO_RESOURCE_REQUIREMENTS_LIST ResourceRequirements,
  _In_     BOOLEAN                        ResourceAssigned,
  _Inout_  PDEVICE_OBJECT                 *DeviceObject
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Pointer to the driver object of the driver that detected the device.</p>
</dd>

### -param <i>LegacyBusType</i> [in]

<dd>
<p>Specifies the type of bus on which the device resides. The PnP manager uses this information to match the reported device to its PnP-enumerated instance, if one exists.</p>
<p>The interface types, such as <b>PCIBus</b>, are defined in Wdm.h. If a driver does not know the <i>LegacyBusType</i> for the device, the driver supplies the value <b>InterfaceTypeUndefined</b> for this parameter.</p>
</dd>

### -param <i>BusNumber</i> [in]

<dd>
<p>Specifies the bus number for the device. The PnP manager uses this information to match the reported device to its PnP-enumerated instance, if one exists.</p>
<p>The bus number distinguishes the bus on which the device resides from other buses of the same type on the computer. The bus-numbering scheme is bus-specific. If a driver does not know the <i>BusNumber</i> for the device, the driver supplies the value -1 for this parameter. </p>
</dd>

### -param <i>SlotNumber</i> [in]

<dd>
<p>Specifies the logical slot number of the device. The PnP manager uses this information to match the reported device to its PnP-enumerated instance, if one exists.</p>
<p>If a driver does not know the <i>SlotNumber</i> for the device, the driver supplies the value -1 for this parameter.</p>
</dd>

### -param <i>ResourceList</i> [in, optional]

<dd>
<p>Pointer to the resource list the driver used to detect the device. Resources in this list are in raw, untranslated form. </p>
</dd>

### -param <i>ResourceRequirements</i> [in, optional]

<dd>
<p>Optionally points to a resource requirements list for the detected device. <b>NULL</b> if the caller does not have this information for the device.</p>
</dd>

### -param <i>ResourceAssigned</i> [in]

<dd>
<p>Specifies whether the device's resources have already been reported to the PnP manager. If <i>ResourceAssigned</i> is <b>TRUE</b>, the resources have already been reported, possibly with <a href="https://msdn.microsoft.com/library/windows/hardware/ff549608">IoReportResourceForDetection</a>, and the PnP manager will not attempt to claim them on behalf of the device. If <b>TRUE</b>, the PnP manager will also not claim resources when the device is root-enumerated on subsequent boots.</p>
</dd>

### -param <i>DeviceObject</i> [in, out]

<dd>
<p>Optionally points to a PDO for the detected device. </p>
<p><b>NULL</b> if the caller does not have a PDO for the device, which is typically the case. If <i>DeviceObject</i> is <b>NULL</b>, the PnP manager creates a PDO for the device and returns a pointer to the caller.</p>
<p>If the caller supplies a PDO, the PnP manager does not create a new PDO. On a given call to this routine the <i>DeviceObject</i> parameter is either an IN or an OUT parameter, but not both. </p>
</dd>
</dl>

## -returns
<p><b>IoReportDetectedDevice</b> returns STATUS_SUCCESS on success, or the appropriate error code on failure.</p>

## -remarks
<p>Drivers for legacy devices use <b>IoReportDetectedDevice</b> to report their devices to the system. A driver should only call <b>IoReportDetectedDevice</b> to report a legacy, non-PnP device. PnP devices should be reported in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a> request.</p>

<p>Drivers only need to call <b>IoReportDetectedDevice</b> the first time they are loaded because the PnP manager caches the reported information. Drivers that use this routine should store a flag in the registry to indicate whether they have already done device detection.</p>

<p>A driver typically calls this routine from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. A few drivers, like certain NDIS or EISA drivers, might call this routine from an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>

<p>On successful completion of <b>IoReportDetectedDevice</b>, the caller should attach an FDO to the PDO returned at <i>DeviceObject</i>. Once the caller attaches its FDO, the caller is the function driver for the device, at least temporarily. There are no filter drivers. The PnP manager owns the PDO.</p>

<p>The PnP manager considers the device to be started and therefore does not call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine and does not send an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request. The driver must be prepared to handle all other PnP IRPs, however. </p>

<p><b>IoReportDetectedDevice</b> marks the device as a root-enumerated device and this identification is persistent across system boots. During subsequent system boots the PnP manager "detects" the device on the root-enumerated list and configures it like a PnP device: the PnP manager queries for device information, identifies the appropriate drivers and calls their <i>AddDevice</i> routines, and sends all the appropriate PnP IRPs.</p>

<p>The system generates two compatible ID strings for the device, of the form DETECTED<i>Interface</i>\<i>Driver</i> and DETECTED\<i>Driver</i>. <i>Interface</i> is the string name of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547839">INTERFACE_TYPE</a> of the first bus specified in the <i>ResourceList</i> parameter. <i>Interface</i> is set to "Internal" if no bus is specified. <i>Driver</i> is the driver's service name. A driver can provide additional hardware IDs or compatible IDs by handling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551679">IRP_MN_QUERY_ID</a> request.</p>

<p>A driver writer must provide an INF file that matches any of the specified hardware IDs or compatible IDs. The INF file should specify the original driver that called <b>IoReportDetectedDevice</b> as the driver to load for those IDs. The system uses this information to rebuild the driver stack for the device, for example on restart. Callers of <b>IoReportDetectedDevice</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

<p>Drivers for legacy devices use <b>IoReportDetectedDevice</b> to report their devices to the system. A driver should only call <b>IoReportDetectedDevice</b> to report a legacy, non-PnP device. PnP devices should be reported in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a> request.</p>

<p>Drivers only need to call <b>IoReportDetectedDevice</b> the first time they are loaded because the PnP manager caches the reported information. Drivers that use this routine should store a flag in the registry to indicate whether they have already done device detection.</p>

<p>A driver typically calls this routine from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. A few drivers, like certain NDIS or EISA drivers, might call this routine from an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>

<p>On successful completion of <b>IoReportDetectedDevice</b>, the caller should attach an FDO to the PDO returned at <i>DeviceObject</i>. Once the caller attaches its FDO, the caller is the function driver for the device, at least temporarily. There are no filter drivers. The PnP manager owns the PDO.</p>

<p>The PnP manager considers the device to be started and therefore does not call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine and does not send an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request. The driver must be prepared to handle all other PnP IRPs, however. </p>

<p><b>IoReportDetectedDevice</b> marks the device as a root-enumerated device and this identification is persistent across system boots. During subsequent system boots the PnP manager "detects" the device on the root-enumerated list and configures it like a PnP device: the PnP manager queries for device information, identifies the appropriate drivers and calls their <i>AddDevice</i> routines, and sends all the appropriate PnP IRPs.</p>

<p>The system generates two compatible ID strings for the device, of the form DETECTED<i>Interface</i>\<i>Driver</i> and DETECTED\<i>Driver</i>. <i>Interface</i> is the string name of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547839">INTERFACE_TYPE</a> of the first bus specified in the <i>ResourceList</i> parameter. <i>Interface</i> is set to "Internal" if no bus is specified. <i>Driver</i> is the driver's service name. A driver can provide additional hardware IDs or compatible IDs by handling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551679">IRP_MN_QUERY_ID</a> request.</p>

<p>A driver writer must provide an INF file that matches any of the specified hardware IDs or compatible IDs. The INF file should specify the original driver that called <b>IoReportDetectedDevice</b> as the driver to load for those IDs. The system uses this information to rebuild the driver stack for the device, for example on restart. Callers of <b>IoReportDetectedDevice</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549608">IoReportResourceForDetection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoReportDetectedDevice routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
