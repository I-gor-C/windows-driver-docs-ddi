---
UID: NI.avc.IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO
title: IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO
author: windows-driver-content
description: The IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits.
old-location: stream\ioctl_avc_update_virtual_subunit_info.htm
old-project: stream
ms.assetid: 2a66ea7f-bfa1-4c51-a93d-18043fc49066
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KBUGCHECK_DATA, KBUGCHECK_DATA, *PKBUGCHECK_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: avc.h
req.include-header: Avc.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO
req.alt-loc: avc.h
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

# IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO IOCTL



## -description
<p>
<p>The IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits. It is available to user mode as well as kernel-mode components through the IRP_MJ_DEVICE_CONTROL dispatch. For driver-to-driver communication, it is a METHOD_BUFFERED IOCTL, so set the IRP fields accordingly (IrpStack-&gt;Parameters.DeviceIoControl.InputBufferLength and Irp-&gt;AssociatedIrp.SystemBuffer).</p>
<p>IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO is used to add or remove subunit IDs of a single type. Successive calls with a different ID part of the subunit address cause the number of enumerated IDs to change. Note that <i>avc.sys</i> adds or removes the highest IDs only. This is a limitation of the AV/C specification, not the driver implementation.</p>
<p>This IOCTL uses the AVC_SUBUNIT_ADDR_SPEC structure.</p>
</p>
<p>The IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits. It is available to user mode as well as kernel-mode components through the IRP_MJ_DEVICE_CONTROL dispatch. For driver-to-driver communication, it is a METHOD_BUFFERED IOCTL, so set the IRP fields accordingly (IrpStack-&gt;Parameters.DeviceIoControl.InputBufferLength and Irp-&gt;AssociatedIrp.SystemBuffer).</p>
<p>IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO is used to add or remove subunit IDs of a single type. Successive calls with a different ID part of the subunit address cause the number of enumerated IDs to change. Note that <i>avc.sys</i> adds or removes the highest IDs only. This is a limitation of the AV/C specification, not the driver implementation.</p>
<p>This IOCTL uses the AVC_SUBUNIT_ADDR_SPEC structure.</p>


## -ioctlparameters

### -input-buffer

<text></text>

### -input-buffer-length

<text></text>

### -output-buffer

<text></text>

### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If successful, the AV/C protocol driver sets <b>Irp-&gt;IoStatus.Status </b>to STATUS_SUCCESS.</p>

<p>Possible other return values include:</p>

<p>STATUS_INSUFFICIENT_RESOURCES</p>

<p>No buffer was passed, or insufficient resources available to perform a registry query.</p>

<p>STATUS_INVALID_BUFFER_SIZE</p>

<p>The buffer passed in Irp-&gt;AssociatedIrp.SystemBuffer must be at least as large as sizeof(AVC_SUBUNIT_ADDR_SPEC) which includes a single-byte subunit address, but limited to a 32 byte subunit address.</p>

<p>STATUS_INVALID_PARAMETER</p>

<p>The subunit address was specified incorrectly.</p>

<p>STATUS_ACCESS_DENIED</p>

<p>The current user has insufficient registry access privileges to make the update persistent.</p>

<p> </p>

## -remarks
<p>Must be called at IRQL = PASSIVE_LEVEL.</p>

<p>Must be called at IRQL = PASSIVE_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Avc.h (include Avc.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554198">AVC_SUBUNIT_ADDR_SPEC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560789">IOCTL_AVC_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560793">IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560783">IOCTL_AVC_BUS_RESET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO control code%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
