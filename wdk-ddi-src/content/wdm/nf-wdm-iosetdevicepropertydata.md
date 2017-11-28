---
UID: NF.wdm.IoSetDevicePropertyData
title: IoSetDevicePropertyData
author: windows-driver-content
description: The IoSetDevicePropertyData routine modifies the current setting for a device property.
old-location: kernel\iosetdevicepropertydata.htm
old-project: kernel
ms.assetid: 8e535a6a-9b17-4ef6-b068-43042a589ac0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoSetDevicePropertyData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetDevicePropertyData
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoSetDevicePropertyData function



## -description
<p>The <b>IoSetDevicePropertyData</b> routine modifies the current setting for a device property.</p>


## -syntax

````
NTSTATUS IoSetDevicePropertyData(
  _In_           PDEVICE_OBJECT Pdo,
  _In_     const DEVPROPKEY     *PropertyKey,
  _In_           LCID           Lcid,
  _In_           ULONG          Flags,
  _In_           DEVPROPTYPE    Type,
  _In_           ULONG          Size,
  _In_opt_       PVOID          Data
);
````


## -parameters
<dl>

### -param <i>Pdo</i> [in]

<dd>
<p>A pointer to the physical device object (PDO) for the device that is being queried.</p>
</dd>

### -param <i>PropertyKey</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> structure that specifies the device property key.</p>
</dd>

### -param <i>Lcid</i> [in]

<dd>
<p>A locale identifier. Set this parameter either to a language-specific LCID value or to <b>LOCALE_NEUTRAL</b>.</p>
<p>The <b>LOCALE_NEUTRAL</b> LCID specifies that the property is language-neutral (that is, not specific to any language).</p>
<p>Do not set this parameter to <b>LOCALE_SYSTEM_DEFAULT</b> or <b>LOCALE_USER_DEFAULT</b>.</p>
<p>For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Set this parameter to <b>PLUGPLAY_PROPERTY_PERSISTENT</b> if the property value set by this routine should persist across computer restarts. Otherwise, set <i>Flags</i> to zero.</p>
<p>Windows 8 and Windows Server 2012 and later operating systems treat <b>Flags</b> as if <b>PLUGPLAY_PROPERTY_PERSISTENT</b>  is always passed.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a> value that specifies the type of the data that is provided in the <i>Data</i> buffer.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>The size, in bytes, of the buffer that <i>Data</i> points to.</p>
</dd>

### -param <i>Data</i> [in, optional]

<dd>
<p>A pointer to the device property data. Set this parameter to <b>NULL</b> to delete the specified property. If <i>Data</i> is non-<b>NULL</b>, the routine stores an internal copy of the property value. The buffer pointed to by <i>Data</i> does not need to remain valid after the call returns.</p>
</dd>
</dl>

## -returns
<p><b>IoSetDevicePropertyData</b> returns STATUS_SUCCESS if the call was successful, or the appropriate NTSTATUS code on failure.</p>

## -remarks
<p>Kernel-mode drivers use the <b>IoSetDevicePropertyData</b> routine to modify device properties that are defined as part of the unified device property model. For more information about device properties, see <a href="NULL">Device Properties</a>.</p>

<p>To delete a property for a specific locale, pass a language-specific LCID value in <i>Lcid</i> and <b>NULL</b> in <i>Data</i>.</p>

<p>To delete a property for all locales, pass <b>LOCALE_NEUTRAL</b> in <i>Lcid</i> and <b>NULL</b> in <i>Data</i>.</p>

<p>To modify a property for a specific locale, pass a language-specific LCID value in <i>Lcid</i> and non-<b>NULL</b> in <i>Data</i>.</p>

<p>To modify a property for all locales, pass <b>LOCALE_NEUTRAL</b> in <i>Lcid</i> and non-<b>NULL</b> in <i>Data</i>.</p>

<p>Beginning with Windows 8 and Windows Server 2012 passing <b>LOCALE_NEUTRAL</b> in <i>Lcid</i> is treated like any other locale.</p>

<p>Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549206">IoGetDevicePropertyData</a> routine to obtain the current value for a device property.</p>

<p>Callers of <b>IoSetDeviceProperty</b> must be running at IRQL &lt;= APC_LEVEL in the context of a system thread.</p>

<p>Kernel-mode drivers use the <b>IoSetDevicePropertyData</b> routine to modify device properties that are defined as part of the unified device property model. For more information about device properties, see <a href="NULL">Device Properties</a>.</p>

<p>To delete a property for a specific locale, pass a language-specific LCID value in <i>Lcid</i> and <b>NULL</b> in <i>Data</i>.</p>

<p>To delete a property for all locales, pass <b>LOCALE_NEUTRAL</b> in <i>Lcid</i> and <b>NULL</b> in <i>Data</i>.</p>

<p>To modify a property for a specific locale, pass a language-specific LCID value in <i>Lcid</i> and non-<b>NULL</b> in <i>Data</i>.</p>

<p>To modify a property for all locales, pass <b>LOCALE_NEUTRAL</b> in <i>Lcid</i> and non-<b>NULL</b> in <i>Data</i>.</p>

<p>Beginning with Windows 8 and Windows Server 2012 passing <b>LOCALE_NEUTRAL</b> in <i>Lcid</i> is treated like any other locale.</p>

<p>Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549206">IoGetDevicePropertyData</a> routine to obtain the current value for a device property.</p>

<p>Callers of <b>IoSetDeviceProperty</b> must be running at IRQL &lt;= APC_LEVEL in the context of a system thread.</p>

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
<p>Available starting with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549206">IoGetDevicePropertyData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetDevicePropertyData routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
