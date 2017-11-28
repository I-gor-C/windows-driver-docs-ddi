---
UID: NF.wdm.ZwEnumerateValueKey
title: ZwEnumerateValueKey
author: windows-driver-content
description: The ZwEnumerateValueKey routine gets information about the value entries of an open key.
old-location: kernel\zwenumeratevaluekey.htm
old-project: kernel
ms.assetid: 4e94c9cc-eaa9-4de1-8f17-d24a5ed19507
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwEnumerateValueKey
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
req.alt-api: ZwEnumerateValueKey,NtEnumerateValueKey
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlZwPassive, PowerIrpDDis, ZwRegistryCreate, ZwRegistryOpen, HwStorPortProhibitedDDIs, ZwRegistryCreate(storport), ZwRegistryOpen(storport)
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

# ZwEnumerateValueKey function



## -description
<p>The <b>ZwEnumerateValueKey</b> routine gets information about the value entries of an open key.</p>


## -syntax

````
NTSTATUS ZwEnumerateValueKey(
  _In_      HANDLE                      KeyHandle,
  _In_      ULONG                       Index,
  _In_      KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
  _Out_opt_ PVOID                       KeyValueInformation,
  _In_      ULONG                       Length,
  _Out_     PULONG                      ResultLength
);
````


## -parameters
<dl>

### -param <i>KeyHandle</i> [in]

<dd>
<p>Handle to the registry key that you want to enumerate value entries for. A successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567014">ZwOpenKey</a> creates this handle.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>The zero-based index of the subkey that you want value information for.</p>
</dd>

### -param <i>KeyValueInformationClass</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554218">KEY_VALUE_INFORMATION_CLASS</a> value that determines the type of information returned in the <i>KeyValueInformation</i> buffer.</p>
</dd>

### -param <i>KeyValueInformation</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated buffer that receives the requested information.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the size, in bytes, of the <i>KeyValueInformation</i> buffer.</p>
</dd>

### -param <i>ResultLength</i> [out]

<dd>
<p>Pointer to a variable that receives the size, in bytes, of the value information. If this routine returns STATUS_SUCCESS, the variable indicates the amount of data returned. If this routine returns STATUS_BUFFER_OVERFLOW or STATUS_BUFFER_TOO_SMALL, the variable indicates the buffer size that is required to hold the value information. </p>
</dd>
</dl>

## -returns
<p><b>ZwEnumerateValueKey</b> returns STATUS_SUCCESS on success, or the appropriate error code on failure. Possible error code values include:</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The buffer supplied is too small, and only partial data has been written to the buffer. *<i>ResultLength</i> is set to the minimum size required to hold the requested information. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer supplied is too small, and no data has been written to the buffer. *<i>ResultLength</i> is set to the minimum size required to hold the requested information. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>KeyInformationClass</i> parameter is not a valid KEY_VALUE_INFORMATION_CLASS value. </p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>The <i>Index</i> value is out of range for the registry key specified by <i>KeyHandle</i>. For example, if a key has <i>n</i> subkeys, then for any value greater than <i>n</i>-1 the routine returns STATUS_NO_MORE_ENTRIES. </p>

<p> </p>

## -remarks
<p>The<i> KeyHandle</i> passed to <b>ZwEnumerateValueKey</b> must have been opened with KEY_QUERY_VALUE access. This is accomplished by passing KEY_QUERY_VALUE, KEY_READ, or KEY_ALL_ACCESS as the <i>DesiredAccess</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567014">ZwOpenKey</a>.</p>

<p>The <i>Index</i> is simply a way to select among subkeys with value entries. Two calls to <b>ZwEnumerateValueKey</b> with the same <i>Index</i> are not guaranteed to return the same results.</p>

<p>For more information about working with registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>The<i> KeyHandle</i> passed to <b>ZwEnumerateValueKey</b> must have been opened with KEY_QUERY_VALUE access. This is accomplished by passing KEY_QUERY_VALUE, KEY_READ, or KEY_ALL_ACCESS as the <i>DesiredAccess</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567014">ZwOpenKey</a>.</p>

<p>The <i>Index</i> is simply a way to select among subkeys with value entries. Two calls to <b>ZwEnumerateValueKey</b> with the same <i>Index</i> are not guaranteed to return the same results.</p>

<p>For more information about working with registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547897">IrqlZwPassive</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556228">ZwRegistryCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556231">ZwRegistryOpen</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_zwregistrycreate">ZwRegistryCreate(storport)</a>, <a href="devtest.storport_zwregistryopen">ZwRegistryOpen(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553410">KEY_VALUE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554217">KEY_VALUE_FULL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554220">KEY_VALUE_PARTIAL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567014">ZwOpenKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567069">ZwQueryValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwEnumerateValueKey routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
