---
UID: NF.storport.StorPortInvokeAcpiMethod
title: StorPortInvokeAcpiMethod
author: windows-driver-content
description: The StorPortInvokeAcpiMethod routine executes an ACPI method for a storage device.
old-location: storage\storportinvokeacpimethod.htm
old-project: storage
ms.assetid: 2A8EF694-B699-46A0-9B1D-B7D0831F3944
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortInvokeAcpiMethod
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortInvokeAcpiMethod
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortInvokeAcpiMethod function



## -description
<p>The <b>StorPortInvokeAcpiMethod</b> routine executes an ACPI method for a storage device.</p>


## -syntax

````
ULONG StorPortInvokeAcpiMethod(
  _In_      PVOID         HwDeviceExtension,
  _In_opt_  PSTOR_ADDRESS Address,
  _In_      ULONG         MethodName,
  _In_opt_  PVOID         InputBuffer,
  _In_      ULONG         InputBufferLength,
  _In_opt_  PVOID         OutputBuffer,
  _In_      ULONG         OutputBufferLength,
  _Out_opt_ PULONG        BytesReturned
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>Address</i> [in, optional]

<dd>
<p>The address of the target device. This parameter is optional. If <i>Address</i> is set to <b>NULL</b>, the adapter is the target.</p>
</dd>

### -param <i>MethodName</i> [in]

<dd>
<p>A four-byte name for the ACPI method. For example, ((ULONG) 'DDS_') would name the _SDD, or 'Set Device Data',  ACPI method for an AHCI controller.</p>
</dd>

### -param <i>InputBuffer</i> [in, optional]

<dd>
<p>A pointer to the input data to the method.</p>
</dd>

### -param <i>InputBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the buffer in <i>InputBuffer</i>.</p>
</dd>

### -param <i>OutputBuffer</i> [in, optional]

<dd>
<p>A pointer to the output data from the method.</p>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the buffer in <i>OutputBuffer</i>.</p>
</dd>

### -param <i>BytesReturned</i> [out, optional]

<dd>
<p>A pointer to the length, in bytes, of the data returned in <i>OutputBuffer</i>.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortInvokeAcpiMethod</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_INVALID_UNSUCCESSFUL</b></dt>
</dl><p>A general error condition exists.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p><i>HwDeviceExtension</i>,  <i>InputBuffer</i>, or <i>OutputBuffer</i> is NULL.</p>

<p>-or-</p>

<p><i>Address</i> refers to a target that does not exist.</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p> The ACPI method is not implemented.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p> Insufficient resources are available to execute the method, or <i>OutputBufferLength</i> is not large enough for the returned data.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>Current IRQL &gt; PASSIVE_LEVEL.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The method executed successfully.</p>

<p> </p>

## -remarks
<p>The <b>StorPortInvokeAcpiMethod</b> enables a miniport driver to invoke ACPI methods defined for storage controllers and storage LUNs. The method names are four-byte character strings that occupy a <b>ULONG</b> value in <i>MethodName</i>.</p>

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
<p>Available in Windows 8 and later versions of Windows.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>