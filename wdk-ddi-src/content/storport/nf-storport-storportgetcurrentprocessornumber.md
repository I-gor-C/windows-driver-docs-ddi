---
UID: NF.storport.StorPortGetCurrentProcessorNumber
title: StorPortGetCurrentProcessorNumber function
author: windows-driver-content
description: The StorPortGetCurrentProcessorNumber routine retrieves the current processor number from the kernel.
old-location: storage\storportgetcurrentprocessornumber.htm
old-project: storage
ms.assetid: 10d77823-fcaa-43c3-b55e-74f2da97ecf0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: StorPortGetCurrentProcessorNumber
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetCurrentProcessorNumber
req.alt-loc: storport.h
req.ddi-compliance: StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# StorPortGetCurrentProcessorNumber function



## -description
The <b>StorPortGetCurrentProcessorNumber</b> routine retrieves the current processor number from the kernel.



## -syntax

````
ULONG StorPortGetCurrentProcessorNumber(
  _In_  PVOID             HwDeviceExtension,
  _Out_ PPROCESSOR_NUMBER ProcNumber
);
````


## -parameters

### -param HwDeviceExtension [in]

A pointer to the hardware device extension for the host bus adapter (HBA).


### -param ProcNumber [out]

A pointer to a processor number structure that holds the return data.


## -returns
The <b>StorPortGetCurrentProcessorNumber</b> routine returns one of the following status codes:
<dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl>This function is not implemented on the active operating system.
<dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl>The operation was successful.
<dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl>The operation fails with this return value if one or more of the parameters are invalid, for example, if <i>ProcNumber</i> is set to <b>NULL</b>.

 


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
Available starting with Windows 7.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.storport_storportirql">StorPortIrql</a>
</td>
</tr>
</table>