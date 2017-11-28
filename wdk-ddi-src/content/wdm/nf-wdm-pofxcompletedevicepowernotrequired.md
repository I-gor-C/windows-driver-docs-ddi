---
UID: NF.wdm.PoFxCompleteDevicePowerNotRequired
title: PoFxCompleteDevicePowerNotRequired
author: windows-driver-content
description: The PoFxCompleteDevicePowerNotRequired routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's DevicePowerNotRequiredCallback callback routine.
old-location: kernel\pofxcompletedevicepowernotrequired.htm
old-project: kernel
ms.assetid: 7DCAFA7C-6F13-4020-BCB6-D36EE164BDAA
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PoFxCompleteDevicePowerNotRequired
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxCompleteDevicePowerNotRequired
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoFxCompleteDevicePowerNotRequired function



## -description
<p>The <b>PoFxCompleteDevicePowerNotRequired</b> routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh450946">DevicePowerNotRequiredCallback</a> callback routine.</p>


## -syntax

````
VOID PoFxCompleteDevicePowerNotRequired(
  _In_ POHANDLE Handle
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with PoFx. The device driver previously received this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a> routine.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>After PoFx calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh450946">DevicePowerNotRequiredCallback</a> callback routine, the driver must respond by calling <b>PoFxCompleteDevicePowerNotRequired</b>.</p>

<p>PoFx calls the driver's <i>DevicePowerNotRequiredCallback</i> routine to inform the driver that the device is no longer required to remain in the D0 state. In response to this call, the driver can choose to enter a low-power Dx state or to remain in the D0 state. After the driver has completed its response to the <i>DevicePowerNotRequiredCallback</i> call, the driver calls <b>PoFxCompleteDevicePowerNotRequired</b> to inform PoFx. The <b>PoFxCompleteDevicePowerNotRequired</b> call can occur either during or after the <i>DevicePowerNotRequiredCallback</i> call.</p>

<p>After PoFx calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh450946">DevicePowerNotRequiredCallback</a> callback routine, the driver must respond by calling <b>PoFxCompleteDevicePowerNotRequired</b>.</p>

<p>PoFx calls the driver's <i>DevicePowerNotRequiredCallback</i> routine to inform the driver that the device is no longer required to remain in the D0 state. In response to this call, the driver can choose to enter a low-power Dx state or to remain in the D0 state. After the driver has completed its response to the <i>DevicePowerNotRequiredCallback</i> call, the driver calls <b>PoFxCompleteDevicePowerNotRequired</b> to inform PoFx. The <b>PoFxCompleteDevicePowerNotRequired</b> call can occur either during or after the <i>DevicePowerNotRequiredCallback</i> call.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
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
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450946">DevicePowerNotRequiredCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxCompleteDevicePowerNotRequired routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
