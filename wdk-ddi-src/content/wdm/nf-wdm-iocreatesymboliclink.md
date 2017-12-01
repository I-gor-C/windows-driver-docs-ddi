---
UID: NF.wdm.IoCreateSymbolicLink
title: IoCreateSymbolicLink
author: windows-driver-content
description: The IoCreateSymbolicLink routine sets up a symbolic link between a device object name and a user-visible name for the device.
old-location: kernel\iocreatesymboliclink.htm
old-project: kernel
ms.assetid: be080007-f88e-4cea-b15d-58dc4ac2cb66
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoCreateSymbolicLink
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
req.alt-api: IoCreateSymbolicLink
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive3, PowerIrpDDis, HwStorPortProhibitedDDIs
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

# IoCreateSymbolicLink function



## -description
<p>The <b>IoCreateSymbolicLink</b> routine sets up a symbolic link between a device object name and a user-visible name for the device. </p>


## -syntax

````
NTSTATUS IoCreateSymbolicLink(
  _In_ PUNICODE_STRING SymbolicLinkName,
  _In_ PUNICODE_STRING DeviceName
);
````


## -parameters
<dl>

### -param <i>SymbolicLinkName</i> [in]

<dd>
<p>Pointer to a buffered Unicode string that is the user-visible name.</p>
</dd>

### -param <i>DeviceName</i> [in]

<dd>
<p>Pointer to a buffered Unicode string that is the name of the driver-created device object. </p>
</dd>
</dl>

## -returns
<p><b>IoCreateSymbolicLink</b> returns STATUS_SUCCESS if the symbolic link object was created.</p>

## -remarks
<p>WDM drivers do not name device objects and therefore should not use this routine. Instead, a WDM driver should call <a href="..\wdm\nf-wdm-ioregisterdeviceinterface.md">IoRegisterDeviceInterface</a> to set up a symbolic link. </p>

<p>For more information about when to use <b>IoCreateSymbolicLink</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556420">Named Device Objects</a>. </p>

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
<a href="devtest.wdm_irqliopassive3">IrqlIoPassive3</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioregisterdeviceinterface.md">IoRegisterDeviceInterface</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioassignarcname.md">IoAssignArcName</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iocreateunprotectedsymboliclink.md">IoCreateUnprotectedSymbolicLink</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iodeletesymboliclink.md">IoDeleteSymbolicLink</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoCreateSymbolicLink routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
