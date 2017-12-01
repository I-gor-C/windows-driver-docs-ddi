---
UID: NF.usbcamdi.USBCAMD_GetRegistryKeyValue
title: USBCAMD_GetRegistryKeyValue
author: windows-driver-content
description: The USBCAMD_GetRegistryKeyValue function retrieves the device-instance-specific registry key value.
old-location: stream\usbcamd_getregistrykeyvalue.htm
old-project: stream
ms.assetid: c3512a79-884f-4f38-9942-63a4a464585c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: USBCAMD_GetRegistryKeyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_GetRegistryKeyValue
req.alt-loc: usbcamd2.lib,usbcamd2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbcamd2.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# USBCAMD_GetRegistryKeyValue function



## -description
<p>The <b>USBCAMD_GetRegistryKeyValue</b> function retrieves the device-instance-specific registry key value.</p>


## -syntax

````
NTSTATUS USBCAMD_GetRegistryKeyValue(
  _In_ HANDLE Handle,
  _In_ PWCHAR KeyNameString,
  _In_ ULONG  KeyNameStringLength,
  _In_ PVOID  Data,
  _In_ ULONG  DataLength
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Handle to a valid and open device registry key.</p>
</dd>

### -param <i>KeyNameString</i> [in]

<dd>
<p>Pointer to the string buffer describing the key type.</p>
</dd>

### -param <i>KeyNameStringLength</i> [in]

<dd>
<p>Specifies the length, in characters, of <i>KeyNameString</i>.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>Pointer to a caller-specified value or structure.</p>
</dd>

### -param <i>DataLength</i> [in]

<dd>
<p>Specifies the length, in bytes, of the value or structure at <i>Data.</i></p>
</dd>
</dl>

## -returns
<p><b>USBCAMD_GetRegistryKeyValue </b>returns STATUS_SUCCESS if the call was successful. Other possible error codes include:</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>There was insufficient memory to continue.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamd2.lib</dt>
</dl>
</td>
</tr>
</table>