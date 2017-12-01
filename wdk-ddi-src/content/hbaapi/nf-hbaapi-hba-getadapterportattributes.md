---
UID: NF.hbaapi.HBA_GetAdapterPortAttributes
title: HBA_GetAdapterPortAttributes
author: windows-driver-content
description: The HBA_GetAdapterPortAttributes routine retrieves the attributes for a specified remote fibre channel port.
old-location: storage\hba_getadapterportattributes.htm
old-project: storage
ms.assetid: f1f5dc4e-8069-4e3e-94a0-a9a7c359bdb4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_GetAdapterPortAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_GetAdapterPortAttributes
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
req.iface: 
---

# HBA_GetAdapterPortAttributes function



## -description
<p>The <b>HBA_GetAdapterPortAttributes</b> routine retrieves the attributes for a specified remote fibre channel port. </p>


## -syntax

````
HBA_STATUS HBA_API HBA_GetAdapterPortAttributes(
  _In_  HBA_HANDLE         HbaHandle,
  _In_  HBA_UINT32         PortIndex,
  _Out_ HBA_PORTATTRIBUTES *PortAttributes
);
````


## -parameters
<dl>

### -param <i>HbaHandle</i> [in]

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA on which the port is located. </p>
</dd>

### -param <i>PortIndex</i> [in]

<dd>
<p>Indicates which remote port to query on the HBA specified by <i>HbaHandle</i>. </p>
</dd>

### -param <i>PortAttributes</i> [out]

<dd>
<p>Pointer to a structure of type <a href="..\hbaapi\ns-hbaapi-hba-portattributes.md">HBA_PortAttributes</a> that, on return, contains the attributes of the remote port with an index of <i>PortIndex </i>on the HBA specified by <i>HbaHandle. </i></p>
</dd>
</dl>

## -returns
<p>The <b>HBA_GetAdapterPortAttributes</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. A value of HBA_STATUS_OK indicates that the operation succeeded. A value of HBA_STATUS_ERROR indicates that an unspecified error occurred that prevented the retrieval of the port attributes. </p>

## -remarks
<p>The <b>HBA_GetAdapterPortAttributes</b> routine retrieves attributes for remote ports of type Nx_Port. For a definition of Nx_Port, see the T11 committee's specification for <i>Fibre Channel HBA API</i>.</p>

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
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-portattributes.md">HBA_PortAttributes</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_GetAdapterPortAttributes routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
