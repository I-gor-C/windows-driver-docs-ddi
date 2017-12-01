---
UID: NF.pwmutil.PwmParsePinPath
title: PwmParsePinPath
author: windows-driver-content
description: Parses a pin path under the Pulse Width Modulation (PWM) controller namespace to validate its format and extract the pin number.
old-location: kernel\pwmparsepinpath.htm
old-project: kernel
ms.assetid: 854A2B6F-A841-4AE4-9E54-68EF048C9504
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PwmParsePinPath
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pwmutil.h
req.include-header: Pwm.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.19
req.umdf-ver: 2.19
req.alt-api: PwmParsePinPath
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PwmParsePinPath function



## -description
<p>    Parses a pin path under the Pulse Width Modulation (PWM) controller namespace to validate
    its format and extract the pin number.</p>


## -syntax

````
NTSTATUS PwmParsePinPath(
  _In_      UNICODE_STRING *PinPath,
  _Out_opt_ ULONG          *PinNumber
);
````


## -parameters
<dl>

### -param <i>PinPath</i> [in]

<dd>
<p>A pointer to pin path as a Unicode character string.</p>
</dd>

### -param <i>PinNumber</i> [out, optional]

<dd>
<p>A pointer to variable that receives a pin number.</p>
</dd>
</dl>

## -returns
<p><b>PwmParsePinPath</b> returns the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Extracted pin path successfully from supplied pin path.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified pin path pointer is invalid or its Unicode string is
        invalid.</p><dl>
<dt><b>STATUS_NO_SUCH_FILE</b></dt>
</dl><p> The specified pin path does not constitute a valid pin path.</p>

<p> </p>

## -remarks
<p>The pin path must be a Unicode character string that ends in the pin number as follows: <i>...\&lt;PinNumber&gt;</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.19</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.19</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pwmutil.h (include Pwm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
</table>