---
UID: NF.ntddk.ZwOpenProcess
title: ZwOpenProcess
author: windows-driver-content
description: The ZwOpenProcess routine opens a handle to a process object and sets the access rights to this object.
old-location: kernel\zwopenprocess.htm
old-project: kernel
ms.assetid: 261d7676-9ce7-4e15-a58f-0439434f202b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwOpenProcess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwOpenProcess,NtOpenProcess
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ZwOpenProcess function



## -description
<p>The <b>ZwOpenProcess</b> routine opens a handle to a process object and sets the access rights to this object.</p>


## -syntax

````
NTSTATUS ZwOpenProcess(
  _Out_    PHANDLE            ProcessHandle,
  _In_     ACCESS_MASK        DesiredAccess,
  _In_     POBJECT_ATTRIBUTES ObjectAttributes,
  _In_opt_ PCLIENT_ID         ClientId
);
````


## -parameters
<dl>

### -param <i>ProcessHandle</i> [out]

<dd>
<p>A pointer to a variable of type HANDLE. The <b>ZwOpenProcess</b> routine writes the process handle to the variable that this parameter points to.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that contains the access rights that the caller has requested to the process object.</p>
</dd>

### -param <i>ObjectAttributes</i> [in]

<dd>
<p>A pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies the attributes to apply to the process object handle. In Windows Vista and later versions of Windows, the <b>ObjectName</b> field of this structure must be set to <b>NULL</b>. In Windows Server 2003, Windows XP, and Windows 2000, this field can, as an option, point to an object name. For more information, see the following Remarks section.</p>
</dd>

### -param <i>ClientId</i> [in, optional]

<dd>
<p>A pointer to a client ID that identifies the thread whose process is to be opened. In Windows Vista and later versions of Windows, this parameter must be a non-<b>NULL</b> pointer to a valid client ID. In Windows Server 2003, Windows XP, and Windows 2000, this parameter is optional and can be set to <b>NULL</b> if the <b>OBJECT_ATTRIBUTES</b> structure that <i>ObjectAttributes</i> points to specifies an object name. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><b>ZwOpenProcess</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error status codes.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_MIX</b></dt>
</dl><p>In Windows Vista and later versions of Windows, the caller either supplied an object name or failed to supply a client ID. In Windows Server 2003, Windows XP, and Windows 2000, the caller supplied both an object name and a client ID.</p><dl>
<dt><b>STATUS_INVALID_CID</b></dt>
</dl><p>The specified client ID is not valid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The requested access rights are not valid for a process object.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The requested access rights cannot be granted.</p>

<p> </p>

## -remarks
<p>In Windows Vista and later versions of Windows, the <i>ClientId</i> parameter must point to a client ID that identifies the thread whose process is to be opened. In addition, the <b>ObjectName</b> field of the structure pointed to by <i>ObjectAttributes</i> must be set to <b>NULL</b>.</p>

<p>In Windows Server 2003, Windows XP, and Windows 2000, the caller has the option of supplying either a client ID or an object name (but not both). If the <b>ObjectName</b> field of the structure pointed to by <i>ObjectAttributes</i> contains a non-<b>NULL</b> pointer to an object name, <i>ClientId</i> must be <b>NULL</b>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
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
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenProcess routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
