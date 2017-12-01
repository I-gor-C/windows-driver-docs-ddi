---
UID: NI.pmi.IOCTL_PMI_SET_CONFIGURATION
title: IOCTL_PMI_SET_CONFIGURATION
author: windows-driver-content
description: The IOCTL_PMI_SET_CONFIGURATION request sets the configuration data for a power meter.
old-location: powermeter\ioctl_pmi_set_configuration.htm
old-project: powermeter
ms.assetid: c8eff87f-b8af-4876-9327-545eeff958c3
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: PEP_WORK_IDLE_STATE, PEP_WORK_IDLE_STATE, *PPEP_WORK_IDLE_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: pmi.h
req.include-header: Pmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_PMI_SET_CONFIGURATION
req.alt-loc: Pmi.h
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

# IOCTL_PMI_SET_CONFIGURATION IOCTL



## -description
<p>The <b>IOCTL_PMI_SET_CONFIGURATION</b> request sets the configuration data for a power meter.</p>


## -ioctlparameters

### -input-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member of the I/O request packet (IRP) points to an initiator-allocated input buffer that contains a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. This structure contains the configuration data.</p>

### -input-buffer-length
<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member of the IRP's current I/O stack location (<a href="..\wdm\ns-wdm--io-stack-location.md">IO_STACK_LOCATION</a>) is set to the size in bytes of the input buffer that is pointed to by the <b>AssociatedIrp.SystemBuffer</b> member. This size must be greater than or equal to <b>sizeof</b>(<b>PMI_CONFIGURATION</b>) or the request fails with an error status of STATUS_BUFFER_TOO_SMALL.</p>

<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member of the IRP's current I/O stack location (<a href="..\wdm\ns-wdm--io-stack-location.md">IO_STACK_LOCATION</a>) is set to the size in bytes of the input buffer that is pointed to by the <b>AssociatedIrp.SystemBuffer</b> member. This size must be greater than or equal to <b>sizeof</b>(<b>PMI_CONFIGURATION</b>) or the request fails with an error status of STATUS_BUFFER_TOO_SMALL.</p>

### -output-buffer
<p>None.</p>

<p>None.</p>

<p>None.</p>

### -output-buffer-length
<p>None.</p>

<p>None.</p>

<p>None.</p>

<p>None.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Information</b> member is set to the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The WDM driver that supports the PMI interface has completed the IOCTL request successfully. </p>

<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member of the <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> is less than the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. </p>

<p>The <b>Information</b> member is set to the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The WDM driver that supports the PMI interface has completed the IOCTL request successfully. </p>

<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member of the <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> is less than the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. </p>

<p>The <b>Information</b> member is set to the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The WDM driver that supports the PMI interface has completed the IOCTL request successfully. </p>

<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member of the <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> is less than the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. </p>

<p>The <b>Information</b> member is set to the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The WDM driver that supports the PMI interface has completed the IOCTL request successfully. </p>

<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member of the <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> is less than the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. </p>

<p>The <b>Information</b> member is set to the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The WDM driver that supports the PMI interface has completed the IOCTL request successfully. </p>

<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member of the <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> is less than the size, in bytes, of a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. </p>

## -remarks
<p>The <b>IOCTL_PMI_SET_CONFIGURATION</b> request sets the configuration parameters for the power meter. The <b>AssociatedIrp.SystemBuffer</b> member of the IRP references a buffer that contains a <a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a> structure. The <b>ConfigurationType</b> member of this structure contains information about the type of PMI configuration data to set in the power meter.</p>

<p>Only PMI configuration data that the power meter supports with read/write permissions can be changed by using a set request of <b>IOCTL_PMI_SET_CONFIGURATION</b>. A set request of <b>IOCTL_PMI_SET_CONFIGURATION</b> to change read-only PMI configuration data will fail, and the data will not be changed on the power meter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pmi.h (include Pmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--io-stack-location.md">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--irp.md">IRP</a>
</dt>
<dt>
<a href="..\pmi\ns-pmi--pmi-configuration.md">PMI_CONFIGURATION</a>
</dt>
<dt>
<a href="..\pmi\ns-pmi--pmi-reported-capabilities.md">PMI_REPORTED_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20IOCTL_PMI_SET_CONFIGURATION control code%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
