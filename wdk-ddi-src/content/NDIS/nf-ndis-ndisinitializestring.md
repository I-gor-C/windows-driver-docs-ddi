---
UID: NF.ndis.NdisInitializeString
title: NdisInitializeString
author: windows-driver-content
description: The NdisInitializeString function allocates storage for and initializes a counted string in the system-default character set.
old-location: netvista\ndisinitializestring.htm
ms.assetid: c6945d7d-5152-4968-a628-7850b8083a82
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use RtlInitUnicodeString  or RTL_CONSTANT_STRING or   DECLARE_CONST_UNICODE_STRING (see ntdef.h) instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInitializeString
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisInitializeString
req.iface: 
---

# NdisInitializeString function



## -description
<p>The 
  <b>NdisInitializeString</b> function allocates storage for and initializes a counted string in the
  system-default character set.</p>


## -syntax

````
VOID NdisInitializeString(
  _Out_ PNDIS_STRING DestinationString,
  _In_  PUCHAR       SourceString
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [out]

<dd>
<p>A pointer that is <b>NULL</b> when 
     <b>NdisInitializeString</b> is called; on return from this function, this parameter points to an
     NDIS_STRING type that describes an initialized counted string. For Windows 2000 and later, NDIS defines
     the NDIS_STRING type as a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> type.</p>
</dd>

### -param <i>SourceString</i> [in]

<dd>
<p>A pointer to a null-terminated string with which to initialize the counted string. 
     <i>SourceString</i> must not be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisInitializeString</b> sets the 
    <b>Length</b> and 
    <b>MaximumLength</b> members of NDIS_STRING for the destination string and terminates the destination
    string with zero. For Windows 2000 and later drivers, 
    <b>NdisInitializeString</b> converts the supplied source string to Unicode characters.</p>

<p><i>SourceString</i> must not be <b>NULL</b>.</p>

<p>The buffer allocated by 
    <b>NdisInitializeString</b> should be released with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562604">NdisFreeString</a> function.</p>

<p><b>NdisInitializeString</b> sets the 
    <b>Length</b> and 
    <b>MaximumLength</b> members of NDIS_STRING for the destination string and terminates the destination
    string with zero. For Windows 2000 and later drivers, 
    <b>NdisInitializeString</b> converts the supplied source string to Unicode characters.</p>

<p><i>SourceString</i> must not be <b>NULL</b>.</p>

<p>The buffer allocated by 
    <b>NdisInitializeString</b> should be released with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562604">NdisFreeString</a> function.</p>

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
<p>Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff561934">RtlInitUnicodeString</a>  or <a href="kernel.rtl_constant_string">RTL_CONSTANT_STRING</a> or   DECLARE_CONST_UNICODE_STRING (see ntdef.h) instead.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540605">ANSI_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cd668a59-f74f-427b-880a-9352a7e09fa8">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561729">RtlAnsiStringToUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561854">RtlEqualUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561899">RtlFreeAnsiString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561903">RtlFreeUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561929">RtlInitString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561934">RtlInitUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562969">RtlUnicodeStringToAnsiString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitializeString function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
