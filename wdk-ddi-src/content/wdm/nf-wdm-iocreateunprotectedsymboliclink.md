---
UID: NF.wdm.IoCreateUnprotectedSymbolicLink
title: IoCreateUnprotectedSymbolicLink function
author: windows-driver-content
description: The IoCreateUnprotectedSymbolicLink routine sets up an unprotected symbolic link between a device object name and a corresponding Win32-visible name.
old-location: kernel\iocreateunprotectedsymboliclink.htm
old-project: kernel
ms.assetid: 21ca4ec1-fd5f-46bb-9760-3bb0cdb761b9
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IoCreateUnprotectedSymbolicLink
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
req.alt-api: IoCreateUnprotectedSymbolicLink
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive4, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# IoCreateUnprotectedSymbolicLink function



## -description
The <b>IoCreateUnprotectedSymbolicLink</b> routine sets up an unprotected symbolic link between a device object name and a corresponding Win32-visible name.



## -syntax

````
NTSTATUS IoCreateUnprotectedSymbolicLink(
  _In_ PUNICODE_STRING SymbolicLinkName,
  _In_ PUNICODE_STRING DeviceName
);
````


## -parameters

### -param SymbolicLinkName [in]

Supplies the symbolic link name as a Unicode string. 


### -param DeviceName [in]

Supplies the name of the device object to which the symbolic link name refers. 


## -returns
<b>IoCreateUnprotectedSymbolicLink</b> returns the final status of the operation.


## -remarks
WDM drivers do not name device objects and therefore should not use this routine. Instead, a WDM driver should call <a href="kernel.ioregisterdeviceinterface">IoRegisterDeviceInterface</a> to set up a symbolic link. 

<b>IoCreateUnprotectedSymbolicLink</b> can be used by drivers if the user needs to be able to manipulate the symbolic link. For example, the parallel and serial drivers create unprotected symbolic links for LPTx and COMx, so that users can manipulate and reassign them by using the MODE command.

In general, drivers should call this routine instead of <a href="kernel.iocreatesymboliclink">IoCreateSymbolicLink</a> if a protected subsystem lets end users change what a named device references as, for example, when using LPT1 to access a network printer.

For more information about when to use <b>IoCreateSymbolicLink</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556420">Named Device Objects</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqliopassive4">IrqlIoPassive4</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioregisterdeviceinterface">IoRegisterDeviceInterface</a>
</dt>
<dt>
<a href="kernel.ioassignarcname">IoAssignArcName</a>
</dt>
<dt>
<a href="kernel.iocreatesymboliclink">IoCreateSymbolicLink</a>
</dt>
<dt>
<a href="kernel.iodeletesymboliclink">IoDeleteSymbolicLink</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoCreateUnprotectedSymbolicLink routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

