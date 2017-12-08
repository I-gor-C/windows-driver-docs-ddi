---
UID: NF.ntddk.RtlCharToInteger
title: RtlCharToInteger function
author: windows-driver-content
description: The RtlCharToInteger routine converts a single-byte character string to an integer value in the specified base.
old-location: kernel\rtlchartointeger.htm
old-project: kernel
ms.assetid: a08cb12a-c574-4871-9bba-f8f3a766f377
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlCharToInteger
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCharToInteger
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
req.irql: PASSIVE_LEVEL
---

# RtlCharToInteger function



## -description
The <b>RtlCharToInteger</b> routine converts a single-byte character string to an integer value in the specified base. 


## -syntax

````
NTSTATUS RtlCharToInteger(
  _In_     PCSZ   String,
  _In_opt_ ULONG  Base,
  _Out_    PULONG Value
);
````


## -parameters

### -param String [in]

Pointer to a null-terminated, single-byte character string. 

### -param Base [in, optional]

Specifies decimal, binary, octal, or hexadecimal base. If this parameter is not given, the routine will look for 0x, 0o, and 0b prefixes in the input string to determine if the base should be decimal (default), binary, octal, or hexadecimal.

### -param Value [out]

Pointer to a location to which the converted value is returned. 

## -returns
<b>RtlCharToInteger</b> returns STATUS_SUCCESS if the given character string is converted. Otherwise, it can return STATUS_INVALID_PARAMETER. 

## -remarks
<b>RtlCharToInteger</b> converts ANSI alphanumeric characters. 

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlinitstring">RtlInitString</a>
</dt>
<dt>
<a href="kernel.rtlintegertounicodestring">RtlIntegerToUnicodeString</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlCharToInteger routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
