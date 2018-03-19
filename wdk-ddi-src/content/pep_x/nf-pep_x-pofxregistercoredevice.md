---
UID: NF:pep_x.PoFxRegisterCoreDevice
title: PoFxRegisterCoreDevice function
author: windows-driver-content
description: The PoFxRegisterCoreDevice routine registers a new core system resource with the Windows power management framework (PoFx).
old-location: kernel\pofxregistercoredevice.htm
old-project: kernel
ms.assetid: D1564DB7-57D9-44B2-8ED2-1170CA4C22EE
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: PoFxRegisterCoreDevice, PoFxRegisterCoreDevice routine [Kernel-Mode Driver Architecture], kernel.pofxregistercoredevice, pepfx/PoFxRegisterCoreDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pep_x.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	ntoskrnl.lib
-	ntoskrnl.dll
api_name:
-	PoFxRegisterCoreDevice
product: Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE, PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PoFxRegisterCoreDevice function
The <b>PoFxRegisterCoreDevice</b> routine registers a new core system resource with the Windows power management framework (PoFx).

## Syntax

````
NTSTATUS PoFxRegisterCoreDevice(
  _In_  PCUNICODE_STRING   Id,
  _In_  PPO_FX_CORE_DEVICE Device,
  _Out_ POHANDLE           *Handle
);
````

## Parameters

`Id`

A string that uniquely identifies the core system resource. This member is a pointer to a <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure that contains a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/install/device-identification-strings">device identification string</a>.

`Device`

A pointer to a <a href="..\pepfx\ns-pepfx-_po_fx_core_device.md">PO_FX_CORE_DEVICE</a> structure that describes the power characteristics of the core system resource.

`Handle`

A pointer to a location to which the routine writes a POHANDLE value. This handle represents the registration of the core system resource with PoFx.


## Return Value

<b>PoFxRegisterCoreDevice</b> returns STATUS_SUCCESS if the call successfully registers the PEP. Possible error return values include the following status codes.

<table>
<tr>
<th>Return value</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl>
</td>
<td width="60%">
The component count for this device is zero, or the <b>PO_FX_CORE_DEVICE</b> structure contains an invalid version number, or the <b>ComponentCriticalTransitionCallback</b> member of this structure contains an invalid function pointer.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl>
</td>
<td width="60%">
Unable to allocate the resources required to complete the requested registration.

</td>
</tr>
</table>

## Remarks

This routine registers a core system resource so that this resource can be power-managed by PoFx.

Core system resources are hardware devices, such as timers and interrupt controllers, that are managed by the Windows hardware abstraction layer (HAL). These devices provide basic functions that are required by the operating system. Due to the close relationship between core system resources and processors, the power management of these resources needs to be coordinated with processor idle state management.

The <b>PoFxRegisterCoreDevice</b> routine should be called at IRQL = PASSIVE_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pep_x.h (include Pep_x.h) |
| **Library** | Ntoskrnl.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a>



<a href="..\pepfx\ns-pepfx-_po_fx_core_device.md">PO_FX_CORE_DEVICE</a>