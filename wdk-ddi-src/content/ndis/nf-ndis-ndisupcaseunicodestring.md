---
UID: NF.ndis.NdisUpcaseUnicodeString
title: NdisUpcaseUnicodeString
author: windows-driver-content
description: The NdisUpcaseUnicodeString function converts a copy of a given Unicode string to upper case and returns the converted string.Note  This function is deprecated for NDIS 6.0 and later.
old-location: netvista\ndisupcaseunicodestring.htm
old-project: netvista
ms.assetid: 5f735c98-26a6-4644-9fd4-b832ac9379c2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisUpcaseUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use RtlUpcaseUnicodeString instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisUpcaseUnicodeString
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
req.iface: 
---

# NdisUpcaseUnicodeString function



## -description
<p>The 
  <b>NdisUpcaseUnicodeString</b> function converts a copy of a given Unicode string to upper case and returns
  the converted string.</p>


## -syntax

````
NTSTATUS NdisUpcaseUnicodeString(
  _Out_ PUNICODE_STRING DestinationString,
  _In_  PUNICODE_STRING SourceString
);
````


## -parameters
<dl>

### -param <i>DestinationString</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer in which to return the converted string.</p>
</dd>

### -param <i>SourceString</i> [in]

<dd>
<p>A pointer to the source Unicode string to be converted to upper case.</p>
</dd>
</dl>

## -returns
<p><b>NdisUpcaseUnicodeString</b> returns STATUS_SUCCESS if it returned the converted string in the buffer
     at 
     <i>DestinationString</i> .</p>

## -remarks


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
<p>Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use <a href="..\ntddk\nf-ntddk-rtlupcaseunicodestring.md">RtlUpcaseUnicodeString</a> instead.</p>
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
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlinitunicodestring.md">RtlInitUnicodeString</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlunicodestringtoansistring.md">RtlUnicodeStringToAnsiString</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisUpcaseUnicodeString function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
