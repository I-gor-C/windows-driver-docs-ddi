---
UID: NF.ndis.NdisEqualString
title: NdisEqualString macro
author: windows-driver-content
description: The NdisEqualString function compares two strings, in the OS-default character set, to determine whether they are equal.
old-location: netvista\ndisequalstring.htm
old-project: NetVista
ms.assetid: cc5da07d-fcd2-40f9-8ba9-d7ddf35e7b7f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisEqualString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use RtlEqualUnicodeString instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisEqualString
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
---

# NdisEqualString macro



## -description
The 
  <b>NdisEqualString</b> function compares two strings, in the OS-default character set, to determine whether
  they are equal.



## -syntax

````
BOOLEAN NdisEqualString(
  [in] PNDIS_STRING String1,
  [in] PNDIS_STRING String2,
  [in] BOOLEAN      CaseInsensitive
);
````


## -parameters

### -param String1 [in]

A pointer to an NDIS_STRING type that describes the first string.


### -param String2 [in]

A pointer to an NDIS_STRING type that describes the second string.


### -param CaseInsensitive [in]

A boolean value that is <b>TRUE</b> if case should be ignored when doing the comparison. Otherwise, it is
     <b>FALSE</b>.


## -remarks
Starting with Windows 2000, a string of type NDIS_STRING is a counted, null-terminated Unicode string.
    That is, NDIS defines the NDIS_STRING type as a 
    <a href="kernel.unicode_string">UNICODE_STRING</a> type.


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
Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use <a href="kernel.rtlequalunicodestring">RtlEqualUnicodeString</a> instead.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ansi_string">ANSI_STRING</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_bind_adapter_ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="kernel.rtlinitstring">RtlInitString</a>
</dt>
<dt>
<a href="kernel.rtlinitunicodestring">RtlInitUnicodeString</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisEqualString macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

