---
UID: NF.wdm.IoWMIRegistrationControl
title: IoWMIRegistrationControl
author: windows-driver-content
description: The IoWMIRegistrationControl routine registers or unregisters the caller as a WMI data provider for a specified device object.
old-location: kernel\iowmiregistrationcontrol.htm
old-project: kernel
ms.assetid: fe135118-1992-43c7-8492-81f9febd79b9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoWMIRegistrationControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMIRegistrationControl
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive5, LowerDriverReturn, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoWMIRegistrationControl function



## -description
<p>The <b>IoWMIRegistrationControl</b> routine registers or unregisters the caller as a WMI data provider for a specified device object.</p>


## -syntax

````
NTSTATUS IoWMIRegistrationControl(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ ULONG          Action
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>A pointer to a device object. This object is a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> system structure.</p>
</dd>

### -param Action [in]

<dd>
<p>The action that WMI should take. The requested action is indicated by one of the following values.</p>
<table>
<tr>
<th>Action value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WMIREG_ACTION_REGISTER</p>
</td>
<td>
<p>Specifies that WMI should register the caller as a WMI provider for <i>DeviceObject</i>. This will result in WMI sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551731">IRP_MN_REGINFO</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551734">IRP_MN_REGINFO_EX</a> request to the driver.</p>
</td>
</tr>
<tr>
<td>
<p>WMIREG_ACTION_DEREGISTER</p>
</td>
<td>
<p>Specifies that WMI should remove the caller from its list of WMI providers for <i>DeviceObject</i>.</p>
</td>
</tr>
<tr>
<td>
<p>WMIREG_ACTION_REREGISTER</p>
</td>
<td>
<p>Specifies that WMI should unregister the driver and then register (reregister) the driver. Reregistering the driver results in WMI sending an <b>IRP_MN_REGINFO</b> or <b>IRP_MN_REGINFO_EX</b> request to the driver.</p>
</td>
</tr>
<tr>
<td>
<p>WMIREG_ACTION_UPDATE_GUIDS</p>
</td>
<td>
<p>Specifies that WMI should re-query the driver for a new list of GUID identifiers that it provides data for. This will result in WMI sending an <b>IRP_MN_REGINFO</b> or <b>IRP_MN_REGINFO_EX</b> request to the driver.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>IoWMIRegistrationControl</b> returns a status code from the following list:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Indicates that WMI completed the action requested without error.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that the action, specified in <i>Action</i>, was invalid.</p><dl>
<dt><b>STATUS_<i>XXX</i></b></dt>
</dl><p>Indicates that the request failed for the reason specified by the NTSTATUS value. See Ntstatus.h for detailed information for the actual status return code.</p>

<p> </p>

## -remarks
<p>After a driver calls <b>IoWMIRegistrationControl</b>, WMI sends the driver an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551731">IRP_MN_REGINFO</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551734">IRP_MN_REGINFO_EX</a> request so the driver can provide information to WMI. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560870">Registering as a WMI Data Provider</a>.</p>

<p>If the caller specifies WMIREG_ACTION_DEREGISTER for <i>Action</i>, <b>IoWMIRegistrationControl</b> causes the calling thread to block until all <b>IRP_MJ_SYSTEM_CONTROL</b> requests that were previously sent to the specified device object have completed. In such a case, if a driver calls <b>IoWMIRegistrationControl</b> within a dispatch routine for an <b>IRP_MJ_SYSTEM_CONTROL</b> request, the calling thread will deadlock.</p>

<p>If a device is removed suddenly (for example, in a surprise removal), causing the PnP manager to send an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551760">IRP_MN_SURPRISE_REMOVAL</a> IRP, the driver must call <b>IoWMIRegistrationControl</b> and specify WMIREG_ACTION_DEREGISTER in <i>Action</i> in the call. Note that if the driver calls <b>IoWMIRegistrationControl</b> with <i>Action</i> set to WMIREG_ACTION_DEREGISTER in response to an <b>IRP_MN_SURPRISE_REMOVAL</b> IRP, the driver must not make the same call to <b>IoWMIRegistrationControl</b> in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> IRP.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqliopassive5">IrqlIoPassive5</a>, <a href="devtest.wdm_lowerdriverreturn">LowerDriverReturn</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551731">IRP_MN_REGINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551734">IRP_MN_REGINFO_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551760">IRP_MN_SURPRISE_REMOVAL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIRegistrationControl routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
