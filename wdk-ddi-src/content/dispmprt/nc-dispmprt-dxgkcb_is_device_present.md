---
UID: NC.dispmprt.DXGKCB_IS_DEVICE_PRESENT
title: DXGKCB_IS_DEVICE_PRESENT
author: windows-driver-content
description: The DxgkCbIsDevicePresent function determines whether a specified PCI device is present.
old-location: display\dxgkcbisdevicepresent.htm
old-project: display
ms.assetid: 82716a1a-e361-40ad-b3cd-bdcd3abc75f8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbIsDevicePresent
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# DXGKCB_IS_DEVICE_PRESENT callback



## -description
The <b>DxgkCbIsDevicePresent</b> function determines whether a specified PCI device is present.


## -prototype

````
DXGKCB_IS_DEVICE_PRESENT DxgkCbIsDevicePresent;

NTSTATUS DxgkCbIsDevicePresent(
  _In_  HANDLE                          DeviceHandle,
  _In_  PPCI_DEVICE_PRESENCE_PARAMETERS DevicePresenceParameters,
  _Out_ PBOOLEAN                        DevicePresent
)
{ ... }
````


## -parameters

### -param DeviceHandle [in]

A handle that represents a display adapter. The display miniport driver previously obtained this handle in the <b>DeviceHandle</b> member of the <a href="display.dxgkrnl_interface">DXGKRNL_INTERFACE</a> structure that was passed to <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>.

### -param DevicePresenceParameters [in]

A pointer to a PCI_DEVICE_PRESENCE_PARAMETERS structure (defined in <i>Wdm.h</i>) that the caller fills in with information that identifies the device.

### -param DevicePresent [out]

A pointer to a Boolean variable that receives <b>TRUE</b> if the device is present or <b>FALSE</b> if the device is not present.

## -returns
<b>DxgkCbIsDevicePresent</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in <i>Ntstatus.h</i>.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
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