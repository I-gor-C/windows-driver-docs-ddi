---
UID: NF.hwnclx.HwNProcessAddDevicePostDeviceCreate
title: HwNProcessAddDevicePostDeviceCreate
author: windows-driver-content
description: Creates I/O queues. It should be called after the client driver’s EVT_WDF_DRIVER_DEVICE_ADD callback function is invoked and the device object has been created.
old-location: gpiobtn\hwnprocessadddevicepostdevicecreate.htm
old-project: gpiobtn
ms.assetid: 907cdeac-e2f0-48fa-bbf0-082c0fce6401
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: HwNProcessAddDevicePostDeviceCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwNProcessAddDevicePostDeviceCreate
req.alt-loc: Mshwnclxstub.lib,Mshwnclxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Mshwnclxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# HwNProcessAddDevicePostDeviceCreate function



## -description
<p>
			
             Creates I/O queues. It should be called after the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/ff541693">EVT_WDF_DRIVER_DEVICE_ADD</a> callback function is invoked and the device object has been created. </p>


## -syntax

````
FORCEINLINE NTSTATUS  HwNProcessAddDevicePostDeviceCreate(
  _In_ WDFDRIVER  Driver,
  _In_ WDFDEVICE  Device,
  _In_ LPGUID     DeviceGuid
);
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>Handle to the client drivers framework driver object. </p>
</dd>

### -param <i>Device</i> [in]

<dd>
<p>Handle to the framework device object. </p>
</dd>

### -param <i>DeviceGuid</i> [in]

<dd>
<p>Pointer to the GUID for the client driver. Valid values are defined in Hwn.h, which ships with Window SDK.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if function succeeds. Returns STATUS_INVALID_PARAMETER if corresponding client driver can't be found. Otherwise, it returns one of the error status values defined in Ntstatus.h.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hwnclx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Mshwnclxstub.lib</dt>
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
<dt><a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a></dt>
<dt>
<a href="gpiobtn.hardware_notifications_reference">Hardware notifications reference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [gpiobtn\gpiobtn]:%20HwNProcessAddDevicePostDeviceCreate function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
