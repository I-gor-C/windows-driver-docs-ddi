---
UID: NF.wdm.IoWMISuggestInstanceName
title: IoWMISuggestInstanceName
author: windows-driver-content
description: The IoWMISuggestInstanceName routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device.
old-location: kernel\iowmisuggestinstancename.htm
ms.assetid: a07ff2f6-e67e-489e-a477-6dc4b4ce6fed
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
req.alt-api: IoWMISuggestInstanceName
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
ms.keywords: IoWMISuggestInstanceName
req.iface: 
req.product: Windows 10 or later.
---

# IoWMISuggestInstanceName function



## -description
<p>The <b>IoWMISuggestInstanceName</b> routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device.</p>


## -syntax

````
NTSTATUS IoWMISuggestInstanceName(
  _In_opt_ PDEVICE_OBJECT  PhysicalDeviceObject,
  _In_opt_ PUNICODE_STRING SymbolicLinkName,
  _In_     BOOLEAN         CombineNames,
  _Out_    PUNICODE_STRING SuggestedInstanceName
);
````


## -parameters
<dl>

### -param <i>PhysicalDeviceObject</i> [in, optional]

<dd>
<p>If supplied, points to the driver's physical device object.</p>
</dd>

### -param <i>SymbolicLinkName</i> [in, optional]

<dd>
<p>If supplied, points to the symbolic link name returned from <a href="https://msdn.microsoft.com/library/windows/hardware/ff549506">IoRegisterDeviceInterface</a>. </p>
</dd>

### -param <i>CombineNames</i> [in]

<dd>
<p>If <b>TRUE</b> then the suggested names returned will combine the <i>PhysicalDeviceObject</i> and <i>SymbolicLinkName</i> information.</p>
</dd>

### -param <i>SuggestedInstanceName</i> [out]

<dd>
<p>A pointer to a buffer which upon successful completion will contain a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> which contains the suggested instance name. The caller is responsible for freeing this buffer when it is no longer needed.</p>
</dd>
</dl>

## -returns
<p><b>IoWMISuggestInstanceName</b> returns a status code from the following list:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Indicates that WMI was able to successfully complete this function.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>Indicates that the WMI services are not available.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that insufficient resources were available to provide the caller with a buffer containing the Unicode string.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>Indicates that insufficient resources were available to provide the caller with a buffer containing the Unicode string.</p>

<p> </p>

## -remarks
<p>If the <i>CombineNames</i> parameter is <b>TRUE</b> then both <i>PhysicalDeviceObject</i> and <i>SymbolicLinkName</i> must be specified. Otherwise, only one of them should be specified.</p>

<p>If the <i>CombineNames</i> parameter is <b>TRUE</b> then both <i>PhysicalDeviceObject</i> and <i>SymbolicLinkName</i> must be specified. Otherwise, only one of them should be specified.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550429">IoWMIAllocateInstanceIds</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMISuggestInstanceName routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
