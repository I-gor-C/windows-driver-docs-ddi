---
UID: NF.wdm.PoFxRegisterCrashdumpDevice
title: PoFxRegisterCrashdumpDevice
author: windows-driver-content
description: The PoFxRegisterCrashdumpDevice routine registers a crash-dump device.
old-location: kernel\pofxregistercrashdumpdevice.htm
old-project: kernel
ms.assetid: 3237B68F-838A-4443-89FD-DC7815EAB403
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoFxRegisterCrashdumpDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Pepfx.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxRegisterCrashdumpDevice
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoFxRegisterCrashdumpDevice function



## -description
<p>The <b>PoFxRegisterCrashdumpDevice</b> routine registers a crash-dump device.</p>


## -syntax

````
NTSTATUS PoFxRegisterCrashdumpDevice(
   POHANDLE Handle
);
````


## -parameters
<dl>

### -param Handle 

<dd>
<p>A handle that represents the registration of the crash-dump device with the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The device driver previously received this handle from the <a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a> routine.</p>
</dd>
</dl>

## -returns
<p><b>PoFxRegisterCrashdumpDevice</b> returns STATUS_SUCCESS if the routine successfully registers the crash-dump device. Possible error return values include the following status codes.</p><dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl><p>Not a valid handle value.</p><dl>
<dt>STATUS_UNSUCCESSFUL</dt>
</dl><p>There is no PEP for this device.</p>

<p> </p>

## -remarks
<p>This routine is called by the driver for a crash-dump device to inform PoFx that the device is part of the crash-dump device chain. Several devices (storage controller, PCI controller, and so on) might need to be turned on so that the Windows kernel can write a crash-dump file to disk. When a fatal system error occurs, the kernel tries to turn on the crash-dump devices and save the crash-dump file.</p>

<p>The driver must call <a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a> to register the device with PoFx before calling <b>PoFxRegisterCrashdumpDevice</b>.</p>

<p>The driver for a crash-dump device can call the <a href="..\wdm\nf-wdm-pofxpoweroncrashdumpdevice.md">PoFxPowerOnCrashdumpDevice</a> routine to request that the PEP turn the device on.</p>

<p>For more information about crash dumps, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551880">Kernel-Mode Dump Files</a>.</p>

<p><b>PoFxRegisterCrashdumpDevice</b> must be called at IRQL = PASSIVE_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Pepfx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
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

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-pofxpoweroncrashdumpdevice.md">PoFxPowerOnCrashdumpDevice</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxRegisterCrashdumpDevice routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
