---
UID: NS.STI._STI_DIAG
title: _STI_DIAG
author: windows-driver-content
description: The STI_DIAG structure is used as a parameter to the IStiDevice::Diagnostic and IStiUSD::Diagnostic methods.
old-location: image\sti_diag.htm
old-project: Image
ms.assetid: 07caa8b0-849c-4ad9-9adb-b1726edc9234
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _STI_DIAG, *LPSTI_DIAG, STI_DIAG, LPSTI_DIAG
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
req.product: Windows 10 or later.
---

# _STI_DIAG structure



## -description
The STI_DIAG structure is used as a parameter to the <a href="image.istidevice_diagnostic">IStiDevice::Diagnostic</a> and <a href="image.istiusd_diagnostic">IStiUSD::Diagnostic</a> methods.



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

### -field dwSize

Caller-supplied size, in bytes, of the STI_DIAG structure.


### -field dwBasicDiagCode

Bit flag indicating the type of test to be performed. Currently this must be STI_DIAGCODE_HWPRESENCE<i>.</i>


### -field dwVendorDiagCode

Optional, vendor-defined diagnostic request code.


### -field dwStatusMask

Reserved for future use.


### -field sErrorInfo

Structure of type <a href="image.sti_error_info">STI_ERROR_INFO</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>