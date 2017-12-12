---
UID: NF.ndis.NdisFDeregisterFilterDriver
title: NdisFDeregisterFilterDriver function
author: windows-driver-content
description: A filter drivers calls the NdisFDeregisterFilterDriver function to release resources that it previously allocated with the NdisFRegisterFilterDriver function.
old-location: netvista\ndisfderegisterfilterdriver.htm
old-project: netvista
ms.assetid: f97ecce3-73b9-4c51-b4a4-e114420af2c9
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisFDeregisterFilterDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFDeregisterFilterDriver
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Filter_Driver_Function, NdisFDeregisterFilterDriver
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

# NdisFDeregisterFilterDriver function



## -description
A filter drivers calls the
  <b>NdisFDeregisterFilterDriver</b> function to release resources that it previously allocated with the 
  <a href="netvista.ndisfregisterfilterdriver">
  NdisFRegisterFilterDriver</a> function.



## -syntax

````
VOID NdisFDeregisterFilterDriver(
  _In_ NDIS_HANDLE NdisFilterDriverHandle
);
````


## -parameters

### -param NdisFilterDriverHandle [in]

The filter driver handle that identifies this filter driver. NDIS returned the handle to the
     filter driver in a call to 
     <b>NdisFRegisterFilterDriver</b>.


## -returns
None


## -remarks
A filter driver must call 
    <b>NdisFDeregisterFilterDriver</b> from its 
    <a href="netvista.filterdriverunload">FilterDriverUnload</a> routine.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.0 and later.

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
<a href="devtest.ndis_irql_filter_driver_function">Irql_Filter_Driver_Function</a>, <a href="devtest.ndis_ndisfderegisterfilterdriver">NdisFDeregisterFilterDriver</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.filterdriverunload">FilterDriverUnload</a>
</dt>
<dt>
<a href="netvista.ndisfregisterfilterdriver">NdisFRegisterFilterDriver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFDeregisterFilterDriver function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

