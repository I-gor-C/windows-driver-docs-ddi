---
UID: NS.sti._STI_DIAG
title: STI_DIAG
author: windows-driver-content
description: The STI_DIAG structure is used as a parameter to the IStiDevice::Diagnostic and IStiUSD::Diagnostic methods.
old-location: image\sti_diag.htm
old-project: image
ms.assetid: 07caa8b0-849c-4ad9-9adb-b1726edc9234
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: STI_DIAG, STI_DIAG, *LPSTI_DIAG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sti.h
req.include-header: Sti.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STI_DIAG
req.alt-loc: sti.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IStiDevice
req.product: Windows 10 or later.
---

# STI_DIAG structure



## -description
<p>The STI_DIAG structure is used as a parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543736">IStiDevice::Diagnostic</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543814">IStiUSD::Diagnostic</a> methods.</p>


## -syntax

````
typedef struct _STI_DIAG {
  DWORD          dwSize;
  DWORD          dwBasicDiagCode;
  DWORD          dwVendorDiagCode;
  DWORD          dwStatusMask;
  STI_ERROR_INFO sErrorInfo;
} STI_DIAG, *LPSTI_DIAG;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Caller-supplied size, in bytes, of the STI_DIAG structure.</p>
</dd>

### -field <b>dwBasicDiagCode</b>

<dd>
<p>Bit flag indicating the type of test to be performed. Currently this must be STI_DIAGCODE_HWPRESENCE<i>.</i></p>
</dd>

### -field <b>dwVendorDiagCode</b>

<dd>
<p>Optional, vendor-defined diagnostic request code.</p>
</dd>

### -field <b>dwStatusMask</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>sErrorInfo</b>

<dd>
<p>Structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff548396">STI_ERROR_INFO</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>