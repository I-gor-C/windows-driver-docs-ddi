---
UID: NS.parallel._MORE_PARALLEL_PORT_INFORMATION
title: MORE_PARALLEL_PORT_INFORMATION
author: windows-driver-content
description: The MORE_PARALLEL_PORT_INFORMATION structure specifies information about the system interface that supports the operation of a parallel port.
old-location: parports\more_parallel_port_information.htm
old-project: parports
ms.assetid: b21bfbce-5436-4865-b291-2e55abc4aad1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: MORE_PARALLEL_PORT_INFORMATION, MORE_PARALLEL_PORT_INFORMATION, *PMORE_PARALLEL_PORT_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MORE_PARALLEL_PORT_INFORMATION
req.alt-loc: parallel.h
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

# MORE_PARALLEL_PORT_INFORMATION structure



## -description
<p>The MORE_PARALLEL_PORT_INFORMATION structure specifies information about the system interface that supports the operation of a parallel port.</p>


## -syntax

````
typedef struct _MORE_PARALLEL_PORT_INFORMATION {
  INTERFACE_TYPE  InterfaceType;
  ULONG           BusNumber;
  ULONG           InterruptLevel;
  ULONG           InterruptVector;
  KAFFINITY       InterruptAffinity;
  KINTERRUPT_MODE InterruptMode;
} MORE_PARALLEL_PORT_INFORMATION, *PMORE_PARALLEL_PORT_INFORMATION;
````


## -struct-fields
<dl>

### -field InterfaceType

<dd>
<p>Specifies the I/O bus interface type that is associated with a parallel port. See <i>wdm.h </i>or <i>ntddk.h</i> for the definition of INTERFACE_TYPE.</p>
</dd>

### -field BusNumber

<dd>
<p>Specifies the bus number for the interface.</p>
</dd>

### -field InterruptLevel

<dd>
<p>Specifies the interrupt level for the parallel port.</p>
</dd>

### -field InterruptVector

<dd>
<p>Specifies the interrupt vector for the parallel port.</p>
</dd>

### -field InterruptAffinity

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a> interrupt affinity value.</p>
</dd>

### -field InterruptMode

<dd>
<p>Specifies the interrupt mode. See <i>wdm.h </i>or <i>ntddk.h</i> for the declaration of KINTERRUPT_MODE.</p>
</dd>
</dl>

## -remarks
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request from the Plug and Play manager passes a translated resource list that contains the information in a MORE_PARALLEL_PORT_INFORMATION structure. The system-supplied function driver for parallel ports saves the information in the device extension of the parallel port functional device object <a href="wdkgloss.f#wdkgloss.fdo#wdkgloss.fdo"><i>FDO</i></a>, and returns the information in response to an <a href="..\parallel\ni-parallel-ioctl-internal-get-more-parallel-port-info.md">IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO</a> request.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/d8ae2296-05b6-419a-93cc-00fcb12d41fe">Obtaining Information About a ParallelPort</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Parallel.h (include Parallel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-get-more-parallel-port-info.md">IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-get-parallel-pnp-info.md">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a>
</dt>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-get-parallel-port-info.md">IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a>
</dt>
<dt>
<a href="..\parallel\ns-parallel--parallel-port-information.md">PARALLEL_PORT_INFORMATION</a>
</dt>
<dt>
<a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20MORE_PARALLEL_PORT_INFORMATION structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
