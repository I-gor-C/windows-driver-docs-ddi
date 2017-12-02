---
UID: NF.hbaapi.HBA_GetAdapterAttributes
title: HBA_GetAdapterAttributes
author: windows-driver-content
description: The HBA_GetAdapterAttributes routine retrieves the attributes for an HBA.
old-location: storage\hba_getadapterattributes.htm
old-project: storage
ms.assetid: a172f53c-9993-4d52-ae3f-35a8ab5745f6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_GetAdapterAttributes
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
req.alt-api: HBA_GetAdapterAttributes
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

# HBA_GetAdapterAttributes function



## -description
<p>The <b>HBA_GetAdapterAttributes</b> routine retrieves the attributes for an HBA. </p>


## -syntax

````
HBA_STATUS HBA_API HBA_GetAdapterAttributes(
  _In_  HBA_HANDLE            HbaHandle,
  _Out_ HBA_ADAPTERATTRIBUTES *HbaAdapterAttributes
);
````


## -parameters
<dl>

### -param HbaHandle [in]

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA on which the port is located.  </p>
</dd>

### -param HbaAdapterAttributes [out]

<dd>
<p>Contains, on return, a structure of type <a href="..\hbaapi\ns-hbaapi-hba-adapterattributes.md">HBA_AdapterAttributes</a> that holds the HBA attributes. </p>
</dd>
</dl>

## -returns
<p>The <b>HBA_GetAdapterAttributes</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA.</p>

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
<a href="..\hbaapi\ns-hbaapi-hba-adapterattributes.md">HBA_AdapterAttributes</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_GetAdapterAttributes routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
