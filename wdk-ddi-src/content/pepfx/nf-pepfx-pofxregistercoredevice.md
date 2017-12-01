---
UID: NF.pepfx.PoFxRegisterCoreDevice
title: PoFxRegisterCoreDevice
author: windows-driver-content
description: The PoFxRegisterCoreDevice routine registers a new core system resource with the Windows power management framework (PoFx).
old-location: kernel\pofxregistercoredevice.htm
old-project: kernel
ms.assetid: D1564DB7-57D9-44B2-8ED2-1170CA4C22EE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoFxRegisterCoreDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxRegisterCoreDevice
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
---

# PoFxRegisterCoreDevice function



## -description
<p>The <b>PoFxRegisterCoreDevice</b> routine registers a new core system resource with the Windows power management framework (PoFx).</p>


## -syntax

````
NTSTATUS PoFxRegisterCoreDevice(
  _In_  PCUNICODE_STRING   Id,
  _In_  PPO_FX_CORE_DEVICE Device,
  _Out_ POHANDLE           *Handle
);
````


## -parameters
<dl>

### -param <i>Id</i> [in]

<dd>
<p>A string that uniquely identifies the core system resource. This member is a pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains a <a href="devinst.device_identification_strings">device identification string</a>.</p>
</dd>

### -param <i>Device</i> [in]

<dd>
<p>A pointer to a <a href="..\pepfx\ns-pepfx--po-fx-core-device.md">PO_FX_CORE_DEVICE</a> structure that describes the power characteristics of the core system resource.</p>
</dd>

### -param <i>Handle</i> [out]

<dd>
<p>A pointer to a location to which the routine writes a POHANDLE value. This handle represents the registration of the core system resource with PoFx.</p>
</dd>
</dl>

## -returns
<p><b>PoFxRegisterCoreDevice</b> returns STATUS_SUCCESS if the call successfully registers the PEP. Possible error return values include the following status codes.</p><dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl><p>The component count for this device is zero, or the <b>PO_FX_CORE_DEVICE</b> structure contains an invalid version number, or the <b>ComponentCriticalTransitionCallback</b> member of this structure contains an invalid function pointer.</p><dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl><p>Unable to allocate the resources required to complete the requested registration.</p>

<p> </p>

## -remarks
<p>This routine registers a core system resource so that this resource can be power-managed by PoFx.</p>

<p>Core system resources are hardware devices, such as timers and interrupt controllers, that are managed by the Windows hardware abstraction layer (HAL). These devices provide basic functions that are required by the operating system. Due to the close relationship between core system resources and processors, the power management of these resources needs to be coordinated with processor idle state management.</p>

<p>The <b>PoFxRegisterCoreDevice</b> routine should be called at IRQL = PASSIVE_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
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
<a href="..\pepfx\ns-pepfx--po-fx-core-device.md">PO_FX_CORE_DEVICE</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxRegisterCoreDevice routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
