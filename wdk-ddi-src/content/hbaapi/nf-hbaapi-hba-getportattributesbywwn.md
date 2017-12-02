---
UID: NF.hbaapi.HBA_GetPortAttributesByWWN
title: HBA_GetPortAttributesByWWN
author: windows-driver-content
description: The HBA_GetPortAttributesByWWN routine retrieves the attributes for the port specified by the indicated port name.
old-location: storage\hba_getportattributesbywwn.htm
old-project: storage
ms.assetid: 79d63b5e-78b0-452a-aa84-695c59a7d4a5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_GetPortAttributesByWWN
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
req.alt-api: HBA_GetPortAttributesByWWN
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

# HBA_GetPortAttributesByWWN function



## -description
<p>The <b>HBA_GetPortAttributesByWWN</b> routine retrieves the attributes for the port specified by the indicated port name. </p>


## -syntax

````
HBA_STATUS HBA_API HBA_GetPortAttributesByWWN(
  _In_  HBA_HANDLE         HbaHandle,
  _In_  HBA_WWN            PortWWN,
  _Out_ HBA_PORTATTRIBUTES *HbaPortAttributes
);
````


## -parameters
<dl>

### -param HbaHandle [in]

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA on which the port is located.  </p>
</dd>

### -param PortWWN [in]

<dd>
<p>Contains the worldwide name (WWN) of the port whose attributes to retrieve. For a definition of worldwide names, see the T11 committee's <i>Fibre Channel HBA API </i>specification .</p>
</dd>

### -param HbaPortAttributes [out]

<dd>
<p>Contains a structure of type <a href="..\hbaapi\ns-hbaapi-hba-portattributes.md">HBA_PortAttributes</a> that holds the port attributes: </p>
</dd>
</dl>

## -returns
<p>The <b>HBA_GetPortAttributesByWWN</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. </p>

## -remarks
<p>The <b>HBA_GetPortAttributesByWWN</b> routine serves a purpose very similar to the <a href="storage.getdiscoveredportattributes">GetDiscoveredPortAttributes</a> WMI method.</p>

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
<a href="storage.getdiscoveredportattributes">GetDiscoveredPortAttributes</a>
</dt>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_GetPortAttributesByWWN routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
