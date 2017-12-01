---
UID: NF.ndis.NdisInitUnicodeString
title: NdisInitUnicodeString
author: windows-driver-content
description: The NdisInitUnicodeString function initializes a counted Unicode string.
old-location: netvista\ndisinitunicodestring.htm
old-project: netvista
ms.assetid: 073feb91-48ae-4ad5-9061-117e6541021c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisInitUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisInitUnicodeString (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisInitUnicodeString (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInitUnicodeString
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
req.irql: See Remarks section
req.iface: 
---

# NdisInitUnicodeString function



## -description
<p>The 
  <b>NdisInitUnicodeString</b> function initializes a counted Unicode string.</p>


## -syntax

````
VOID NdisInitUnicodeString(
  _Inout_ PNDIS_STRING DestinationString,
  _In_    PCWSTR       SourceString
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [in, out]

<dd>
<p>A pointer to a caller-allocated NDIS_STRING type in which 
     <b>NdisInitUnicodeString</b> should store the counted Unicode string. For Windows 2000 and later, NDIS
     defines the NDIS_STRING type as a 
     <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> type.</p>
</dd>

### -param <i>SourceString</i> [in]

<dd>
<p>A pointer to a null-terminated string with which to initialize the counted string.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <i>DestinationString</i> is initialized to point to the 
    <i>SourceString</i> . The 
    <b>Length</b> and 
    <b>MaximumLength</b> members of NDIS_STRING for the 
    <i>DestinationString</i> are initialized to the length of the string at 
    <i>SourceString</i>. If 
    <i>SourceString</i> is <b>NULL</b>, the length is zero.</p>

<p>Callers of 
    <b>NdisInitUnicodeString</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the 
    <i>DestinationString</i> buffer is allocated from nonpaged memory. Usually, callers are running at IRQL =
    PASSIVE_LEVEL during driver initialization.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/9eec98d4-3e4f-4e2c-9f8c-ff612d5de603">NdisInitUnicodeString (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInitUnicodeString (NDIS
   5.1)</b>) in Windows XP.</p>
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
<p>See Remarks section</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisansistringtounicodestring.md">
   NdisAnsiStringToUnicodeString</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinitansistring.md">NdisInitAnsiString</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinitializestring.md">NdisInitializeString</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisunicodestringtoansistring.md">
   NdisUnicodeStringToAnsiString</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitUnicodeString function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
