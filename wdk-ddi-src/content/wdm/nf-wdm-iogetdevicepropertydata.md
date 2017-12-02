---
UID: NF.wdm.IoGetDevicePropertyData
title: IoGetDevicePropertyData
author: windows-driver-content
description: The IoGetDevicePropertyData routine retrieves the current setting for a device property.
old-location: kernel\iogetdevicepropertydata.htm
old-project: kernel
ms.assetid: 3ca026b8-abed-409c-8be4-01553cfadca3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoGetDevicePropertyData
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
req.alt-api: IoGetDevicePropertyData
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

# IoGetDevicePropertyData function



## -description
<p>The <b>IoGetDevicePropertyData</b> routine retrieves the current setting for a device property.</p>


## -syntax

````
NTSTATUS IoGetDevicePropertyData(
  _In_             PDEVICE_OBJECT Pdo,
  _In_       const DEVPROPKEY     *PropertyKey,
  _In_             LCID           Lcid,
  _Reserved_       ULONG          Flags,
  _In_             ULONG          Size,
  _Out_            PVOID          Data,
  _Out_            PULONG         RequiredSize,
  _Out_            PDEVPROPTYPE   Type
);
````


## -parameters
<dl>

### -param Pdo [in]

<dd>
<p>A pointer to the physical device object (PDO) for the device that is being queried.</p>
</dd>

### -param PropertyKey [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> structure that specifies the device property key.</p>
</dd>

### -param Lcid [in]

<dd>
<p>A locale identifier. Set this parameter either to a language-specific LCID value or to <b>LOCALE_NEUTRAL</b>. The <b>LOCALE_NEUTRAL</b> LCID specifies that the property is language-neutral (that is, not specific to any language). Do not set this parameter to <b>LOCALE_SYSTEM_DEFAULT</b> or <b>LOCALE_USER_DEFAULT</b>. For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.</p>
</dd>

### -param Flags 

<dd>
<p>Reserved for system use. Drivers should set this value to 0.</p>
</dd>

### -param Size [in]

<dd>
<p>The size, in bytes, of the buffer that <i>Data</i> points to.</p>
</dd>

### -param Data [out]

<dd>
<p>A pointer to the device property data.</p>
</dd>

### -param RequiredSize [out]

<dd>
<p>A pointer to a ULONG to receive the size of the property information that is returned at <i>Data</i>. If <b>IoGetDevicePropertyData</b> returns STATUS_BUFFER_TOO_SMALL, the caller can use this value to allocate a buffer of the correct size.</p>
</dd>

### -param Type [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a> value. If <b>IoGetDevicePropertyData</b> completes successfully, the routine uses <i>Type</i> to supply the type of data that is returned in the <i>Data</i> buffer.</p>
</dd>
</dl>

## -returns
<p><b>IoGetDevicePropertyData</b> returns an NTSTATUS value. This routine might return one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation succeeded. The <i>Data</i> buffer contains the retrieved data. *<i>Type</i> contains the type of the retrieved data.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The <i>Data</i> buffer is too small. *<i>RequiredSize</i> contains the required buffer length.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The specified device property was not found.</p>

<p> </p>

## -remarks
<p>Kernel-mode drivers use the <b>IoGetDevicePropertyData</b> routine to retrieve device properties that are defined as part of the unified device property model. For more information about device properties, see <a href="https://msdn.microsoft.com/f41040c5-0eac-450d-b532-9165c543cc1a">Device Properties</a>.</p>

<p>Drivers can use the <a href="..\wdm\nf-wdm-iosetdevicepropertydata.md">IoSetDevicePropertyData</a> routine to modify a device property.</p>

<p>Callers of <b>IoGetDevicePropertyData</b> must be running at IRQL &lt;= APC_LEVEL in the context of a system thread.</p>

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
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
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
<a href="..\wdm\nf-wdm-iosetdevicepropertydata.md">IoSetDevicePropertyData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetDevicePropertyData routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
