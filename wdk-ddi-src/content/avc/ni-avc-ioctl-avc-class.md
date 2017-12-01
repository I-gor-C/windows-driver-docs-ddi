---
UID: NI.avc.IOCTL_AVC_CLASS
title: IOCTL_AVC_CLASS
author: windows-driver-content
description: The IOCTL_AVC_CLASS I/O control code is supported only from kernel mode, using the IRP_MJ_INTERNAL_DEVICE_CONTROL dispatch.Avc.sys supports two device interfaces, depending upon the type of instance (peer or virtual).
old-location: stream\ioctl_avc_class.htm
old-project: stream
ms.assetid: 033069b8-98e5-4302-ae4e-71f9249533ff
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: IOCTL_AVC_CLASS
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

# IOCTL_AVC_CLASS IOCTL



## -description
<p>
<p>The IOCTL_AVC_CLASS I/O control code is supported only from kernel mode, using the IRP_MJ_INTERNAL_DEVICE_CONTROL dispatch.</p>
<p><i>Avc.sys</i> supports two device interfaces, depending upon the type of instance (peer or virtual). These interfaces define the functionality that the driver exposes for subunit drivers, other drivers, and applications. During initialization, <i>avc.sys</i> calls <b>IoRegisterDeviceInterface</b> with either GUID_AVC_CLASS (a peer, or nonvirtual instance) or GUID_VIRTUAL_AVC_CLASS (a virtual instance), then uses <b>IoSetDeviceInterfaceState</b> as appropriate for the started or stopped state of the driver.</p>
<p>Peer instances of <i>avc.sys</i> register the device interface identified by GUID_AVC_CLASS. This interface supports one I/O control code, IOCTL_AVC_CLASS, which in turn supports multiple function codes. Child drivers of peer <i>avc.sys</i> instances are guaranteed to have access to this interface through their parent device object.</p>
<p>Virtual instances of <i>avc.sys</i> register the device interface identified by GUID_VIRTUAL_AVC_CLASS. This interface supports four I/O control codes:</p>
<ul>
<li>
<p>IOCTL_AVC_CLASS</p>
</li>
<li>
<p>IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO</p>
</li>
<li>
<p>IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO</p>
</li>
<li>
<p>IOCTL_AVC_BUS_RESET</p>
</li>
</ul>
<p>The GUID_AVC_CLASS interface supports all IOCTL_AVC_CLASS function codes, although some have limitation on their use. However, the GUID_VIRTUAL_AVC_CLASS interface does not support all IOCTL_AVC_CLASS function codes. The reference page for each individual function code specifies whether it is supported for GUID_VIRTUAL_AVC_CLASS instances of <i>avc.sys</i>.</p>
<p>The IOCTL_AVC_CLASS function codes (and any restrictions) are described in each function code.</p>
<p>For more information about IRPs and IOCTLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546847">Handling IRPs</a>.</p>
</p>
<p>The IOCTL_AVC_CLASS I/O control code is supported only from kernel mode, using the IRP_MJ_INTERNAL_DEVICE_CONTROL dispatch.</p>
<p><i>Avc.sys</i> supports two device interfaces, depending upon the type of instance (peer or virtual). These interfaces define the functionality that the driver exposes for subunit drivers, other drivers, and applications. During initialization, <i>avc.sys</i> calls <b>IoRegisterDeviceInterface</b> with either GUID_AVC_CLASS (a peer, or nonvirtual instance) or GUID_VIRTUAL_AVC_CLASS (a virtual instance), then uses <b>IoSetDeviceInterfaceState</b> as appropriate for the started or stopped state of the driver.</p>
<p>Peer instances of <i>avc.sys</i> register the device interface identified by GUID_AVC_CLASS. This interface supports one I/O control code, IOCTL_AVC_CLASS, which in turn supports multiple function codes. Child drivers of peer <i>avc.sys</i> instances are guaranteed to have access to this interface through their parent device object.</p>
<p>Virtual instances of <i>avc.sys</i> register the device interface identified by GUID_VIRTUAL_AVC_CLASS. This interface supports four I/O control codes:</p>
<p>IOCTL_AVC_CLASS</p>
<p>IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO</p>
<p>IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO</p>
<p>IOCTL_AVC_BUS_RESET</p>
<p>The GUID_AVC_CLASS interface supports all IOCTL_AVC_CLASS function codes, although some have limitation on their use. However, the GUID_VIRTUAL_AVC_CLASS interface does not support all IOCTL_AVC_CLASS function codes. The reference page for each individual function code specifies whether it is supported for GUID_VIRTUAL_AVC_CLASS instances of <i>avc.sys</i>.</p>
<p>The IOCTL_AVC_CLASS function codes (and any restrictions) are described in each function code.</p>
<p>For more information about IRPs and IOCTLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546847">Handling IRPs</a>.</p>


## -syntax

````
typedef struct _AVC_COMMAND_IRB {
  AVC_IRB  Common;
  .
  .
  .
} AVC_COMMAND_IRB, *PAVC_COMMAND_IRB;
````


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
<p>The information the AV/C protocol driver returns in the I/O Status Block (Irp-&gt;IoStatus.Status) is documented with each request.</p>

<p>The information the AV/C protocol driver returns in the I/O Status Block (Irp-&gt;IoStatus.Status) is documented with each request.</p>

## -remarks
<p>Most AV/C functions must be called IRQL = PASSIVE_LEVEL. A few may be called at IRQL &lt;= DISPATCH_LEVEL. The respective IRQL is documented in each AV/C function.</p>

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
<a href="..\avc\ns-avc--avc-command-irb.md">AVC_COMMAND_IRB</a>
</dt>
<dt>
<a href="..\avc\ns-avc--avc-multifunc-irb.md">AVC_MULTIFUNC_IRB</a>
</dt>
<dt>
<a href="..\avc\ns-avc--avc-irb.md">AVC_IRB</a>
</dt>
<dt>
<a href="..\avc\ni-avc-ioctl-avc-update-virtual-subunit-info.md">IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO</a>
</dt>
<dt>
<a href="..\avc\ni-avc-ioctl-avc-remove-virtual-subunit-info.md">IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO</a>
</dt>
<dt>
<a href="..\avc\ni-avc-ioctl-avc-bus-reset.md">IOCTL_AVC_BUS_RESET</a>
</dt>
<dt>
<a href="stream.avc_function">AVC_FUNCTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IOCTL_AVC_CLASS control code%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
