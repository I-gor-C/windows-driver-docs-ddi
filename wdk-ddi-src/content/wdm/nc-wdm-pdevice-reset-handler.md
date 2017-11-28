---
UID: NC.wdm.PDEVICE_RESET_HANDLER
title: PDEVICE_RESET_HANDLER
author: windows-driver-content
description: The DeviceReset routine is used to reset and recover a malfunctioning device.
old-location: kernel\devicereset.htm
old-project: kernel
ms.assetid: A5AA5E73-3DC1-4977-9B64-9E0FB3E6609E
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ResetDevice
req.alt-loc: Wdm.h
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
req.product: Windows 10 or later.
---

# PDEVICE_RESET_HANDLER callback



## -description
<p>The <i>DeviceReset</i> routine is used to reset and recover a malfunctioning device.</p>


## -prototype

````
PDEVICE_RESET_HANDLER ResetDevice;

NTSTATUS ResetDevice(
  _In_     PVOID             InterfaceContext,
  _In_     DEVICE_RESET_TYPE ResetType,
  _In_     ULONG             Flags,
  _In_opt_ PVOID             ResetParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>InterfaceContext</i> [in]

<dd>
<p>A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939397">DEVICE_RESET_INTERFACE_STANDARD</a> structure for the interface.</p>
</dd>

### -param <i>ResetType</i> [in]

<dd>
<p>The type of reset being  requested. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/dn939400">DEVICE_RESET_TYPE</a> enumeration values.</p>
<ul>
<li><b>FunctionLevelDeviceReset</b>. Specify this value to request a function-level reset, which is restricted to a specific device.</li>
<li><b>PlatformLevelDeviceReset</b>. Specify this value to request a platform-level reset, which affects a specific device and all other devices that are connected to it via the same power rail or reset line.</li>
</ul>
<p>For more information about how function-level and platform-level resets are implemented in the device stack, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Set to 0. Currently, no flags are defined for this routine.</p>
</dd>

### -param <i>ResetParameters</i> [in, optional]

<dd>
<p>If the caller is requesting a  function-level device reset, this optional parameter can point to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn939576">FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS</a> structure that specifies a callback routine that is called when the reset is completed.</p>
</dd>
</dl>

## -returns
<p>This routine returns STATUS_SUCCESS if the requested operation succeeds. Otherwise, it returns an appropriate an NTSTATUS error code. </p>

## -remarks
<p>If a function driver detects that the device is not functioning correctly, it should first attempt a function-level reset. If a function-level reset does not fix the issue, then the driver can attempt a more invasive platform-level reset, but a platform-level reset should only be used as the final option.

For more information about function-level and platform-level resets, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a>.</p>

<p>If a function driver detects that the device is not functioning correctly, it should first attempt a function-level reset. If a function-level reset does not fix the issue, then the driver can attempt a more invasive platform-level reset, but a platform-level reset should only be used as the final option.

For more information about function-level and platform-level resets, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DeviceReset routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
