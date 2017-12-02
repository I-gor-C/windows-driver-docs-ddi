---
UID: NF.wdm.IoWMISetSingleInstance
title: IoWMISetSingleInstance
author: windows-driver-content
description: The IoWMISetSingleInstance routine sets the values for properties within the data block instance that matches the specified WMI class and instance name.
old-location: kernel\iowmisetsingleinstance.htm
old-project: kernel
ms.assetid: 043b51cd-816f-414d-85b2-2573c42393e4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoWMISetSingleInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMISetSingleInstance
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

# IoWMISetSingleInstance function



## -description
<p>The <b>IoWMISetSingleInstance</b> routine sets the values for properties within the data block instance that matches the specified WMI class and instance name.</p>


## -syntax

````
NTSTATUS IoWMISetSingleInstance(
  _In_ PVOID           DataBlockObject,
  _In_ PUNICODE_STRING InstanceName,
  _In_ ULONG           Version,
  _In_ ULONG           ValueBufferSize,
  _In_ PVOID           ValueBuffer
);
````


## -parameters
<dl>

### -param DataBlockObject [in]

<dd>
<p>Pointer to a WMI data block object. The caller opens the data block object for the WMI class with the <a href="..\wdm\nf-wdm-iowmiopenblock.md">IoWMIOpenBlock</a> routine. The object must be opened with the WMIGUID_SET access right. </p>
</dd>

### -param InstanceName [in]

<dd>
<p>Specifies the name of the instance of the data block. This value corresponds to the value of the <b>InstanceName</b> property for the block.</p>
</dd>

### -param Version [in]

<dd>
<p>Reserved for future use. Callers must set this parameter to zero.</p>
</dd>

### -param ValueBufferSize [in]

<dd>
<p>Specifies the size, in bytes, of the buffer passed in the <i>ValueBuffer</i> parameter.</p>
</dd>

### -param ValueBuffer [in]

<dd>
<p>Pointer to the buffer that contains the new values for the properties within the data block.</p>
</dd>
</dl>

## -returns
<p>The routine returns an NTSTATUS code. Possible return values include:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation succeeded. The values of the WMI data block instance properties are updated to the contents of the buffer pointed to by the <i>ValueBuffer</i> parameter.</p><dl>
<dt><b>STATUS_WMI_GUID_NOT_FOUND</b></dt>
</dl><p>No drivers implement the WMI class.</p><dl>
<dt><b>STATUS_WMI_INSTANCE_NOT_FOUND</b></dt>
</dl><p>No driver implements an instance of the WMI class with <b>InstanceName</b> property equal to the value specified in the <i>InstanceName</i> parameter.</p><dl>
<dt><b>STATUS_WMI_READ_ONLY</b></dt>
</dl><p>All properties of the WMI class are read-only.</p><dl>
<dt><b>STATUS_WMI_SET_FAILURE</b></dt>
</dl><p>The driver that implements the WMI data block instance is unable to update the instance.</p>

<p> </p>

## -remarks
<p><b>IoWMISetSingleInstance</b> determines which drivers might support the specified WMI class and instance name, and issues an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550831">IRP_MN_CHANGE_SINGLE_INSTANCE</a> request to each such driver. The driver that exports the data block instance with matching <b>InstanceName</b> property updates its data block instance. Note that a data block might have both read-only and read/write properties. In this case, only the read/write properties will be updated and STATUS_SUCCESS is returned.</p>

<p>Drivers can also use the <a href="..\wdm\nf-wdm-iowmisetsingleitem.md">IoWMISetSingleItem</a> routine to update a single property within the class instance.</p>

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
<p>Available in Windows XP and later versions of the Windows operating system.</p>
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
<a href="..\wdm\nf-wdm-iowmiopenblock.md">IoWMIOpenBlock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iowmiquerysingleinstance.md">IoWMIQuerySingleInstance</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iowmisetsingleitem.md">IoWMISetSingleItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550831">IRP_MN_CHANGE_SINGLE_INSTANCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMISetSingleInstance routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
