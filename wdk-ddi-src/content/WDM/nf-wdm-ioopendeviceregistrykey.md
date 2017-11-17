---
UID: NF.wdm.IoOpenDeviceRegistryKey
title: IoOpenDeviceRegistryKey
author: windows-driver-content
description: The IoOpenDeviceRegistryKey routine returns a handle to a device-specific or a driver-specific registry key for a particular device instance.
old-location: kernel\ioopendeviceregistrykey.htm
ms.assetid: c3b67c73-446b-42a8-bc41-2ca42fde3513
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
req.alt-api: IoOpenDeviceRegistryKey
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: IoOpenDeviceRegistryKey
req.iface: 
req.product: Windows 10 or later.
---

# IoOpenDeviceRegistryKey function



## -description
<p>The <b>IoOpenDeviceRegistryKey</b> routine returns a handle to a device-specific or a driver-specific registry key for a particular device instance. </p>


## -syntax

````
NTSTATUS IoOpenDeviceRegistryKey(
  _In_  PDEVICE_OBJECT DeviceObject,
  _In_  ULONG          DevInstKeyType,
  _In_  ACCESS_MASK    DesiredAccess,
  _Out_ PHANDLE        DevInstRegKey
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the PDO of the device instance for which the registry key is to be opened.</p>
</dd>

### -param <i>DevInstKeyType</i> [in]

<dd>
<p>Specifies flags indicating whether to open a device-specific hardware key or a driver-specific software key. The flags also indicate whether the key is relative to the current hardware profile. For more information about hardware and software keys, see <a href="devinst.overview_of_registry_trees_and_keys">Registry Keys for Drivers</a>.</p>
<p>The flags are defined as follows:</p>
<p></p>
<dl>

### -param <a id="PLUGPLAY_REGKEY_DEVICE"></a><a id="plugplay_regkey_device"></a>PLUGPLAY_REGKEY_DEVICE

<dd>
<p>Open the <b>Device Parameters</b> subkey under the device's <a href="wdkgloss.h#wdkgloss.hardware_key#wdkgloss.hardware_key"><i>hardware key</i></a>. The key is located under the key for the device instance specified by <i>DeviceObject</i>. This flag cannot be specified with PLUGPLAY_REGKEY_DRIVER.</p>
</dd>

### -param <a id="PLUGPLAY_REGKEY_DRIVER"></a><a id="plugplay_regkey_driver"></a>PLUGPLAY_REGKEY_DRIVER

<dd>
<p>Open a <a href="wdkgloss.s#wdkgloss.software_key#wdkgloss.software_key"><i>software key</i></a> for storing driver-specific information. This flag cannot be specified with PLUGPLAY_REGKEY_DEVICE.</p>
</dd>

### -param <a id="PLUGPLAY_REGKEY_CURRENT_HWPROFILE"></a><a id="plugplay_regkey_current_hwprofile"></a>PLUGPLAY_REGKEY_CURRENT_HWPROFILE

<dd>
<p>Open a key relative to the current hardware profile for device or driver information. This allows the driver to access configuration information that is hardware-profile-specific. The caller must specify either PLUGPLAY_REGKEY_DEVICE or PLUGPLAY_REGKEY_DRIVER with this flag. </p>
</dd>
</dl>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that represents the access the caller needs to the key. See the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> routine for a description of each KEY_<i>XXX</i> access right.</p>
</dd>

### -param <i>DevInstRegKey</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that, on successful return, contains a handle to the requested registry key. </p>
</dd>
</dl>

## -returns
<p><b>IoOpenDeviceRegistryKey</b> returns STATUS_SUCCESS if the call was successful. Possible error return values include the following.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Possibly indicates that the caller specified an illegal set of <i>DevInstKeyType</i> flags.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>Possibly indicates that the <i>DeviceObject</i> is not a valid PDO.</p>

<p> </p>

## -remarks
<p>The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> to close the handle returned from this routine when access is no longer required.</p>

<p>The registry keys opened by this routine are nonvolatile.</p>

<p>User-mode setup applications, such as <a href="wdkgloss.c#wdkgloss.class_installer#wdkgloss.class_installer"><i>class installers</i></a>, can access these registry keys using <a href="https://msdn.microsoft.com/library/windows/hardware/ff541299">device installation functions</a> such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff552079">SetupDiOpenDevRegKey</a>.</p>

<p>To create registry keys, use <a href="devinst.inf_addreg_directive">INF AddReg directives</a> in an INF file or use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550973">SetupDiCreateDevRegKey</a> in a setup application.</p>

<p>Callers of <b>IoOpenDeviceRegistryKey</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread. </p>

<p>The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> to close the handle returned from this routine when access is no longer required.</p>

<p>The registry keys opened by this routine are nonvolatile.</p>

<p>User-mode setup applications, such as <a href="wdkgloss.c#wdkgloss.class_installer#wdkgloss.class_installer"><i>class installers</i></a>, can access these registry keys using <a href="https://msdn.microsoft.com/library/windows/hardware/ff541299">device installation functions</a> such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff552079">SetupDiOpenDevRegKey</a>.</p>

<p>To create registry keys, use <a href="devinst.inf_addreg_directive">INF AddReg directives</a> in an INF file or use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550973">SetupDiCreateDevRegKey</a> in a setup application.</p>

<p>Callers of <b>IoOpenDeviceRegistryKey</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread. </p>

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
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoOpenDeviceRegistryKey routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
