---
UID: NF:wdfdriver.WdfWdmDriverGetWdfDriverHandle
title: WdfWdmDriverGetWdfDriverHandle function
author: windows-driver-content
description: The WdfWdmDriverGetWdfDriverHandle method returns a handle to the framework driver object that is associated with a specified Windows Driver Model (WDM) driver object.
old-location: wdf\wdfwdmdrivergetwdfdriverhandle.htm
old-project: wdf
ms.assetid: 2126d36c-42c1-4e29-bf82-9f5682482557
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: WdfWdmDriverGetWdfDriverHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfWdmDriverGetWdfDriverHandle
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: Any level
req.typenames: WDF_DRIVER_INIT_FLAGS
req.product: Windows 10 or later.
---

# WdfWdmDriverGetWdfDriverHandle function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfWdmDriverGetWdfDriverHandle</b> method returns a handle to the framework driver object that is associated with a specified Windows Driver Model (WDM) driver object.



## -syntax

````
WDFDRIVER WdfWdmDriverGetWdfDriverHandle(
  _In_ PDRIVER_OBJECT DriverObject
);
````


## -parameters

### -param DriverObject [in]

A pointer to a WDM driver object.


## -returns
<b>WdfWdmDriverGetWdfDriverHandle</b> returns a handle to a framework driver object. A system bug check occurs if the <i>DriverObject</i> pointer is <b>NULL</b>. 

The following code example obtains a handle to the framework driver object that is associated with a specified WDM driver object.


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
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdriver.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>