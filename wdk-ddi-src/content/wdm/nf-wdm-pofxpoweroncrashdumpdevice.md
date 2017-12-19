---
UID: NF.wdm.PoFxPowerOnCrashdumpDevice
title: PoFxPowerOnCrashdumpDevice function
author: windows-driver-content
description: The PoFxPowerOnCrashdumpDevice routine requests that a crash-dump device be turned on.
old-location: kernel\pofxpoweroncrashdumpdevice.htm
old-project: kernel
ms.assetid: 41560DC4-EE5E-4756-8540-ACC19835A9DA
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: PoFxPowerOnCrashdumpDevice
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
req.alt-api: PoFxPowerOnCrashdumpDevice
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
req.irql: <= HIGH_LEVEL
req.product: Windows 10 or later.
---

# PoFxPowerOnCrashdumpDevice function



## -description
The <b>PoFxPowerOnCrashdumpDevice</b> routine requests that a crash-dump device be turned on.



## -syntax

````
NTSTATUS PoFxPowerOnCrashdumpDevice(
  _In_     POHANDLE Handle,
  _In_opt_ PVOID    Context
);
````


## -parameters

### -param Handle [in]

A handle that represents the registration of the crash-dump device with the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The device driver previously received this handle from the <a href="kernel.pofxregisterdevice">PoFxRegisterDevice</a> routine.


### -param Context [in, optional]

A pointer to a device-specific context. This pointer is passed as an input parameter to the <a href="kernel.powerondumpdevicecallback">PowerOnDumpDeviceCallback</a> callback routine that is implemented by the platform extension plug-in (PEP) for the device. The context information is stored in a format that is defined by the device driver and is understood by the PEP. This context is opaque to the operating system. The driver can set this parameter to NULL if the PEP does not require a context.


## -returns
<b>PoFxPowerOnCrashdumpDevice</b> returns STATUS_SUCCESS if the routine succeeds in turning on power to the device. Possible error return values include the following status codes.
<dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl>Not a valid handle value.
<dl>
<dt>STATUS_UNSUCCESSFUL</dt>
</dl>The PEP for this device does not implement a <i>PowerOnDumpDeviceCallback</i> callback routine; or the PEP failed to turn on the device.

 


## -remarks
The driver for a crash-dump device calls this routine to request that the platform extension plug-in (PEP) turn the device on so that a crash dump can be saved. All devices in the crash-dump device chain (which might include a storage controller, a PCI controller, and so on) must be turned on before a crash-dump file can be written to disk.

For more information about crash dumps, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551880">Kernel-Mode Dump Files</a>.

This routine can be called at IRQL &lt;= HIGH_LEVEL.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 8.1.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Pepfx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= HIGH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pofxregisterdevice">PoFxRegisterDevice</a>
</dt>
<dt>
<a href="kernel.powerondumpdevicecallback">PowerOnDumpDeviceCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxPowerOnCrashdumpDevice routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

