---
UID : NF:wdm.RtlQueryRegistryValues
title : RtlQueryRegistryValues function
author : windows-driver-content
description : The RtlQueryRegistryValues routine allows the caller to query several values from the registry subtree with a single call.
old-location : kernel\rtlqueryregistryvalues.htm
old-project : kernel
ms.assetid : 6c6d0664-0c00-461b-bcac-13070511430c
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : wdm/RtlQueryRegistryValues, RtlQueryRegistryValues routine [Kernel-Mode Driver Architecture], RtlQueryRegistryValues, k109_5a8cb907-8c49-4a88-9494-ff137cf6507d.xml, kernel.rtlqueryregistryvalues
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ntoskrnl.lib
req.dll : Ntoskrnl.exe
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# RtlQueryRegistryValues function
The <b>RtlQueryRegistryValues</b> routine allows the caller to query several values from the registry subtree with a single call.

## Syntax

````
NTSTATUS RtlQueryRegistryValues(
  _In_     ULONG                     RelativeTo,
  _In_     PCWSTR                    Path,
  _Inout_  PRTL_QUERY_REGISTRY_TABLE QueryTable,
  _In_opt_ PVOID                     Context,
  _In_opt_ PVOID                     Environment
);
````

## Parameters

`RelativeTo`

Specifies whether <i>Path</i> is an absolute registry path or is relative to a predefined path as one of the following.
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
RTL_REGISTRY_ABSOLUTE

</td>
<td>
Path is an absolute registry path.

</td>
</tr>
<tr>
<td>
RTL_REGISTRY_CONTROL

</td>
<td>
Path is relative to <b>\Registry\Machine\System\CurrentControlSet\Control</b>.

</td>
</tr>
<tr>
<td>
RTL_REGISTRY_DEVICEMAP

</td>
<td>
Path is relative to <b>\Registry\Machine\Hardware\DeviceMap</b>.

</td>
</tr>
<tr>
<td>
RTL_REGISTRY_SERVICES

</td>
<td>
Path is relative to <b>\Registry\Machine\System\CurrentControlSet\Services</b>.

</td>
</tr>
<tr>
<td>
RTL_REGISTRY_USER

</td>
<td>
Path is relative to <b>\Registry\User\CurrentUser</b>. (For a system process, this is <b>\User\.Default</b>.)

</td>
</tr>
<tr>
<td>
RTL_REGISTRY_WINDOWS_NT

</td>
<td>
Path is relative to <b>\Registry\Machine\Software\Microsoft\Windows NT\CurrentVersion</b>.

</td>
</tr>
</table> 

The <i>RelativeTo</i> value can be modified by bitwise-ORing it with one of the following flags.
<table>
<tr>
<td>
RTL_REGISTRY_OPTIONAL

</td>
<td>
Specifies that the key referenced by this parameter and the <i>Path</i> parameter are optional.

</td>
</tr>
<tr>
<td>
RTL_REGISTRY_HANDLE

</td>
<td>
Specifies that the <i>Path</i> parameter is actually a registry handle to use.

</td>
</tr>
</table>

`Path`

Pointer to either an absolute registry path or a path relative to the known location specified by the <i>RelativeTo</i> parameter. Note that the names of keys in such a path must be known to the caller, including the last key in the path. If the RTL_REGISTRY_HANDLE flag is specified, this parameter is a registry handle for an already opened key to be queried directly.

`QueryTable`

Pointer to a table of one or more value names and subkey names in which the caller is interested. Each table entry contains the address of a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff559969">QueryRoutine</a> function that will be called for each value name that exists in the registry. The table must be terminated with a <b>NULL</b> table entry, which is a table entry with a <b>NULL</b> <b>QueryRoutine</b> member and a <b>NULL</b> <b>Name</b> member. The structure for query table entries is defined as follows:
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _RTL_QUERY_REGISTRY_TABLE {
    PRTL_QUERY_REGISTRY_ROUTINE QueryRoutine;
    ULONG Flags;
    PWSTR Name;
    PVOID EntryContext;
    ULONG DefaultType;
    PVOID DefaultData;
    ULONG DefaultLength;
} RTL_QUERY_REGISTRY_TABLE, *PRTL_QUERY_REGISTRY_TABLE;</pre>
</td>
</tr>
</table></span></div>If the caller allocates storage for the query table pointed to by the <i>QueryTable</i> parameter, the caller is responsible for releasing this storage after the <b>RtlQueryRegistryValues</b> call returns.

`Context`

Specifies the value passed as the <i>Context</i> parameter of a <i>QueryRoutine</i> function each time it is called.

`Environment`

Pointer to the environment used when expanding variable values in REG_EXPAND_SZ registry values, or a <b>NULL</b> pointer (optional).


## Return Value

<b>RtlQueryRegistryValues</b> returns an NTSTATUS code. The possible return values include:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The entire query table was processed successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
Processing of the query table terminated with an invalid table entry. A table entry can be invalid if the specified flags require the <b>QueryRoutine</b> or <b>Name</b> member to be non-<b>NULL</b>, but a <b>NULL</b> value was provided.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl>
</td>
<td width="60%">
The <i>Path</i> parameter does not match a valid key, or processing of the query table terminated with an entry with the RTL_QUERY_REGISTRY_REQUIRED flag set and no matching key is found. This occurs if the <b>Name</b> member is <b>NULL</b> and the current key has no subkeys, or if <b>Name</b> specifies a nonexistent subkey.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>
</td>
<td width="60%">
The RTL_QUERY_REGISTRY_DIRECT flag is set, and the buffer specified by <b>EntryContext</b> is too small to hold the key value data.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>
</td>
<td width="60%">
The RTL_QUERY_REGISTRY_TYPECHECK flag is set and the type of the stored registry value does not match the type expected by the caller.

</td>
</tr>
</table> 

<b>RtlQueryRegistryValues</b> also terminates processing of the table if the <i>QueryRoutine</i> function for a table entry returns an NTSTATUS error code, and returns that error code as its result. (With one exception: If <i>QueryRoutine</i> returns STATUS_BUFFER_TOO_SMALL, the error code is ignored.)

## Remarks

The caller specifies an initial key path and a table. The table contains one or more entries that describe the key values and subkey names in which the caller is interested. The table is terminated by an entry with a <b>NULL</b> <b>QueryRoutine</b> member and a <b>NULL</b> <b>Name</b> member. The table must be allocated from nonpaged pool.
<div class="alert"><b>Note</b>  Kernel-mode drivers must specify the RTL_QUERY_REGISTRY_NOEXPAND flag to prevent calling environment variable routines. These routines are unsafe, so kernel-mode drivers should not use them.</div><div> </div><div class="alert"><b>Caution</b>  If you use the RTL_QUERY_REGISTRY_DIRECT flag, an untrusted user-mode application may be able to cause a buffer overflow. A buffer overflow can occur if a driver uses this flag to read a registry value to which the wrong type is assigned. In all cases, a driver that uses the RTL_QUERY_REGISTRY_DIRECT flag should additionally use the RTL_QUERY_REGISTRY_TYPECHECK flag to prevent such overflows.</div><div> </div>If the RTL_QUERY_REGISTRY_TYPECHECK flag is set in a table entry, the caller must specify the expected REG_<i>XXX</i> type in the 8 most significant bits (MSBs) of the 32-bit <b>DefaultType</b> member of the table entry. As shown in the following code example, the RTL_QUERY_REGISTRY_TYPECHECK_SHIFT constant, which is defined to be 24, can be used as the shift count required to place the expected REG_<i>XXX</i> type in the 8 MSBs of the <b>DefaultType</b> member.
<div class="code"><span codelanguage="ManagedCPlusPlus"><table>
<tr>
<th>C++</th>
</tr>
<tr>
<td>
<pre>RTL_QUERY_REGISTRY_TABLE QueryRegTable[2];    
...
QueryRegTable[0].DefaultType = (REG_SZ &lt;&lt; RTL_QUERY_REGISTRY_TYPECHECK_SHIFT) | REG_NONE;
...
QueryRegTable[1].DefaultType = (REG_DWORD &lt;&lt; RTL_QUERY_REGISTRY_TYPECHECK_SHIFT) | REG_NONE;
...</pre>
</td>
</tr>
</table></span></div>Starting with Windows 8, if an <b>RtlQueryRegistryValues</b> call accesses an untrusted hive, and the caller sets the RTL_QUERY_REGISTRY_DIRECT flag for this call, the caller must additionally set the RTL_QUERY_REGISTRY_TYPECHECK flag. A violation of this rule by a call from user mode causes an exception.  A violation of this rule by a call from kernel mode causes a 0x139 bug check (KERNEL_SECURITY_CHECK_FAILURE).

Only system hives are trusted. An <b>RtlQueryRegistryValues</b> call that accesses a system hive does not cause an exception or a bug check if the RTL_QUERY_REGISTRY_DIRECT flag is set and the RTL_QUERY_REGISTRY_TYPECHECK flag is not set. However, as a best practice, the RTL_QUERY_REGISTRY_TYPECHECK flag should always be set if the RTL_QUERY_REGISTRY_DIRECT flag is set.

Similarly, in versions of Windows before Windows 8, as a best practice, an <b>RtlQueryRegistryValues</b> call that sets the RTL_QUERY_REGISTRY_DIRECT flag should additionally set the RTL_QUERY_REGISTRY_TYPECHECK flag. However, failure to follow this recommendation does not cause an exception or a bug check.

The following is a list of system hives:
<ul>
<li>\REGISTRY\MACHINE\HARDWARE</li>
<li>\REGISTRY\MACHINE\SOFTWARE</li>
<li>\REGISTRY\MACHINE\SYSTEM</li>
<li>\REGISTRY\MACHINE\SECURITY</li>
<li>\REGISTRY\MACHINE\SAM</li>
</ul>Support for the RTL_QUERY_REGISTRY_TYPECHECK flag is available through Windows Update for Windows 7, Windows Vista, Windows Server 2003, and Windows XP. For more information about this update, see <a href="http://go.microsoft.com/fwlink/p/?linkid=210698">Vulnerabilities in Windows Kernel Could Allow Elevation of Privilege (2393802)</a>. In versions of these operating systems that do not have this update, the caller can use the RTL_QUERY_REGISTRY_TYPECHECK flag. However, this flag is ignored by the <b>RtlQueryRegistryValues</b> routine.

Starting with Windows Driver Kit (WDK) 8, the RTL_QUERY_REGISTRY_TYPECHECK flag is defined in the Wdm.h header file as follows:
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>#define RTL_QUERY_REGISTRY_TYPECHECK 0x00000100</pre>
</td>
</tr>
</table></span></div>If an entry does not specify the RTL_QUERY_REGISTRY_DIRECT flag, <b>RtlQueryRegistryValues</b> uses the specified <i>QueryRoutine</i> function to report the value name, type, data, and data length, in bytes, to the caller. If the <b>Name</b> member of the entry is <b>NULL</b>, <b>RtlQueryRegistryValues</b> reports every direct subkey of the key. If the key type is REG_MULTI_SZ and the RTL_QUERY_REGISTRY_NOEXPAND flag not is specified, the routine calls <i>QueryRoutine</i> separately for each individual string; otherwise the routine reports it as a single value. If an entry specifies the RTL_QUERY_REGISTRY_DIRECT flag, <b>RtlQueryRegistryValues</b> stores the value of the key in the buffer pointed to by the entry's <b>EntryContext</b> member. The format of the returned data is as follows.
<table>
<tr>
<th>Key data type</th>
<th>How data is returned</th>
</tr>
<tr>
<td>
A null-terminated Unicode string (such as REG_SZ, REG_EXPAND_SZ).

</td>
<td>
<b>EntryContext</b> must point to an initialized <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure. If the <b>Buffer</b> member of <b>UNICODE_STRING</b> is <b>NULL</b>, the routine allocates storage for the string data. Otherwise, it stores the string data in the buffer that <b>Buffer</b> points to.

</td>
</tr>
<tr>
<td>
REG_MULTI_SZ

</td>
<td>
You must specify the RTL_QUERY_REGISTRY_NOEXPAND flag for this key data type. <b>EntryContext</b> points to an initialized <b>UNICODE_STRING</b> structure. The routine stores the key value as a single string value. Each individual component within the string is terminated by a zero.

If the <b>Buffer</b> member of <b>UNICODE_STRING</b> is <b>NULL</b>, the routine allocates storage for the string data. Otherwise, it stores the string data in the buffer that <b>Buffer</b> points to.

</td>
</tr>
<tr>
<td>
Nonstring data with size, in bytes, &lt;= <b>sizeof</b>(ULONG)

</td>
<td>
The value is stored in the memory location specified by <b>EntryContext</b>.

</td>
</tr>
<tr>
<td>
Nonstring data with size, in bytes, &gt; <b>sizeof</b>(ULONG)

</td>
<td>
The buffer pointed to by <b>EntryContext</b> must begin with a signed LONG value. The magnitude of the value must specify the size, in bytes, of the buffer. If the sign of the value is negative, <b>RtlQueryRegistryValues</b> will only store the data of the key value. Otherwise, it will use the first ULONG in the buffer to record the value length, in bytes, the second ULONG to record the value type, and the rest of the buffer to store the value data.

</td>
</tr>
</table> 

If an error occurs at any stage of processing of the query table, <b>RtlQueryRegistryValues</b> stops processing the table and returns the error status.

See <a href="..\wdm\nf-wdm-zwsetvaluekey.md">ZwSetValueKey</a> for a description of the possible REG_<i>XXX</i> values.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\wdm\nf-wdm-zwsetvaluekey.md">ZwSetValueKey</a>

<a href="..\wdm\nf-wdm-rtlzeromemory.md">RtlZeroMemory</a>

<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a>

<a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559969">QueryRoutine</a>

<a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlQueryRegistryValues routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>