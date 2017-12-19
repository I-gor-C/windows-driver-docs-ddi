---
UID: NF.pepfx.PoFxRegisterCoreDevice
title: PoFxRegisterCoreDevice function
author: windows-driver-content
description: The PoFxRegisterCoreDevice routine registers a new core system resource with the Windows power management framework (PoFx).
old-location: kernel\pofxregistercoredevice.htm
old-project: kernel
ms.assetid: D1564DB7-57D9-44B2-8ED2-1170CA4C22EE
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
---

# PoFxRegisterCoreDevice function



## -description
The <b>PoFxRegisterCoreDevice</b> routine registers a new core system resource with the Windows power management framework (PoFx).



## -syntax

````
NTSTATUS PoFxRegisterCoreDevice(
  _In_  PCUNICODE_STRING   Id,
  _In_  PPO_FX_CORE_DEVICE Device,
  _Out_ POHANDLE           *Handle
);
````


## -parameters

### -param Id [in]

A string that uniquely identifies the core system resource. This member is a pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains a <a href="devinst.device_identification_strings">device identification string</a>.


### -param Device [in]

A pointer to a <a href="kernel.po_fx_core_device">PO_FX_CORE_DEVICE</a> structure that describes the power characteristics of the core system resource.


### -param Handle [out]

A pointer to a location to which the routine writes a POHANDLE value. This handle represents the registration of the core system resource with PoFx.


## -returns
<b>PoFxRegisterCoreDevice</b> returns STATUS_SUCCESS if the call successfully registers the PEP. Possible error return values include the following status codes.
<dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl>The component count for this device is zero, or the <b>PO_FX_CORE_DEVICE</b> structure contains an invalid version number, or the <b>ComponentCriticalTransitionCallback</b> member of this structure contains an invalid function pointer.
<dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl>Unable to allocate the resources required to complete the requested registration.

 


## -remarks
This routine registers a core system resource so that this resource can be power-managed by PoFx.

Core system resources are hardware devices, such as timers and interrupt controllers, that are managed by the Windows hardware abstraction layer (HAL). These devices provide basic functions that are required by the operating system. Due to the close relationship between core system resources and processors, the power management of these resources needs to be coordinated with processor idle state management.

The <b>PoFxRegisterCoreDevice</b> routine should be called at IRQL = PASSIVE_LEVEL.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
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
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.po_fx_core_device">PO_FX_CORE_DEVICE</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxRegisterCoreDevice routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

