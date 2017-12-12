---
UID: NF.wdm.RtlNumberOfSetBitsUlongPtr
title: RtlNumberOfSetBitsUlongPtr function
author: windows-driver-content
description: The RtlNumberOfSetBitsUlongPtr routine returns the number of bits in the specified ULONG_PTR integer value that are set to one.
old-location: kernel\rtlnumberofsetbitsulongptr.htm
old-project: kernel
ms.assetid: CD619018-7E6D-4B45-93C3-AD89FDFEB1E9
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: RtlNumberOfSetBitsUlongPtr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlNumberOfSetBitsUlongPtr
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
req.irql: Any IRQL
req.product: Windows 10 or later.
---

# RtlNumberOfSetBitsUlongPtr function



## -description
The <b>RtlNumberOfSetBitsUlongPtr</b> routine returns the number of bits in the specified ULONG_PTR integer value that are set to one.



## -syntax

````
ULONG RtlNumberOfSetBitsUlongPtr(
  _In_ ULONG_PTR Target
);
````


## -parameters

### -param Target [in]

A ULONG_PTR integer value.


## -returns
<b>RtlNumberOfSetBitsUlongPtr</b> returns a count of the bits in the <i>Target</i> parameter that are set to one.


## -remarks


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
Available starting with Windows Vista.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
Any IRQL

</td>
</tr>
</table>