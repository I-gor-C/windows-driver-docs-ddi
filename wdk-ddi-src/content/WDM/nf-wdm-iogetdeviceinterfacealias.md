---
UID: NF.wdm.IoGetDeviceInterfaceAlias
title: IoGetDeviceInterfaceAlias
author: windows-driver-content
description: The IoGetDeviceInterfaceAlias routine returns the alias device interface of the specified device interface instance, if the alias exists.
old-location: kernel\iogetdeviceinterfacealias.htm
ms.assetid: 667c9524-be12-4f02-b921-6067abfb1dde
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
req.alt-api: IoGetDeviceInterfaceAlias
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
ms.keywords: IoGetDeviceInterfaceAlias
req.iface: 
req.product: Windows 10 or later.
---

# IoGetDeviceInterfaceAlias function



## -description
<p>The <b>IoGetDeviceInterfaceAlias</b> routine returns the alias device interface of the specified device interface instance, if the alias exists.</p>


## -syntax

````
NTSTATUS IoGetDeviceInterfaceAlias(
  _In_        PUNICODE_STRING SymbolicLinkName,
  _In_  const GUID            *AliasInterfaceClassGuid,
  _Out_       PUNICODE_STRING AliasSymbolicLinkName
);
````


## -parameters
<dl>

### -param <i>SymbolicLinkName</i> [in]

<dd>
<p>Pointer to the name of the device interface instance for which to retrieve an alias. The caller typically received this string from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549186">IoGetDeviceInterfaces</a> or in a PnP notification structure.</p>
</dd>

### -param <i>AliasInterfaceClassGuid</i> [in]

<dd>
<p>Pointer to a GUID specifying the interface class of the alias to retrieve.</p>
</dd>

### -param <i>AliasSymbolicLinkName</i> [out]

<dd>
<p>Specifies a pointer to a <b>NULL</b> Unicode string. On successful return, <i>AliasSymbolicLinkName</i>.<b>Buffer</b> points to a string containing the name of the alias. The caller must free the Unicode string with <a href="https://msdn.microsoft.com/library/windows/hardware/ff561903">RtlFreeUnicodeString</a> when it is no longer needed.</p>
</dd>
</dl>

## -returns
<p><b>IoGetDeviceInterfaceAlias</b> returns STATUS_SUCCESS if the call was successful. Possible error return values are described following.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>Possibly indicates that there is no alias of the specified interface class.</p><dl>
<dt><b>STATUS_OBJECT_PATH_NOT_FOUND</b></dt>
</dl><p>Possibly indicates that there is no alias of the specified interface class.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>Possibly indicates an invalid <i>SymbolicLinkName</i> or an invalid <i>AliasClassGuid</i>.</p>

<p> </p>

## -remarks
<p>Device interfaces are considered aliases if they are exposed by the same underlying device and have identical interface reference strings, but are of different interface classes.</p>

<p>The <i>SymbolicLinkName</i> parameter specifies a device interface instance for a particular device, belonging to a particular interface class, with a particular reference string. <b>IoGetDeviceInterfaceAlias</b> returns another device interface instance for the same device and reference string, but of a different interface class, if it exists.</p>

<p>For example, the function driver for a fault-tolerant volume could register and set two device interfaces, one of the fault-tolerant-volume interface class and one of the volume interface class. Another driver could call <b>IoGetDeviceInterfaceAlias</b> with the symbolic link for one of the interfaces and ask whether the other interface exists by specifying its interface class.</p>

<p>Two device interfaces with <b>NULL</b> reference strings are aliases if they are exposed by the same underlying device and have different interface class GUIDs.</p>

<p>Callers of <b>IoGetDeviceInterfaceAlias</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

<p>Device interfaces are considered aliases if they are exposed by the same underlying device and have identical interface reference strings, but are of different interface classes.</p>

<p>The <i>SymbolicLinkName</i> parameter specifies a device interface instance for a particular device, belonging to a particular interface class, with a particular reference string. <b>IoGetDeviceInterfaceAlias</b> returns another device interface instance for the same device and reference string, but of a different interface class, if it exists.</p>

<p>For example, the function driver for a fault-tolerant volume could register and set two device interfaces, one of the fault-tolerant-volume interface class and one of the volume interface class. Another driver could call <b>IoGetDeviceInterfaceAlias</b> with the symbolic link for one of the interfaces and ask whether the other interface exists by specifying its interface class.</p>

<p>Two device interfaces with <b>NULL</b> reference strings are aliases if they are exposed by the same underlying device and have different interface class GUIDs.</p>

<p>Callers of <b>IoGetDeviceInterfaceAlias</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549506">IoRegisterDeviceInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561903">RtlFreeUnicodeString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetDeviceInterfaceAlias routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
