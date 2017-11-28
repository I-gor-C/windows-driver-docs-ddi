---
UID: NF.wdm.IoSetDeviceInterfacePropertyData
title: IoSetDeviceInterfacePropertyData
author: windows-driver-content
description: The IoSetDeviceInterfacePropertyData routine modifies the current value of a device interface property.
old-location: kernel\iosetdeviceinterfacepropertydata.htm
old-project: kernel
ms.assetid: 346F6FEC-7E06-4DF0-A304-88BD830C591B
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoSetDeviceInterfacePropertyData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available for Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetDeviceInterfacePropertyData
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoSetDeviceInterfacePropertyData function



## -description
<p>The <b>IoSetDeviceInterfacePropertyData</b> routine modifies the current value of a <a href="https://msdn.microsoft.com/43aa0ce6-a06b-43e4-a213-300554391ae0">device interface property</a>.</p>


## -syntax

````
NTSTATUS IoSetDeviceInterfacePropertyData(
  _In_     PUNICODE_STRING  SymbolicLinkName,
  _In_     CONST DEVPROPKEY *PropertyKey,
  _In_     LCID             Lcid,
  _In_     ULONG            Flags,
  _In_     DEVPROPTYPE      Type,
  _In_     ULONG            Size,
  _In_opt_ PVOID            Data
);
````


## -parameters
<dl>

### -param <i>SymbolicLinkName</i> [in]

<dd>
<p>A pointer to a string that identifies the device interface instance. This string was obtained from a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549186">IoGetDeviceInterfaces</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549180">IoGetDeviceInterfaceAlias</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549506">IoRegisterDeviceInterface</a> routine.</p>
</dd>

### -param <i>PropertyKey</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> structure that contains the device interface property key.</p>
</dd>

### -param <i>Lcid</i> [in]

<dd>
<p>Specifies a locale identifier. Set this parameter either to a language-specific LCID value or to <b>LOCALE_NEUTRAL</b>. The <b>LOCALE_NEUTRAL</b> LCID specifies that the property is language-neutral (that is, not specific to any language). Do not set this parameter to <b>LOCALE_SYSTEM_DEFAULT</b> or <b>LOCALE_USER_DEFAULT</b>. For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Set this parameter to <b>PLUGPLAY_PROPERTY_PERSISTENT</b> if the property value set by this routine should persist across computer restarts. Otherwise, set <i>Flags</i> to zero.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>Set this parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a> value that specifies the type of the data that is supplied in the <i>Data</i> buffer.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer that <i>Data</i> points to.</p>
</dd>

### -param <i>Data</i> [in, optional]

<dd>
<p>A pointer to the device interface property data. Set this parameter to <b>NULL</b> to delete the specified property. If <i>Data</i> is non-<b>NULL</b>, the routine stores an internal copy of the property value. The buffer pointed to by <i>Data</i> does not need to remain valid after the call returns.</p>
</dd>
</dl>

## -returns
<p><b>IoSetDeviceInterfacePropertyData</b> returns STATUS_SUCCESS if the call was successful. Possible error return values include the following status codes.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The specified LCID value is not valid.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>The specified property is not supported.</p>

<p> </p>

## -remarks
<p>Kernel-mode drivers use the <b>IoSetDeviceInterfacePropertyData</b> routine to modify device interface properties that are defined as part of the <a href="NULL">unified device property model</a>. For more information about device interface properties, see <a href="NULL">Device Properties</a>.</p>

<p>Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439313">IoGetDeviceInterfacePropertyData</a> routine to obtain the current value for a device interface property.</p>

<p>Callers of <b>IoSetDeviceInterfacePropertyData</b> must be running at IRQL &lt;= APC_LEVEL in the context of a system thread.</p>

<p>Kernel-mode drivers use the <b>IoSetDeviceInterfacePropertyData</b> routine to modify device interface properties that are defined as part of the <a href="NULL">unified device property model</a>. For more information about device interface properties, see <a href="NULL">Device Properties</a>.</p>

<p>Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439313">IoGetDeviceInterfacePropertyData</a> routine to obtain the current value for a device interface property.</p>

<p>Callers of <b>IoSetDeviceInterfacePropertyData</b> must be running at IRQL &lt;= APC_LEVEL in the context of a system thread.</p>

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
<p>Available for Windows 8 and later versions of Windows.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439313">IoGetDeviceInterfacePropertyData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetDeviceInterfacePropertyData routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
