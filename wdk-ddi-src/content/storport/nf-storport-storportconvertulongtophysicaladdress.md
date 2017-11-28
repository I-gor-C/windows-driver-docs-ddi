---
UID: NF.storport.StorPortConvertUlongToPhysicalAddress
title: StorPortConvertUlongToPhysicalAddress
author: windows-driver-content
description: The StorPortConvertUlongToPhysicalAddress routine converts an unsigned long address into a physical address.
old-location: storage\storportconvertulongtophysicaladdress.htm
old-project: storage
ms.assetid: 772ca60b-a957-47de-b95d-486497b295ce
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortConvertUlongToPhysicalAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortConvertUlongToPhysicalAddress
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortConvertUlongToPhysicalAddress function



## -description
<p>The <b>StorPortConvertUlongToPhysicalAddress</b> routine converts an unsigned long address into a physical address.</p>


## -syntax

````
STORPORT_API STOR_PHYSICAL_ADDRESS StorPortConvertUlongToPhysicalAddress(
  _In_ ULONG_PTR UlongAddress
);
````


## -parameters
<dl>

### -param <i>UlongAddress</i> [in]

<dd>
<p>Contains the address to be converted.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortConvertUlongToPhysicalAddress</b> routine returns the physical address that corresponds to the unsigned long address that the caller passed in.</p>

<p><b>ULONG64</b></p>

<p><b>StorPortConvertPhysicalAddressToULong64</b> returns a ULONG64 value derived from the physical address that was passed to it.</p>

<p> </p>

<p>StorPortConvertPhysicalAddressToULong64 uses <b>STOR_PHYSICAL_ADDRESS</b> to represent physical addresses.</p>

<p><b>ULONG64</b></p>

<p><b>StorPortConvertPhysicalAddressToULong64</b> returns a ULONG64 value derived from the physical address that was passed to it.</p>

<p> </p>

<p>StorPortConvertPhysicalAddressToULong64 uses <b>STOR_PHYSICAL_ADDRESS</b> to represent physical addresses.</p>

## -remarks
<p><b>StorPortConvertUlongToPhysicalAddress</b> uses <b>STOR_PHYSICAL_ADDRESS</b> to represent physical addresses.</p>

<p>The <b>STOR_PHYSICAL_ADDRESS</b> type is an operating system-independent data type that Storport miniport drivers use to represent either a physical addresses or a bus-relative address. </p>

<p>The StorPortConvertPhysicalAddressToULong64 macro converts a physical address to a ULONG64 value.</p>

<p></p>

<p><a id="Address__in_"></a><a id="address__in_"></a><a id="ADDRESS__IN_"></a><i>Address [in]</i></p>

<p><b>STOR_PHYSICAL_ADDRESS</b></p>

<p>Specifies an address value of type STOR_PHYSICAL_ADDRESS.</p>

<p><a id="Return_value"></a><a id="return_value"></a><a id="RETURN_VALUE"></a>Return value</p>

<p><b>StorPortConvertUlongToPhysicalAddress</b> uses <b>STOR_PHYSICAL_ADDRESS</b> to represent physical addresses.</p>

<p>The <b>STOR_PHYSICAL_ADDRESS</b> type is an operating system-independent data type that Storport miniport drivers use to represent either a physical addresses or a bus-relative address. </p>

<p>The StorPortConvertPhysicalAddressToULong64 macro converts a physical address to a ULONG64 value.</p>

<p></p>

<p><a id="Address__in_"></a><a id="address__in_"></a><a id="ADDRESS__IN_"></a><i>Address [in]</i></p>

<p><b>STOR_PHYSICAL_ADDRESS</b></p>

<p>Specifies an address value of type STOR_PHYSICAL_ADDRESS.</p>

<p><a id="Return_value"></a><a id="return_value"></a><a id="RETURN_VALUE"></a>Return value</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>