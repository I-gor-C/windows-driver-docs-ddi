---
UID: NF.wdm.PoStartNextPowerIrp
title: PoStartNextPowerIrp
author: windows-driver-content
description: The PoStartNextPowerIrp routine signals the power manager that the driver is ready to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.).
old-location: kernel\postartnextpowerirp.htm
ms.assetid: 92754668-5327-4e37-9da1-cc1870f923c5
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoStartNextPowerIrp
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: PoStartNextPowerIrp
req.iface: 
req.product: Windows 10 or later.
---

# PoStartNextPowerIrp function



## -description
<p>The <b>PoStartNextPowerIrp</b> routine signals the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> that the driver is ready to handle the next power <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>. (Windows Server 2003, Windows XP, and Windows 2000 only.)</p>


## -syntax

````
VOID PoStartNextPowerIrp(
  _Inout_ PIRP Irp
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to an IRP in which the major function code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Starting with Windows Vista, the driver is not required to call <b>PoStartNextPowerIrp</b> and a call to this routine does not perform a power management operation. However, on Windows Server 2003, Windows XP, and Windows 2000, <b>PoStartNextPowerIrp</b> must be called by every driver in a device stack after the driver is finished with the previous power IRP, if any, and is ready to handle the next power IRP. It must be called once by each driver for every <a href="https://msdn.microsoft.com/library/windows/hardware/ff551699">IRP_MN_QUERY_POWER</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> request.</p>

<p>Although power IRPs are completed only once, typically by the bus driver for a device, each driver in the device stack must call <b>PoStartNextPowerIrp</b> as the IRP travels down or back up the stack. Even if a driver fails the IRP, the driver must nevertheless call <b>PoStartNextPowerIrp</b> to signal the power manager that it is ready to handle another power IRP.</p>

<p>The driver must call <b>PoStartNextPowerIrp</b> while the current IRP stack location points to the current driver. Therefore, this routine must be called before <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559654">PoCallDriver</a>. As a general rule, a driver should call <b>PoStartNextPowerIrp</b> from its <i>IoCompletion</i> routine associated with the IRP or from the callback routine it passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559734">PoRequestPowerIrp</a>.</p>

<p>Bus drivers must call <b>PoStartNextPowerIrp</b> before completing each IRP.</p>

<p>Starting with Windows Vista, the driver is not required to call <b>PoStartNextPowerIrp</b> and a call to this routine does not perform a power management operation. However, on Windows Server 2003, Windows XP, and Windows 2000, <b>PoStartNextPowerIrp</b> must be called by every driver in a device stack after the driver is finished with the previous power IRP, if any, and is ready to handle the next power IRP. It must be called once by each driver for every <a href="https://msdn.microsoft.com/library/windows/hardware/ff551699">IRP_MN_QUERY_POWER</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> request.</p>

<p>Although power IRPs are completed only once, typically by the bus driver for a device, each driver in the device stack must call <b>PoStartNextPowerIrp</b> as the IRP travels down or back up the stack. Even if a driver fails the IRP, the driver must nevertheless call <b>PoStartNextPowerIrp</b> to signal the power manager that it is ready to handle another power IRP.</p>

<p>The driver must call <b>PoStartNextPowerIrp</b> while the current IRP stack location points to the current driver. Therefore, this routine must be called before <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559654">PoCallDriver</a>. As a general rule, a driver should call <b>PoStartNextPowerIrp</b> from its <i>IoCompletion</i> routine associated with the IRP or from the callback routine it passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559734">PoRequestPowerIrp</a>.</p>

<p>Bus drivers must call <b>PoStartNextPowerIrp</b> before completing each IRP.</p>

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
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551699">IRP_MN_QUERY_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559654">PoCallDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559734">PoRequestPowerIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoStartNextPowerIrp routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
