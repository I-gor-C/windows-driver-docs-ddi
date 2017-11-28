---
UID: NF.hbaapi.HBA_GetDiscoveredPortAttributes
title: HBA_GetDiscoveredPortAttributes
author: windows-driver-content
description: The HBA_GetDiscoveredPortAttributes routine retrieves the attributes for a specified remote fibre channel port.
old-location: storage\hba_getdiscoveredportattributes.htm
old-project: storage
ms.assetid: 64c6ed50-a4b9-4a8c-b38c-b2fcdf5ccee9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_GetDiscoveredPortAttributes
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
req.alt-api: HBA_GetDiscoveredPortAttributes
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

# HBA_GetDiscoveredPortAttributes function



## -description
<p>The <b>HBA_GetDiscoveredPortAttributes</b> routine retrieves the attributes for a specified remote fibre channel port.</p>


## -syntax

````
HBA_STATUS HBA_API HBA_GetDiscoveredPortAttributes(
  _In_  HBA_HANDLE         HbaHandle,
  _In_  HBA_UINT32         PortIndex,
  _In_  HBA_UINT32         DiscoveredPortIndex,
  _Out_ HBA_PORTATTRIBUTES *HbaPortAttributes
);
````


## -parameters
<dl>

### -param <i>HbaHandle</i> [in]

<dd>
<p>Contains a value returned by the routine <a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a> that identifies the HBA on which the port is located.  </p>
</dd>

### -param <i>PortIndex</i> [in]

<dd>
<p>Indicates the index of the local port of type Nx_Port through which to query the discovered remote port. For a definition of Nx_Port, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -param <i>DiscoveredPortIndex</i> [in]

<dd>
<p>Indicates the index of the remote port to query. </p>
</dd>

### -param <i>HbaPortAttributes</i> [out]

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557107">HBA_PortAttributes</a> that reports the port attributes. </p>
</dd>
</dl>

## -returns
<p>The <b>HBA_GetDiscoveredPortAttributes</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. </p>

## -remarks
<p>The <b>HBA_GetDiscoveredPortAttributes</b> library routine corresponds to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553925">GetDiscoveredPortAttributes</a> WMI method. </p>

<p>The <b>HBA_GetDiscoveredPortAttributes</b> library routine corresponds to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553925">GetDiscoveredPortAttributes</a> WMI method. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553925">GetDiscoveredPortAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557107">HBA_PortAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_GetDiscoveredPortAttributes routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
